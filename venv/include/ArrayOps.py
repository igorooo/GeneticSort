from random import randint


def ar_array_gen(i_LENGTH):
    ar_ARRAY = []

    for i in range(0, i_LENGTH):
        ar_ARRAY.append(randint(0, 10000))

    return ar_ARRAY

def i_check_array_fitness(ARRAY):
    i_ARR_LEN = len(ARRAY)
    i_NUM_OF_CHANGES = 0

    b_FLAG = None
    ar_NARR = ARRAY[:]

    while (b_FLAG == None):
        b_FLAG = True
        for i_IX in range(0, i_ARR_LEN-1):
            if( ar_NARR[i_IX] > ar_NARR[i_IX+1] ):
                ar_NARR[i_IX], ar_NARR[i_IX+1] = ar_NARR[i_IX+1], ar_NARR[i_IX]
                i_NUM_OF_CHANGES += 1
                b_FLAG = None
    return (i_ARR_LEN**2) - i_NUM_OF_CHANGES    

