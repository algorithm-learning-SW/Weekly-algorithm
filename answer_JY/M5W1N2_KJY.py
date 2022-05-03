'''
def weightedSum(x,y):
    return x + 2 * y

def mix(inputQueue):
    temp1=inputQueue.get()
    temp2=inputQueue.get()
    inputQueue.put(weightedSum(temp1, temp2))
    return inputQueue

def maxVal(inputList):
    returnList=[]
    for k in range(len(inputList)-1, -1, -1):
        returnList.append(inputList[k]*(2**k))
    return sum(returnList)

def solution(scoville, K):
    newQueue=queue.PriorityQueue()
    newList=[x for x in scoville if x<K]
    for i in newList:
        newQueue.put(i)
    num=0
    
    while True:
        if newQueue.qsize()<=1:
            break
        temp=newQueue.get()
        newQueue.put(temp)
        if temp>=K:
            break
        newQueue=mix(newQueue)
        num+=1
    if newQueue.get()>=K:
        return num
    else:
        return -1
'''
import queue
import heapq

def solution(scoville, K):
    #newQueue=queue.PriorityQueue()
    newHeapq=[x for x in scoville if x<K]
    #for i in newList:
    #    newQueue.put(i)
    heapq.heapify(newHeapq)
    num=0
    
    while newHeapq[0]<K:
        #if newQueue.qsize()<=1:
        #    break
        if len(newHeapq)<=1:
            return -1
        temp1=heapq.heappop(newHeapq)
        temp2=heapq.heappop(newHeapq)
        heapq.heappush(newHeapq,temp1+2*temp2)
        #newQueue=mix(newQueue)
        num+=1
    return num
print(solution([1,2,3,9,10,12],7))
