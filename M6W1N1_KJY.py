import math
def subAnswer(w1,h1):
    answer=h1
    for i in range(1, w1):
        if (h1/w1)*i!=math.floor((h1/w1)*i):
            answer+=1
    return answer
def solution(w,h):
    if w==h:
        return w*w-w
    if h==1:
        return 0
    if w==1:
        return 0
    if w>h:
        #swap
        temp=w
        w=h
        h=temp
    gcd=math.gcd(w, h)
    return w*h-subAnswer(int(w/gcd),int(h/gcd))*gcd

print(solution(8, 12))
