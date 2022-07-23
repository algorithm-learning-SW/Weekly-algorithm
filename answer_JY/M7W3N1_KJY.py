import numpy as np
def solution(answers):
    array1=[]
    array2=[]
    array3=[]
    for i in range(len(answers)):
        array1.append(i%5+1)
    temp=[2,1,2,3,2,4,2,5]
    for j in range(len(answers)):
        array2.append(temp[j%8])
    temparray=[3,3,1,1,2,2,4,4,5,5]
    for k in range(len(answers)):
        array3.append(temparray[k%10])
    '''
    filter1=np.array(array1)
    filter2=np.array(array2)
    filter3=np.array(array3)
    result1=filter1.size-np.count_nonzero(answers-filter1)
    result2=filter2.size-np.count_nonzero(answers-filter2)
    result3=filter3.size-np.count_nonzero(answers-filter3)
    '''

    result1=0
    result2=0
    result3=0
    for p in range(len(answers)):
        if array1[p]^(~answers[p])==-1:
            result1+=1
        if array2[p]^(~answers[p])==-1:
            result2+=1
        if array3[p]^(~answers[p])==-1:
            result3+=1
    result=max([result1, result2, result3])
    final=[]
    if result1==result:
        final.append(1)
    if result2==result:
        final.append(2)
    if result3==result:
        final.append(3)
    return final
