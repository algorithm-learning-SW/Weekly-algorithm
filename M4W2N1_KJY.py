import math

def solution(n,a,b):
    answer = 1
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    print('Hello Python')
    while abs(a-b)!=1:
        print(abs(a-b))
        if a%2==1:
            a=int(math.floor(a/2)+1)
        else:
            a=a/2
        if b%2==1:
            b=int(math.floor(b/2)+1)
        else:
            b=b/2
        answer=answer+1
        
    return answer

print(solution(8,4,7))
