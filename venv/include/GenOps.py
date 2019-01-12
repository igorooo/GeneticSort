from ArrayOps import *
from random import *

class GenObject(object):

    def __init__(self,ar_ARRAY):
        self.ar_ARRAY = ar_ARRAY[:]
        self.i_ARR_LEN = len(ar_ARRAY)
        self.ar_MOVES = []
        self.i_FITNESS = 0

    def __lt__(self, other):
        return self.i_FITNESS < other.i_FITNESS


    def create_randomly(self):
        for i in range(0,self.i_ARR_LEN):
            self.ar_MOVES.append( randint( 0 , self.i_ARR_LEN-1 ) )
        self.ar_RES_ARR = ar_ARRAY[:]
        self.implement_moves()
        self.i_FITNESS = i_check_array_fitness(self.ar_RES_ARR)

    def mutation(self):
        for ELEM in self.ar_MOVES:
            if (randint(0, 100) < 5):
                ELEM = randint( 0 , self.i_ARR_LEN-1 )

    def crossover(self,MOTHER,FATHER):
        RAND_1 = randint(0,self.i_ARR_LEN)
        RAND_2 = randint(0,self.i_ARR_LEN)
        
        SEP_A = min(RAND_1,RAND_2)
        SEP_B = max(RAND_1,RAND_2)
        
        for i in range(0, self.i_ARR_LEN):
            if(i < SEP_A):
                self.ar_MOVES[i] = MOTHER.ar_MOVES[i]
                continue
            if(i < SEP_B):
                self.ar_MOVES[i] = FATHER.ar_MOVES[i]
                continue
            else:
                self.ar_MOVES[i] = MOTHER.ar_MOVES[i]
        self.mutation()
        self.implement_moves()
        self.i_FITNESS = i_check_array_fitness(self.ar_RES_ARR)



    def implement_moves(self):
        #print("----")
        for i in range(0,self.i_ARR_LEN):
            TEMP = self.ar_RES_ARR[i]
            del self.ar_RES_ARR[i]
            self.ar_RES_ARR.insert(self.ar_MOVES[i] , TEMP)
           # print(self.ar_RES_ARR)
        #print("----")

    def introduce(self):
        print("Primary array:")
        print(self.ar_ARRAY)
        print("Moves:")
        print(self.ar_MOVES)
        print("Effect:")
        print(self.ar_RES_ARR)





class GenSort(object):

    def __init__(self,ar_ARRAY,i_POP_SIZE):
        self.ar_ARRAY = ar_ARRAY[:]
        self.i_POP_SIZE = i_POP_SIZE
        self.ar_FST_GEN = []
        self.ar_SND_GEN = []
        self.f_LOGS = open("logs.txt","w")
        self.f_LOGS.close()

        if(self.i_POP_SIZE % 2 == 1):
            self.i_POP_SIZE += 1


    def create_fst_gen(self):
        for i in range(0,self.i_POP_SIZE):
            TEMP = GenObject(self.ar_ARRAY)
            TEMP.create_randomly()
            self.ar_FST_GEN.append(TEMP)

    def get_parent(self):
        RANDOM_1 = self.ar_FST_GEN[randint(0, self.i_POP_SIZE)]
        RANDOM_2 = self.ar_FST_GEN[randint(0, self.i_POP_SIZE)]

        if( RANDOM_1 < RANDOM_2):
            return RANDOM_2
        else:
            return RANDOM_1

    def next_gen(self):
        for i in range(0, self.i_POP_SIZE/2):
            CHILD_A = GenObject(self.ar_ARRAY)
            CHILD_B = GenObject(self.ar_ARRAY)

            PARENT_A = self.get_parent()
            PARENT_B = self.get_parent()

            CHILD_A.crossover(PARENT_A,PARENT_B)
            CHILD_B.crossover(PARENT_B,PARENT_A)

            self.ar_FST_GEN.append( CHILD_A )
            self.ar_SND_GEN.append( CHILD_B )

        self.ar_FST_GEN = self.ar_SND_GEN



