#!venv/bin/python
from click import command, argument, File, option, Path
from lexer import lexer, LexingError
from pprint import pprint
from errors import *
from token_types import *
from os import system


@command(help='ITER40 compiler made by Gornak40.')
@argument('source', type=File())
@option('--outname', '-o', default='main', type=Path(writable=True, dir_okay=False), help='Output file name.')
class Main:
	tokens = []
	assign = []
	bss = []
	text = []

	def __init__(self, source, outname):
		self.lex(source)
		self.check_balance()
		self.set_assign()
		self.set_bss()

		self.build(outname)

	def build(self, outname):
		with open(f'{outname}.asm', 'w') as fout:
			print(*self.assign, sep='\n', file=fout)
			print('section .bss', file=fout)
			print(*self.bss, sep='\n', file=fout)
			with open('iter.asm') as fin:
				print(fin.read(), file=fout)
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

	def set_assign(self):
		for ptoken, token in zip(self.tokens, self.tokens[1:]):
			if token.gettokentype() == 'SETCONST':
				if ptoken.gettokentype() not in CONSTVAL:
					const_error(ptoken)
				self.assign.append(f'%assign {token.getstr()[1:]} {ptoken.getstr()}')
				ptoken = token = None

	def set_bss(self):
		for ptoken, token in zip(self.tokens, self.tokens[1:]):
			if token.gettokentype() in BSS:
				self.bss.append(f'{token.getstr()[1:]}: resd 1')
			elif token.gettokentype() == 'STATARR':
				if ptoken.gettokentype() not in CONSTVAL:
					const_error(ptoken)
				self.bss.append(f'{token.getstr()[1:]}: resd {ptoken.getstr()}')
				ptoken = token = None
		self.bss = list(set(self.bss))


if __name__ == '__main__':
	Main()
