import random
import sys
class Counter():
    def __init__(self):
        self.compares= 0
def UniqueRandList(num):
    lst=[]
    while len(lst)<num:
        for i in range(num):
            r = random.randrange(0,num)
            if r not in lst:
                lst.append(r)
    return(lst)
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
def MergeSort(A, c):
    L=A[0:len(A)//2]
    R=A[len(A)//2:len(A)]
    i=j=k=0
    if len(A) <= 1:
        return
    MergeSort(L)
    MergeSort(R)

    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1
        k+=1

    while i<len(L):
        A[k] = L[i]
        k+=1
        i+=1
    while j < len(R):
        A[k]= R[j]
        k+=1
        j+=1

    return(A)

def QuickSort(A, c, low, high):
    if high - low <= 0:
        return
    lmgt = low +1
    for i in range(low+1, high+1):
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt +=1
    pivotIndex = lmgt-1
    A[low], A[pivotIndex] = A[pivotIndex], A[low]
    QuickSort(A, low, pivotIndex-1)
    QuickSort(A, pivotIndex+1, high)

def ModQuickSort(A, low, high):
    if high - low <= 0:
        return
    mid = (low+high) //2
    A[low], A[mid] = A[mid], A[low]
    lmgt = low +1
    for i in range(low+1, high+1):
        if A[i] < A[low]:
            A[i], A[lmgt] = A[lmgt], A[i]
            lmgt +=1
    pivotIndex = lmgt-1
    A[low], A[pivotIndex] = A[pivotIndex], A[low]
    ModQuickSort(A, low, pivotIndex - 1)
    ModQuickSort(A, pivotIndex + 1, high)
A = UniqueRandList(13)


B = A[0:len(A)]
print(A)
MergeSort(B, 0, len(B)-1)
A.sort()
print(A, B)
