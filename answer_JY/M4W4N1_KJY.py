#convert input string to list of lists
def str2list(inputStr):
    among_set=False
    return_list=[]
    list_list=[]
    eachElement=""
    for element in inputStr:
        if element=='{':
            among_set=True
            eachElement=''
        elif element=='}':
            among_set=False
            return_list.append(int(eachElement))
            list_list.append(return_list)
            return_list=[]
        #if element is a number or ,
        else:
            
            #print("zzz")
            if among_set==True:
                if element==',':
                    return_list.append(int(eachElement))
                    eachElement=""
                    continue
                else:
                    eachElement+=element
            #else:
            #    list_list.append(return_list)
            #    return_list=[]
            #print(return_list)
    #list_list.append(return_list)
    list_list.pop(-1)
    print(list_list)
    return list_list
                
def listMinus(list1, list2):
    for element in list2:
        if element in list1:
            continue
        else:
            return element
#key : length
#value : set in input s of length key
setDic={}

def solution(s):
    lists_list=str2list(s)

    for eachList in lists_list:
        setDic[len(eachList)]=eachList
        
    sortedList=[]
    for i in range(len(lists_list)):
        sortedList.append(setDic[i+1])

    print(sortedList)
    finalList=[]
    finalList.append(sortedList[0][0])
    for index in range(len(lists_list)-1):
        print("///")
        #print(listMinus(sortedList[index], sortedList[index+1]))
        print("aksld")
        finalList.append(listMinus(sortedList[index], sortedList[index+1]))
        print(finalList)
    return finalList

inputStr1="{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(inputStr1))
inputStr2="{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(inputStr2))
inputStr3="{{123}}"
print(solution(inputStr3))
