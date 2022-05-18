from rply import LexerGenerator, Token
from rply.errors import LexingError

vartemp = r'[a-z\d_]+'
inctemp = r'[a-zA-Z\d\./]+'
consttemp = r'-?[A-Z]+'

tokens = {
	'READ': r'\\read',
	'COPY': r'\\copy',
	'PREV': r'\\prev',
	'PREW': r'\\prew',
	'PUSH': r'\\push',
	'SWAP': r'\\swap',
	'DROP': r'\\drop',
	'POST': r'\\post',
	'ITER': r'\\iter',
	'HALT': r'\\halt',
	'JUMP': r'\\jump',
	'ELSE': r'\\else',
	'BACK': r'\\back',
	'MSET': r'\\mset',
	'MCPY': r'\\mcpy',
	'PCNT': r'\\pcnt',
	'FUNC': rf'\\{vartemp}',
	'SUNC': rf'\(\){vartemp}',

	'END': r'\\',
	'SETFUNC': rf'#{vartemp}',
	'SETSUNC': rf'\.{vartemp}',
	'INCLUDE': rf',{inctemp}',
	'COMMENT': r'`.+',

	'NUM': r'-?\d+',
	'GETVAR': rf'{vartemp}',
	'GETCONST': rf'{consttemp}',
	'SETVAR': rf'={vartemp}',
	'SETLVAR': rf':{vartemp}',
	'SETCONST': rf'={consttemp}',

	'GETPTR': r'\[\]\.',
	'LSETPTR': r'\{\}\.',
	'RSETPTR': r'\.\{\}',
	'GETARR': rf'\[\]{vartemp}',
	'LSETARR': r'\{\}' + vartemp,
	'RSETARR': vartemp + r'\{\}',
	'HEAPARR': rf'\${vartemp}',
	'STATARR': rf'@{vartemp}',

	'INC': r'\+\+',
	'DEC': r'--',
	'NOT': r'~',
	'MUL2': r'\*2',
	'DIV2': r'/2',

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
	'RARROW': r'->',
	'LARROW': r'<-',

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
