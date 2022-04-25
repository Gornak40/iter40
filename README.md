# ITER40
*Better version of legendary ITER language.*

### Everything
- ```<number>``` - push(number)
- ```<variable>``` - push(variable)
- ```<constant>``` - push(constant)
- ```[]<array>``` - push(array[pop_1])
- ```+, -, *, /, %, ^, &, |, <<, >>``` - push(pop_2 ** pop_1)
- ```++, --, ~``` - push(pop_1 operation)
- ```\copy``` - push(top_1)
- ```\prev``` - push(top_2)
- ```\push```
- ```\swap``` - swap(top_1, top_2)
- ```\drop``` - pop_1
- ```=<variable>``` - variable = pop_1
- ```:<constant>``` - define constant pop_1
- ```{}<array>```
- ```$<array>``` - assign heap array\[pop_1\]
- ```@<array>``` - assign static array\[pop_1\]
- ```#<function> <commands> ;``` - define function
- ```..<module>``` - include module
- ```\iter <commands> ;``` - while true
- ```<, <=, >, >=, ==, !=, !, ? <commands> ;``` - if pop_2 ** pop_1
- ```\else <commands> ;``` - else
