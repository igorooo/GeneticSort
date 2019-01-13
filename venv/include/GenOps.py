from ArrayOps import *
from random import *

class GenObject(object):

    def __init__(self,ar_ARRAY):
        self.ar_ARRAY = ar_ARRAY[:]
        self.i_ARR_LEN = len(ar_ARRAY)
        self.ar_MOVES = []
        self.i_FITNESS = 0
        self.ar_RES_ARR = ar_ARRAY[:]

    def __lt__(self, other):
        return self.i_FITNESS < other.i_FITNESS


    def create_randomly(self):
        for i in range(0,self.i_ARR_LEN):
            self.ar_MOVES.append( randint( 0 , self.i_ARR_LEN-1 ) )
        self.ar_RES_ARR = self.ar_ARRAY[:]
        self.implement_moves()
        self.i_FITNESS = i_check_array_fitness(self.ar_RES_ARR)

    def mutation(self):
        for i in range(0, len(self.ar_MOVES)):
            if (randint(0, 100) < 5):
                self.ar_MOVES[i] = randint( 0 , self.i_ARR_LEN-1 )


    def crossover(self,MOTHER,FATHER):
        RAND_1 = randint(0,self.i_ARR_LEN-1)
        RAND_2 = randint(0,self.i_ARR_LEN-1)
        
        #SEP_A = min(RAND_1,RAND_2)
        #SEP_B = max(RAND_1,RAND_2)

        SEP_A = RAND_1


        for i in range(0, SEP_A):
            self.ar_MOVES.append(MOTHER.ar_MOVES[i])
        for i in range(SEP_A, self.i_ARR_LEN):
            self.ar_MOVES.append(FATHER.ar_MOVES[i])

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
        self.i_NO_GEN = 0

        if(self.i_POP_SIZE % 2 == 1):
            self.i_POP_SIZE += 1


    def create_fst_gen(self):
        for i in range(0,self.i_POP_SIZE):
            TEMP = GenObject(self.ar_ARRAY)
            TEMP.create_randomly()
            self.ar_FST_GEN.append(TEMP)
        self.save_logs_from_fstgen()

    def get_parent(self):
        RANDOM_1 = self.ar_FST_GEN[randint(0, self.i_POP_SIZE-1)]
        RANDOM_2 = self.ar_FST_GEN[randint(0, self.i_POP_SIZE-1)]

        if( RANDOM_1 < RANDOM_2):
            return RANDOM_2
        else:
            return RANDOM_1

    def next_gen(self):
        self.ar_SND_GEN = []
        for i in range(0, int(self.i_POP_SIZE/2)):
            CHILD_A = GenObject(self.ar_ARRAY)
            CHILD_B = GenObject(self.ar_ARRAY)

            PARENT_A = self.get_parent()
            PARENT_B = self.get_parent()

            CHILD_A.crossover(PARENT_A,PARENT_B)
            CHILD_B.crossover(PARENT_B,PARENT_A)

            self.ar_SND_GEN.append( CHILD_A )
            self.ar_SND_GEN.append( CHILD_B )

        self.ar_FST_GEN = []
        self.ar_FST_GEN = self.ar_SND_GEN[:]
        self.save_logs_from_fstgen()


    def save_logs_from_fstgen(self):
        # saving generation in logs.txt file
        self.f_LOGS = open("logs.txt","a")
        for ELEM in self.ar_FST_GEN:
            self.f_LOGS.write("{")
            for i in range(0,len(ELEM.ar_RES_ARR)):
                self.f_LOGS.write(str(ELEM.ar_RES_ARR[i]))
                self.f_LOGS.write(" ")
            self.f_LOGS.write("}")
            self.f_LOGS.write("(")
            for i in range(0,len(ELEM.ar_MOVES)):
                self.f_LOGS.write(str(ELEM.ar_MOVES[i]))
                self.f_LOGS.write(" ")
            self.f_LOGS.write(")")
            self.f_LOGS.write("[")
            self.f_LOGS.write(str(ELEM.i_FITNESS))
            self.f_LOGS.write("]")
            self.f_LOGS.write(" ")
        self.f_LOGS.write("\n")
        self.f_LOGS.close()





