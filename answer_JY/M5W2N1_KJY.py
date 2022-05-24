import numpy as np
'''
read following this direction : <-
-------------------start----------------------
990 991 992 993 994 995 996 997 998  9  999 99
980 981 982 983 984 985 986 987 988 NaN 989 98
970 971 972 973 974 975 976 977 978 NaN 979 97
...
900 901 902 903 904 905 906 907 908 NaN 909 90

890 891 892 893 894 895 896 897   898 89 899
880 881 882 883 884 885 886 887 8 888 88 889
870 871 872 873 874 875 876 877   87 878 879
...
130  NaN 131 13 132 133 134 135 136 137 138 139
120  NaN 121 12 122 123 124 125 126 127 128 129
110   1  111 11 112 113 114 115 116 117 118 119
100  NaN 10 101 102 103 104 105 106 107 108 109
0
-----------------------end-------------------
90 * 12 + 1 = 1081 total entry
number of empty entry : 8*10 = 80
'''
def swap(mat, m1, n1, m2, n2):
    tempVal=mat[m1][n1]
    mat[m1][n1]=mat[m2][n2]
    mat[m2][n2]=tempVal
    
    return

def hundredMatrix(n):
    temp=np.zeros((10, 12))
    temp[:,n]=np.NaN
    temp[n][n]=n
    for i in range(10):
        for j in range(11, n+2, -1):
            #while temp[i][j]!=np.NaN and temp[i][j]==0:
            temp[i][j]=n * 100 + i * 10 + j-2
        temp[i,n+2]=10 * n + i
        temp[i,n+1]=n * 100 + i * 10 + n
        for m in range(n-1, -1, -1):
            temp[i][m]=n * 100 + i * 10 + m
    for p in range(n+1):
        swap(temp, p, n+1, p, n+2)
    temp[temp==0]=np.NaN
    temp=np.flip(temp)
    print(temp)
    return temp

#print(hundredMatrix(9))
#print(hundredMatrix(8))

def solution(numbers):
    hundredMatrices=np.zeros((9,10,12))
    for i in range(9, 0, -1):
        hundredMatrices[9-i]=(hundredMatrix(i))
    #print(hundredMatrices)
    hundredMatrices[8][9][10]=100
    hundredMatrices[8][9][11]=1000
    #print(hundredMatrices)
    finalArray=hundredMatrices.flatten()
    finalArray=np.concatenate((finalArray, np.array([0])))
    finalArray=finalArray.astype(int)
    print(len(finalArray))

    timesArray=np.zeros((1081))
    finalArray=finalArray.tolist()
    for num in numbers:
        idx=finalArray.index(num)
        timesArray[idx]=timesArray[idx]+1
    timesArray=timesArray.astype(int)
    #print(timesArray)
    arr=[]
    for t in range(1081):
        arr.append(str(finalArray[t])*int(timesArray[t]))
    if sum(numbers)==0:
        return "0"
    return "".join(arr)
print(solution([6,2,10,9,9,9,0,998]))
print(solution([101,10,232,23]))

