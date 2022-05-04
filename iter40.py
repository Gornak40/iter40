#!venv/bin/python
from click import command, argument, File
from lexer import lexer
from pprint import pprint


@command(help='ITER40 compiler made by Gornak40.')
@argument('source', type=File())
class Main:
	tokens = []

	def __init__(self, source):
		for token in source.read().split():
			self.tokens.append(*lexer.lex(token))
		pprint(self.tokens)


if __name__ == '__main__':
	Main()
