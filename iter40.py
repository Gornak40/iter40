#!venv/bin/python
from click import command, argument, File
from lexer import lexer


@command(help='ITER40 compiler made by Gornak40.')
@argument('source', type=File())
def main(source):
	for token in source.read().split():
		print(*lexer.lex(token))


if __name__ == '__main__':
	main()
