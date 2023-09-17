import random

def bubbleSort(A):
    change = True
    while change == True:
        change = False
        for i in range(0,len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                change = True
def shakerSort(A):
    change = True
    while change == True:
        change = False
        for i in range(0,len(A)-1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
                change = True
        # for i in range(len(A)-1, 0, -1):
        #     if A[i] < A[i-1]:
        #         A[i], A[i-1] = A[i-1], A[i]
        #         print(A)
        #         change = True
        for i in range(len(A)-2, -1, -1):
                if A[i] > A[i+1]:
                    A[i], A[i+1] = A[i+1], A[i]
                    change = True
def countingSort(A):
    F=[0]*len(A)
    for v in A:
        F[v]+=1
    k=0
    for i in range(len(F)):
        v=i
        count=F[i]
        
        for j in range(count):
            A[k]=v
            k+=1
def UniqueRandList(num):
    lst=[]
    while len(lst)<num:
        for i in range(num):
            r = random.randrange(0,num)
            if r not in lst:
                lst.append(r)
    return(lst)

def RandList(num):
    lst=[]
    for i in range(num):
        lst.append(random.randrange(0,num))
    return(lst)

def main():
    #check bubble sort
    A = UniqueRandList(7)
    B = A[0:len(A)]
    B.sort()
    bubbleSort(A)
    if A != B:
        print('error')
    #check shaker sort
    C = UniqueRandList(7)
    D= C[0:len(C)]
    shakerSort(C)
    D.sort()
    if C != D:
        print('error')
    #check counting sort
    E=RandList(7)
    F=E[0:len(E)]
    countingSort(E)

    F.sort()
    if E != F:
        print('error')
    
main()