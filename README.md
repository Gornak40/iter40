# ITER
*Better version of legendary ITER language.*

### Standard ITER40
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
- ```\push``` - push(pop_1), push(pop_2), push(pop_1)
- ```\swap``` - swap(top_1, top_2)
- ```\drop``` - pop_1
- ```\post``` - print(pop_1)
- ```\mset``` - memset(pop_1, pop_2, pop_3 * sizeof(int))
- ```\mcpy``` - memcpy(pop_1, pop_2, pop_3 * sizeof(int))
- ```=<variable>``` - variable = pop_1
- ```:<variable>``` - local variable = pop_1
- ```=<constant>``` - define constant pop_1
- ```{}<array>``` - array\[pop_2\] = pop_1
- ```<array>{}``` - array\[pop_1\] = pop_2
- ```$<array>``` - assign heap array\[pop_1\]
- ```@<array>``` - assign static array\[pop_1\]
- ```#<function> <commands> \``` - declare function
- ```.<sunction> <commands> \``` - declare sunction
- ```\back``` - return
- ```,<module>``` - include module
- ``` `<comment>``` - comment
- ```\iter <commands> \``` - while true
- ```\halt``` - break
- ```\jump``` - continue
- ```<, <=, >, >=, ==, !=, !, ? <commands> \``` - if pop_2 ** pop_1
- ```\else <commands> \``` - else
- ```\<function>``` - function()
- ```()<sunction>``` - sunction()