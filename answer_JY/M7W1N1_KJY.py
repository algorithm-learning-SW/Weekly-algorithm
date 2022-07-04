import numpy as np
def boardPos(n):
    if n==0:
        return 3,1
    row=(n-1)//3
    col=n%3-1
    return row, col
def distance(row1, col1, row2, col2):
    return np.abs(row1-row2)+np.abs(col1-col2)
def solution(numbers, hand):
    '''
    basedic={}
    basedic[1]="L"
    basedic[4]="L"
    basedic[7]="L"
    basedic[3]="R"
    basedic[6]="R"
    basedic[9]="R"
    '''
    keyboard=np.zeros((4,3))
    keyboard[3][0]=1
    keyboard[3][2]=2
    result=""
    for element in numbers:
        if element in [1,4,7]:
            result+="L"
            keyboard[keyboard==1]=0
            row, col=boardPos(element)
            keyboard[row][col]=1
        elif element in [3,6,9]:
            result+="R"
            keyboard[keyboard==2]=0
            row, col=boardPos(element)
            keyboard[row][col]=2
        else:
            #2580
            leftHandArray=np.where(keyboard==1, 1, 0)
            leftHandRow, leftHandCol=np.nonzero(leftHandArray)
            rightHandArray=np.where(keyboard==2, 1, 0)
            rightHandRow, rightHandCol=np.nonzero(rightHandArray)
            elementRow, elementCol=boardPos(element)
            leftDis=distance(elementRow, elementCol, leftHandRow, leftHandCol)
            rightDis=distance(elementRow, elementCol, rightHandRow, rightHandCol)
            print(leftDis)
            print(rightDis)
            if leftDis>rightDis:
                result+="R"
                keyboard[keyboard==2]=0
                keyboard[elementRow][elementCol]=2
            elif leftDis<rightDis:
                result+="L"
                keyboard[keyboard==1]=0
                keyboard[elementRow][elementCol]=1
            else:
                if hand=="left":
                    result+="L"
                    keyboard[keyboard==1]=0
                    keyboard[elementRow][elementCol]=1
                else:
                    result+="R"
                    keyboard[keyboard==2]=0
                    keyboard[elementRow][elementCol]=2
    return result
