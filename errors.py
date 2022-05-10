from termcolor import cprint


def syntax_error(token):
	cprint(f'[error] unknown token {token}', color='red')
	exit(0)


def balance_error():
	cprint(f'[error] balance is broken', color='red')
	exit(0)


def const_error(token):
	cprint(f'[error] {token} is not constant', color='red')
	exit(0)