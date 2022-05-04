from rply import LexerGenerator

vartemp = r'[a-zA-Z\d_]+'

tokens = {
	'READ': r'\\read',
	'COPY': r'\\copy',
	'PUSH': r'\\push',
	'SWAP': r'\\swap',
	'DROP': r'\\drop',
	'POST': r'\\post',
	'ITER': r'\\iter',
	'HALT': r'\\halt',
	'ELSE': r'\\else',
	'FUNC': rf'\\{vartemp}',

	'SEMI': r';',
	'SETFUNC': rf'#{vartemp}',

	'NUM': r'-?\d+',
	'GETVAR': rf'{vartemp}',
	'SETVAR': rf'={vartemp}',
	'SETCONST': rf':{vartemp}',

	'GETARR': rf'\[\]{vartemp}',
	'SETARR': r'\{\}' + vartemp,
	'HEAPARR': rf'\${vartemp}',
	'STATARR': rf'@{vartemp}',

	'INC': r'\+\+',
	'DEC': r'\-\-',
	'NOT': r'~',

	'ADD': r'\+',
	'SUB': r'-',
	'MUL': r'\*',
	'DIV': r'/',
	'MOD': r'%',
	'XOR': r'\^',
	'OR': r'\|',
	'AND': r'&',
	'SHL': r'<<',
	'SHR': r'>>',

	'MULDIV': r'\*/',
	'MULMOD': r'\*%',

	'JNE0': r'\?',
	'JE0': r'!',

	'JL': r'<',
	'JLE': r'<=',
	'JG': r'>',
	'JGE': r'>=',
	'JE': r'==',
	'JNE': r'!=',
}

lg = LexerGenerator()
lg.ignore(r'\s')

for name, reg in tokens.items():
	lg.add(name, rf'^{reg}$')

lexer = lg.build()
