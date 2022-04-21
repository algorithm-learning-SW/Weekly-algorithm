'''
import math
import numpy as np

def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

def fillDic(n):
    facDic[n]=factorial(n)
    return

def garoNum(n):
    return math.floor(n/2)

def fillNum(n, g):
    #Combination(n-g, g)
    temp=1
    for i in range(n, n-g, -1):
        temp=temp*i
    for j in range(1,g+1):
        temp=temp//j
    return temp

def solution(n):
    answer=0
    garo=garoNum(n)
    combMatrix=np.zeros((n+1,garo+1), dtype=int)
    for p in range(garo+1):
        combMatrix[n-p][p]=fillNum(n-p,p)
    #for i in range(garo):
        #answer+=combMatrix[n][i]
    answer=int(combMatrix.sum())
    return answer%1000000007

print(solution(500))

'''

def sum(n1, n2):
    return (n1+n2)%1000000007

def solution(n):
    temp1=0
    temp2=1
    
    for i in range(n):
        temp1, temp2 = temp1+temp2, temp1
    temp1, temp2 = temp1+temp2, temp1  
    return temp1

print(solution(10))
