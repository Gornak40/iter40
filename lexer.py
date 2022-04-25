from rply import LexerGenerator

vartemp = r'[a-zA-Z\d_]+'

lg = LexerGenerator()

lg.add('READ', r'^\\read$')
lg.add('COPY', r'^\\copy$')
lg.add('PUSH', r'^\\push$')
lg.add('SWAP', r'^\\swap$')
lg.add('DROP', r'^\\drop$')
lg.add('POST', r'^\\post$')
lg.add('ITER', r'^\\iter$')
lg.add('HALT', r'^\\halt$')
lg.add('ELSE', r'^\\else$')
lg.add('FUNC', rf'^\\{vartemp}$')

lg.add('NUM', r'^\-?\d+$')

lg.add('SETVAR', rf'^\={vartemp}$')
lg.add('GETVAR', rf'{vartemp}$')

lg.add('GETARR', rf'^\[\]{vartemp}$')
lg.add('SETARR', r'^\{\}' + vartemp + r'$')
lg.add('HEAPARR', rf'^\${vartemp}$')
lg.add('STATARR', rf'^\@{vartemp}$')

lg.add('SEMI', r'^\;$')
lg.add('TRASH', r'.')

lg.ignore(r'\s')
lexer = lg.build()
