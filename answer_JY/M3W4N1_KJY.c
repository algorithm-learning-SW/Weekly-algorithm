#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int** answer = (int**)calloc(n, sizeof(int*));
    for(int i=1;i<(n+1);i++)
    {
        answer[i-1]=(int*)calloc(i,sizeof(int));
    }
    int p=1;
    int iterate=n;
    int rowIndex=0;
    int colIndex=0;
    
    while(p<(n*(n+1)/2+1)){   
        for(int k=0;k<iterate;k++)
        {
            answer[rowIndex][colIndex]=p;
            p++;
            rowIndex++;
        }
        
        if(iterate==0)
            break;
        iterate--;
        rowIndex--;
        colIndex++;
        //printArray(answer,n);
        
            
        for(int k=0;k<iterate;k++)
        {
            answer[rowIndex][colIndex]=p;
            p++;
            colIndex++;
        }
        
        if(iterate==0)
            break;
            
        iterate--;
        colIndex=colIndex-2;
        rowIndex--;
        //printArray(answer,n);
       
        for(int k=0;k<iterate;k++)
        {
            answer[rowIndex][colIndex]=p;
            p++;
            rowIndex--;
            colIndex--;
        }
        if(iterate==0)
            break;
        iterate--;
        rowIndex=rowIndex+2;
        colIndex++;
    }
    int* finalArray=(int *)calloc(n*(n+1)/2,sizeof(int*));
    int temp=0;
    for(int m=0;m<n;m++)
    {
        for(int q=0;q<(m+1);q++){
            *(finalArray+temp)=answer[m][q];
            temp++;
        }
    }
    return finalArray;
}