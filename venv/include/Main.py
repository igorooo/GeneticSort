from ArrayOps import *
from GenOps import *


#ARR = ar_array_gen(10)

ARR = [5,4,2,1,10,9,8,3,7,6]

#for c in ARR:
 #   print(c)

VAL = i_check_array_fitness(ARR)


GSORT = GenSort(ARR,10)

GSORT.create_fst_gen()

for i in range(0,10000):
    GSORT.next_gen()





