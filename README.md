# ITER40
*Better version of legendary ITER language.*

### Everything
- ```<number>``` - push(number)
- ```<variable>``` - push(variable)
- ```<constant>``` - push(constant)
- ```[]<array>``` - push(array[pop_1])
- ```\read``` - push(input)
- ```++, --, ~``` - push(pop_1 ^^)
- ```+, -, *, /, %, ^, &, |, <<, >>``` - push(pop_2 ^^ pop_1)
- ```*/, *%``` - push(pop_3 ^^ pop_2 ^^ pop_1)
- ```\copy``` - push(top_1)
- ```\prev``` - push(top_2)
- ```\push```
- ```\swap``` - swap(top_1, top_2)
- ```\drop``` - pop_1
- ```\post``` - print(pop_1)
- ```=<variable>``` - variable = pop_1
- ```:<constant>``` - define constant pop_1
- ```{}<array>``` - array\[pop_2\] = pop_1
- ```$<array>``` - assign heap array\[pop_1\]
- ```@<array>``` - assign static array\[pop_1\]
- ```#<function> <commands> ;``` - declare function
- ```..<module>``` - include module
- ```\iter <commands> ;``` - while true
- ```<, <=, >, >=, ==, !=, !, ? <commands> ;``` - if pop_2 ** pop_1
- ```\else <commands> ;``` - else
