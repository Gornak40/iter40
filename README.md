# ITER
*Better version of legendary ITER language.*

### Standard ITER40
- ```<number>``` - push(number)
- ```<variable>``` - push(variable)
- ```;<variable>``` - push(&variable)
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
- ```\push``` - push(pocket)
- ```\save``` - pocket = top_1
- ```\pick``` - pocket = pop_1
- ```\swap``` - swap(top_1, top_2)
- ```\drop``` - pop_1
- ```\kill``` - \\swap \\drop
- ```\post``` - print(pop_1)
- ```\mset``` - memset(pop_1, pop_2, pop_3 * sizeof(int))
- ```\mcpy``` - memcpy(pop_1, pop_2, pop_3 * sizeof(int))
- ```\bcnt``` - push(\_\_builtin_popcount(pop_1))
- ```\bclz``` - push(\_\_builtin_clz(pop_1))
- ```\bctz``` - push(\_\_builtin_ctz(pop_1))
- ```\dump``` - pop pop_2 values to \*pop_1
- ```\free``` - free(pop_1)
- ```\minc``` - \*pop_1++
- ```\mdec``` - \*pop_1--
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

### AVX2 extention
- ```\avx2_add``` - ymm0 = \_mm256_add_epi32(ymm0, pop_1)
- ```\avx2_sub``` - ymm0 = \_mm256_sub_epi32(ymm0, pop_1)
- ```\avx2_mul``` - ymm0 = \_mm256_mullo_epi32(ymm0, pop_1)
- ```\avx2_xor``` - ymm0 = \_mm256_xor_si256(ymm0, pop_1)
- ```\avx2_and``` - ymm0 = \_mm256_add_si256(ymm0, pop_1)
- ```\avx2_or``` - ymm0 = \_mm256_or_si256(ymm0, pop_1)
- ```\avx2_min``` - ymm0 = \_mm256_min_epi32(ymm0, pop_1)
- ```\avx2_max``` - ymm0 = \_mm256_max_epi32(ymm0, pop_1)
- ```\avx2_cmpeq``` - ymm0 = \_mm256_cmpeq_epi32(ymm0, pop_1)
- ```\avx2_cmpgt``` - ymm0 = \_mm256_cmpgt_epi32(ymm0, pop_1)
- ```\avx2_load``` - \_mm256_loadu_si256(ymm0, pop_1)
- ```\avx2_store``` - \_mm256_storeu_si256(pop_1, ymm0)
- ```\avx2_set1``` - ymm0 = \_mm256_set1_epi32(pop_1)

### Algolymp

#### Numeric
- ```\min``` - a b -> min
- ```\max``` - a b -> max
- ```\lson``` - id -> lson
- ```\rson``` - id -> rson
- ```\upper_2``` - a -> pow
- ```()gcd``` - a b -> gcd
- ```()pow_mod``` - a n mod -> res

#### Ranges
- ```()read_array``` - arr n ->
- ```()print_array``` - arr n ->
- ```()fill``` - arr n x ->
- ```()partial_sum``` - arr n ps ->
- ```()reverse``` - arr n ->
- ```()bubble_sort``` - arr n ->
- ```()merge``` - arr n brr n crr ->
- ```()merge_sort``` - arr n ->
- ```()unique``` - arr n -> new_n

#### Search
- ```()find``` - arr n x -> pos
- ```()lower_bound``` - arr n x -> pos
- ```()upper_bound``` - arr n x -> pos
- ```()count``` - arr n x -> cnt
- ```()accumulate``` - arr n -> sum
- ```()min_element``` - arr n -> min
- ```()max_element``` - arr n -> max

### Structures
- ```\trie_init``` - -> trie
- ```()trie_insert``` - trie x ->
- ```()trie_erase``` - trie x ->
- ```()trie_count``` - trie x -> cnt
