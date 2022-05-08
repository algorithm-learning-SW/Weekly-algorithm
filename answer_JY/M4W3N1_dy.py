arr={}

def arrange(n):
    if n in arr:
        return arr[n]
    else:    
        if n==0:
            arr[n]=0
        elif n==1:
            arr[n]=1
        elif n==2:
            arr[n]=2
        else:
            arr[n]=arrange(n-1)+arrange(n-2)
        return arr[n]

def solution(n):
    return arrange(n)%1000000007   

print(solution(6000))
