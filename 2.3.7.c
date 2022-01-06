#include <stdio.h>
#include "array_oper.h"
#include "decompose.h"
int main(int argc, char const *argv[])
{
	int num[8]={2,1,9,9,7,8,10,1};
	int length=sizeof(num)/sizeof(int);
	print_int(num,length);
	decompose(num,0,7);
	print_int(num,8);
	int *res=(int *)malloc(length*sizeof(int));
	int index=duplicate_removal(num,8,res);
	print_int(res,length);
	int *target=(int *)malloc(index*sizeof(int));
	array_copy(res,0,index,target);
	int targetLength=index+1;
	print_int(target,targetLength);
	int x;
	scanf("%d",&x);
	printf("%d\n", x);
	int *divide=(int *)malloc(targetLength*sizeof(int));
	int i = 0;
	for (; i <= index; ++i)
	{
		divide[i]=x-target[i];
	}
	print_int(divide,targetLength);
	decompose(divide,0,index);
	print_int(divide,targetLength);
	
	int * numend=(int *)malloc(targetLength*2*sizeof(int));
	array_uinon(target,0,index,divide,0,index,numend);
	print_int(numend,targetLength*2);
	decompose(numend,0,targetLength*2-1);
	print_int(numend,targetLength*2);
	i=1;
	int key=0;
	for (; i <= targetLength*2-1; ++i)
	{
		if (numend[i]==numend[i-1])
		{
			key=numend[i];
		}
		
	}
	printf(" %d and %d equal %d\n",key,x-key,x);
	free(res);
	free(target);
	free(divide);
	free(numend);
	return 0;
}