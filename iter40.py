#!venv/bin/python
from click import command, argument, File, option, Path
from lexer import lexer, LexingError
from pprint import pprint
from errors import *
from token_types import *
from os import system


@command(help='ITER compiler made by Gornak40.')
@argument('source', type=File())
@option('--outname', '-o', default='main', type=Path(writable=True, dir_okay=False), help='Output file name.')
class Main:
	tokens = list()
	assign = list()
	bss = list()
	text = list()
	ptr = 0
	label = 0
	ban = set()

	def get_label(self):
		self.label += 1
		return f'@{self.label - 1}'

	def __init__(self, source, outname):
		self.lex(source)
		self.check_balance()
		self.set_include()
		self.set_assign()
		self.set_bss()
		self.text = list(self.set_text())
		pprint(self.tokens)
		self.build(outname)

	def build(self, outname):
		with open(f'{outname}.asm', 'w') as fout:
			print(*self.assign, sep='\n', file=fout)
			print('section .bss', file=fout)
			print(*self.bss, sep='\n', file=fout)
			with open('iter.asm') as fin:
				print(fin.read(), file=fout)
			print('main:', file=fout)
			print('@start', file=fout)
			print(*self.text, sep='\n', file=fout)
			print('@exit', file=fout)
		system(f'nasm -f elf32 {outname}.asm -o {outname}.o && gcc -m32 {outname}.o -o {outname}')


	def lex(self, source):
		for token in source.read().split():
			try:
				self.tokens.append(*lexer.lex(token))
			except LexingError:
				syntax_error(token)

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

	# TODO
	def set_include(self):
		pass

	def set_assign(self):
		for i, (ptoken, token) in enumerate(zip(self.tokens, self.tokens[1:])):
			if token.gettokentype() == 'SETCONST':
				if ptoken.gettokentype() not in CONSTVAL:
					const_error(ptoken)
				self.assign.append(f'%assign {token.getstr()[1:]} {ptoken.getstr()}')
				self.ban |= {i, i + 1}

	def set_bss(self):
		for i, (ptoken, token) in enumerate(zip(self.tokens, self.tokens[1:])):
			if token.gettokentype() in BSS:
				self.bss.append(f'{token.getstr()[1:]}: resd 1')
			elif token.gettokentype() == 'STATARR':
				if ptoken.gettokentype() not in CONSTVAL:
					const_error(ptoken)
				self.bss.append(f'{token.getstr()[1:]}: resd {ptoken.getstr()}')
				self.ban |= {i, i + 1}
		self.bss = list(set(self.bss))

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
			elif token.gettokentype() == 'SETFUNC':
				yield f'%macro @{token.getstr()[1:]} 0'
				self.ptr += 1
				for line in self.set_text(iter_cur_label, iter_end_label):
					yield line
				yield f'%endmacro'
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
