#!venv/bin/python
from click import command, argument, File, option, Path
from lexer import lexer, LexingError
from pprint import pprint
from errors import *
from token_types import *
from os import system


@command(help='ITER compiler (version ITER40) made by Gornak40.')
@argument('source', type=File())
@option('--out', '-o', default='main', type=Path(writable=True, dir_okay=False), help='Set output file name.')
@option('--stack-size', '-s', default=5000, type=int, help='Set stack size for sunctions.')
class Main:
	tokens = list()
	assign = list()
	bss = list()
	sunc = list()
	text = list()
	local = list()
	ptr = 0
	label = 0
	ban = set()

	def get_label(self):
		self.label += 1
		return f'@{self.label - 1}'

	def __init__(self, source, out, stack_size):
		self.stack_size = stack_size
		self.tokens = list(self.set_include(source))
		self.check_balance()
		self.set_assign()
		self.set_bss()
		self.text = list(self.set_text())
		pprint(self.tokens)
		self.build(out)

	def build(self, out):
		with open(f'{out}.asm', 'w') as fout:
			print(*self.assign, sep='\n', file=fout)
			print('section .bss', file=fout)
			print(*set(self.bss), sep='\n', file=fout)
			with open('iter.asm') as fin:
				print(fin.read(), file=fout)
			print(*self.sunc, sep='\n', file=fout)
			print('main:', file=fout)
			print('@start', file=fout)
			print(*self.text, sep='\n', file=fout)
			print('@exit', file=fout)
		system(f'nasm -f elf32 {out}.asm -o {out}.o && gcc -m32 {out}.o -o {out}')


	def lex(self, source):
		res = list()
		for token in source.read().split():
			try:
				res.append(*lexer.lex(token))
			except LexingError:
				syntax_error(token)
		return res

	def check_balance(self):
		balance = 0
		for token in self.tokens:
			if token.gettokentype() == 'END':
				balance -= 1
			elif token.gettokentype() in OPEN:
				balance += 1
			if balance < 0:
				balance_error()
		if balance:
			balance_error()

	def set_include(self, source):
		for token in self.lex(source):
			if token.gettokentype() == 'INCLUDE':
				with open(f'{token.getstr()[1:]}.iter') as isource:
					for itoken in self.set_include(isource):
						yield itoken
			else:
				yield token

	def set_assign(self):
		for i, (ptoken, token) in enumerate(zip(self.tokens, self.tokens[1:])):
			if token.gettokentype() == 'SETCONST':
				if ptoken.gettokentype() not in CONSTVAL:
					const_error(ptoken)
				self.assign.append(f'%assign {token.getstr()[1:]} {ptoken.getstr()}')
				self.ban |= {i, i + 1}

	def set_bss(self):
		self.bss.append(f'@MEM40: resd {self.stack_size}')
		for i, (ptoken, token) in enumerate(zip(self.tokens, self.tokens[1:])):
			if token.gettokentype() in BSS:
				self.bss.append(f'{token.getstr()[1:]}: resd 1')
			elif token.gettokentype() == 'STATARR':
				if ptoken.gettokentype() not in CONSTVAL:
					const_error(ptoken)
				self.bss.append(f'{token.getstr()[1:]}: resd {ptoken.getstr()}')
				self.ban |= {i, i + 1}

	def set_text(self, iter_cur_label=None, iter_end_label=None):
		while self.ptr < len(self.tokens):
			token = self.tokens[self.ptr]
			if self.ptr in self.ban or token.gettokentype() == 'COMMENT':
				self.ptr += 1
			elif token.gettokentype() == 'END':
				self.ptr += 1
				return
			elif token.gettokentype() in COND:
				yield ('@cmp0' if token.gettokentype()[-1] == '0' else '@cmp')
				cur_label = self.get_label()
				end_label = self.get_label()
				yield f'{str().join(filter(str.isalpha, token.gettokentype())).lower()} {cur_label}'
				self.ptr += 1
				lines = list(self.set_text(iter_cur_label, iter_end_label))
				if self.ptr < len(self.tokens) and self.tokens[self.ptr].gettokentype() == 'ELSE':
					self.ptr += 1
					for line in self.set_text(iter_cur_label, iter_end_label):
						yield line
				yield f'jmp {end_label}'
				yield f'{cur_label}:'
				for line in lines:
					yield line
				yield f'{end_label}:'
			elif token.gettokentype() == 'ITER':
				cur_label = self.get_label()
				end_label = self.get_label()
				yield f'{cur_label}:'
				self.ptr += 1
				for line in self.set_text(cur_label, end_label):
					yield line
				yield f'jmp {cur_label}'
				yield f'{end_label}:'
			elif token.gettokentype() == 'HALT':
				yield f'jmp {iter_end_label}'
				self.ptr += 1
			elif token.gettokentype() == 'JUMP':
				yield f'jmp {iter_cur_label}'
				self.ptr += 1
			elif token.gettokentype() == 'SETLVAR':
				yield f'@setlvar {token.getstr()[1:]}'
				self.local.append(token.getstr()[1:])
				self.ptr += 1
			elif token.gettokentype() == 'SETFUNC':
				yield f'%macro @{token.getstr()[1:]} 0'
				self.ptr += 1
				for line in self.set_text(iter_cur_label, iter_end_label):
					yield line
				yield f'%endmacro'
			elif token.gettokentype() == 'BACK':
				yield RETSTATEMENT
				self.ptr += 1
			elif token.gettokentype() == 'SETSUNC':
				# IT'S ALL BROKEN
				self.sunc.append(f'@{token.getstr()[1:]}:')
				self.sunc.append('@meminit')
				self.local.clear()
				self.ptr += 1
				lines = list(self.set_text(iter_cur_label, iter_end_label)) + [RETSTATEMENT]
				self.local = list(set(self.local))
				for lvar in self.local:
					self.sunc.append(f'@memgetvar {lvar}')
					self.bss.append(f'{lvar}: resd 1')
				for line in lines:
					if line == RETSTATEMENT:
						for lvar in reversed(self.local):
							self.sunc.append(f'@memsetvar {lvar}')
						self.sunc.append('@memexit')
					else:
						self.sunc.append(line)
			elif token.gettokentype() == 'SUNC':
				yield f'call @{token.getstr()[2:]}'
				self.ptr += 1
			elif token.gettokentype() == 'FUNC':
				yield f'@{token.getstr()[1:]}'
				self.ptr += 1
			elif token.gettokentype() in PARAM:
				value = str().join(filter(lambda x: x in VAR, token.getstr()))
				yield f'@{token.gettokentype().lower()} {value}'
				self.ptr += 1
			else:
				yield f'@{token.gettokentype().lower()}'
				self.ptr += 1


if __name__ == '__main__':
	Main()
