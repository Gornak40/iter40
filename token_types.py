from string import ascii_letters, digits


VAR = set(ascii_letters) | set(digits) | {'_', '-'}
COND = {'JNE0', 'JE0', 'JL', 'JLE', 'JG', 'JGE', 'JE', 'JNE'}
OPEN = COND | {'ELSE', 'ITER', 'SETFUNC', 'SETSUNC', 'SETCAPSULE'}
CONSTVAL = {'GETCONST', 'NUM'}
BSS = {'SETVAR', 'HEAPARR'}
PARAM = {'NUM', 'GETVAR', 'GETCONST', 'GETARR', 'SETVAR', 'LSETARR', 'RSETARR', 'HEAPARR'}
RETSTATEMENT = '__@retstatement'
# CAPSULE = {'GETVAR', 'GETARR', 'SETVAR', 'LSETARR', 'RSETARR', 'HEAPARR', 'STATARR'}
# SPLITCAPSULE = '_'