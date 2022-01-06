#include <math.h>
#include "decompose.h"
void meger_sort(int num[],int length,int factor);
int main(int argc, char const *argv[])
{
	int num[6]={7,2,8,4,8,6};
	meger_sort(num,6,3);
	return 0;
}
void meger_sort(int num[],int length,int factor)
{
	/*
		factor 为子问题最小数目，当k<=1,不可再缩小
	*/
	int k=ceil(log(length)/log(factor));
	printf("%d",k);

	if (k>1)
	{
		
	}
}