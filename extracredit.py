import random
import time

#make for loop to 50 and set as key values?
answerKey = { '1':1,'4':4,'8':8,'2':2,'16':16,'32':32,'64':64,'128':128,'256':256,'512':512,
            '1k':1024,'2k':2048,'4k':4096,'8k':8192,'16k':16384,'32k':32768,'64k':65536, '128k':131072,'256k':262144,'512k':524288,
            '1m':1048576,'2m':2097152,'4m':4194304,'8m':8388608,'16m':16777216,'32m':33554432,'64m':67108864,'128m':134217728,'256m':268435456,'512m':536870912,
            '1b':1073741824,'2b':2147483648,'4b':4294967296,'8b':8589934592,'16b':17179869184,'32b':34359738368,'64b':68719476736,'128b':137438953472,'256b':274877906944,'512b':549755813888,
            '1t':1099511627776,'2t':2199023255552,'4t':4398046511104,'8t':8796093022208,'16t':17592186044416,'32t':35184372088832,'64t':70368744177664,'128t':140737488355328,'256t':281474976710656,'512t':562949953421312}
def exponents():
    A=[]
    while len(A)<50:
        for i in range(50):
            r = random.randrange(0,50)
            if r not in A:
                A.append(r)
    return A
    #creates a unique list of 50 random numbers

def quiz():
    lst = exponents()
    time1 = time.time()
    #starts timer

    while len(lst) > 0:
        #runs until the list is finished
        randexp = lst[0]
        # gets the first exponent from the list
        correct = int(2**randexp)
        print(lst)
        print(correct)
        answer = (input(f"What is 2 ** {randexp}? "))

        pair = answerKey.get(answer)
        #pair is the exact int value of the answer

        # if pair == correct:
        #     lst.pop(0)
        #     #removes the 1st random number in the list
        #     print(lst)
        # else:
        while pair != correct:
            answer = input(f"Try again: ")
            pair = answerKey.get(answer)
        
        lst.pop(0)
    
    time2=time.time()
    #stop timer
    quizTime = round(time2-time1, 2)
    #calculate the time diffference from start(time1) to finish(time2)
    print(f"*\n*\n*\nYour total time was {quizTime} seconds.")
        
quiz()


