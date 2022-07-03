def series(k):
    i=0
    SIGMA=0
    while i<k:
        SIGMA+=3**i
        i+=1
    return SIGMA

def digit3(k):
    if k//3==0:
        print("base")
        return str(k)
    else:
        print("recursive")
        return digit3(k//3)+str(k%3)

def conv(string):
    temp=list(string)
    for i in range(len(temp)):
        temp.append(str(int(temp[i])+1))
    result=temp[len(temp)//2:]
    return "".join(result)

def solution(n):
    i=0
    j=1 #digit
    while n>i:
        i=i+3**j
        j+=1
    answer = ''
    temp=n-series(j-1)
    print(temp)
    answer=digit3(temp)
    while len(answer)!=j-1:
          answer='0'+answer
    print("$$$$$$")
    print(answer)
    #answer=str(answer)
    answer=conv(answer)
    answer=answer.replace('3','4')
    return answer

print(solution(4))
print(solution(11))
