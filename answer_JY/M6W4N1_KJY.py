import numpy as np
def solution(nums):
    maxRow=max(nums)
    numSelect=len(nums)//2
    tempList=[0]*(maxRow+1)
    for num in nums:
        tempList[num]+=1
    tempArray=np.array(tempList)
    nonzero_num=np.count_nonzero(tempArray)
    if nonzero_num<numSelect:
        return nonzero_num
    else:
        return numSelect
    '''
    maxCol=max(tempList)
    baseArray=np.array([0]*maxCol)
    for i in range(maxRow+1):
        tempArray=np.array(([i+1]*tempList[i])+[0]*(maxCol-tempList[i]))
        baseArray=np.vstack((baseArray, tempArray))
    zeroCol=baseArray[:,0]
    length=np.count_nonzero(zeroCol)
    if numSelect<=length:
        return numSelect
    else:
        return length
    '''
