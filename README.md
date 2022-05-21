# ITER
*Better version of legendary ITER language.*

### Standard ITER40
- ```<number>``` - push(number)
- ```<variable>``` - push(variable)
- ```<constant>``` - push(constant)
- ```[].``` - push(\*pop_1)
- ```[]<array>``` - push(array\[pop_1\])
- ```\read``` - push(input)
- ```++, --, ~, *2, /2, ++., --.``` - push(pop_1, )
- ```+, -, *, /, %, ^, &, |, <<, >>, ->, <-``` - push(pop_2, pop_1)
- ```*/, *%``` - push(pop_3, pop_2, pop_1)
- ```\copy``` - push(top_1)
- ```\prev``` - push(top_2)
- ```\prew``` - push(top_3)
- ```\push``` - push(pop_1), push(pop_2), push(pop_1)
- ```\swap``` - swap(top_1, top_2)
- ```\drop``` - pop_1
- ```\post``` - print(pop_1)
- ```\mset``` - memset(pop_1, pop_2, pop_3 * sizeof(int))
- ```\mcpy``` - memcpy(pop_1, pop_2, pop_3 * sizeof(int))
- ```\bcnt``` - push(\_\_builtin_popcount(pop_1))
- ```\bclz``` - push(\_\_builtin_clz(pop_1))
- ```\bctz``` - push(\_\_builtin_ctz(pop_1))
- ```\dump``` - pop pop_2 values to \*pop_1
- ```\free``` - free(pop_1)
- ```=<variable>``` - variable = pop_1
- ```:<variable>``` - local variable = pop_1
- ```=<constant>``` - define constant pop_1
- ```{}.``` - \*pop_2 = pop_1
- ```.{}``` - \*pop_1 = pop_2
- ```{}<array>``` - array\[pop_2\] = pop_1
- ```<array>{}``` - array\[pop_1\] = pop_2
- ```<->``` - swap(\*pop_1, \*pop_2)
- ```$``` - assign and push heap array
- ```$<array>``` - assign heap array\[pop_1\]
- ```@<array>``` - assign static array\[pop_1\]
- ```#<function> <commands> \``` - declare function (same as define)
- ```.<sunction> <commands> \``` - declare sunction (same as function)
- ```\back``` - return
- ```,<module>``` - include module
- ``` `<comment>``` - comment
- ```\iter <commands> \``` - while true
- ```\halt``` - break
- ```\jump``` - continue
- ```<, <=, >, >=, ==, !=, !, ? <commands> \``` - if (pop_2, pop_1)
- ```\else <commands> \``` - else
- ```\<function>``` - function()
- ```()<sunction>``` - sunction()

### Algolymp

#### Func
- ```\min``` - a b
- ```\max``` - a b
- ```\lson``` - id
- ```\rson``` - id

#### Range
- ```()read_array``` - arr n
- ```()print_array``` - arr n
- ```()fill``` - arr n x
- ```()partial_sum``` - arr n ps
- ```()reverse``` - arr n
- ```()bubble_sort``` - arr n
- ```()merge``` - arr n brr n crr
- ```()merge_sort``` - arr n

#### Search
- ```()find``` - arr n x
- ```()lower_bound``` - arr n x
- ```()upper_bound``` - arr n x
- ```()count``` - arr n x
- ```()accumulate``` - arr n
- ```()min_element``` - arr n
- ```()max_element``` - arr n

#### Numeric
- ```()gcd``` - a b
- ```()pow_mod``` - a n mod
