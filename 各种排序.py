import time


def bubble_sort(ls):
    n=len(ls)
    for i in range(n):
        flag=False
        for j in range(n-1,i,-1):
            if ls[j-1]>ls[j]:
                ls[j-1],ls[j]=ls[j],ls[j-1]
                flag=True
        if not flag:
            return ls
    return ls



def select_sort(ls):
    n = len(ls)
    for i in range(n):
        pm=i
        for j in range(i+1,n):
            if ls[pm]>ls[j]:
                pm=j
        ls[i],ls[pm]=ls[pm],ls[i]
    return ls
    pass

def insert_sort(ls):
    n = len(ls)
    for i in range(1,n):
        if ls[i]<ls[i-1]:
            temp=ls[i]
            j=i-1
            while ls[j]>temp:
                ls[j+1]=ls[j]
                j-=1
            ls[j+1]=temp
            # temp=ls[i]
            # j=i-1
            # while ls[j]>temp:
            #     ls[j+1],ls[j]=ls[j],ls[j+1]
            #     j-=1

    return ls
def shell_sort(ls):
    n = len(ls)

    gap=n
    while True:

        gap=gap//3+1
        # print(gap)
        for i in range(gap, n):
            if ls[i] < ls[i - gap]:
                temp = ls[i]
                j = i - gap
                while ls[j] > temp and j>=0:
                    ls[j + gap] = ls[j]
                    j -= gap
                ls[j + gap] = temp
        if gap<=1:
            break
    return  ls


def quick_sort(ls):
    n=len(ls)
    low=0
    high=n-1
    qsort(ls,low,high)
    return ls
def qsort(ls,low,high):

    if low<high:
        pivot = partition(ls, low, high)
        qsort(ls, low, pivot - 1)
        qsort(ls, pivot + 1, high)
def partition(ls,low,high):
    pivotkey=ls[low]
    # i=low+1
    # j=high
    # while i<j:
    #     if ls[i]>pivotkey and ls[j]<pivotkey:
    #         ls[i],ls[j]=ls[j],ls[i]
    #         i+=1
    #         j-=1
    #     elif ls[i]>pivotkey:
    #         j-=1
    #     elif ls[j]<pivotkey:
    #         i+=1
    while low<high:
        while ls[high]>=pivotkey and low<high:
            high-=1
        ls[high],ls[low]=ls[low],ls[high]
        while ls[low]<=pivotkey and low<high:
            low+=1
        ls[high], ls[low] = ls[low], ls[high]

    return low



ls=[5,9,8,7,10,0,1,2,3,4,-1,6]
# print(bubble_sort(ls))
print(quick_sort(ls))

