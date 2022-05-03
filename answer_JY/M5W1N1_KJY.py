import numpy

clothesDic={}
def solution(clothes):
    for subList in clothes:
        clothesDic[subList[0]]=subList[1]
    categoryList=list(clothesDic.values())
    categoryNumList=[0]*len(categoryList)
    for key,value in clothesDic.items():
        categoryNumList[categoryList.index(value)]+=1
    numList=[x+1 for x in categoryNumList]
    return int(numpy.prod(numList))-1
