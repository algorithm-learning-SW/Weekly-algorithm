'''
def square(lst):
    result=[]
    for k in lst:
        result.append(k**2)
    return result

def solution(n, works):
    if sum(works)<n:
        return 0
    works.sort()
    works.reverse()
    for i in range(n):
        p=max(works)
        works.remove(p)
        works.append(p-1)
    answer=sum(square(works))    
    return answer
'''

import heapq
def solution(n, works):
    if sum(works)<n:
        return 0
    heap=[]
    for i in works:
        heapq.heappush(heap,(-i,i))
    for j in range(n):
        p=heapq.heappop(heap)[1]
        heapq.heappush(heap, (-p+1, p-1))
    result=0
    for element in heap:
        result+=(element[1]*element[1])
    return result
print(solution(4, [4,3,3]))
print(solution(1, [2,1,2]))
print(solution(3, [1,1]))
