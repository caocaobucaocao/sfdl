#include <stdio.h>
void insertOrder(int[],int);
void insertOper(int [],int );
void megerOrder(int [],int );
void arrayCopy(int [],int ,int ,int []);
void printArray(int[],int);
int main(int argc, char const *argv[])
{
	int num[6]={7,2,8,4,8,6};
	int num2[6];
	arrayCopy(num,0,5,num2);
	insertOrder(num,sizeof(num)/sizeof(int));
	printArray(num,sizeof(num)/sizeof(int));
	megerOrder(num2,5);
	printArray(num2,sizeof(num2)/sizeof(int));
	return 0;
}
void insertOrder(int num[],int length)
{
	printf("num is a pointer ,length=%d\n",sizeof(num) );
	int i;						
	for (i=1; i < length; ++i)		//length
	{
		int j=i-1;					//length
		int key=num[i];
		while(key<num[j]&&j>=0)		//i 从1到length，在此情况下此语句执行次数，总和
		{
			num[j+1]=num[j];
			num[j]=key;
			--j;
		}
	}
}
/*
	问题分解
*/
void megerOrder(int num[],int tag)
{
	if (tag>1)
	{
		megerOrder(num,tag-1);
	}
	insertOper(num,tag);
}
/*
	当子列有序时选择的插入方法
*/
void insertOper(int num[],int tag)
{
	int i=tag-1;						
	for (; i >=0; --i)		//length
	{
		if (num[i]>num[tag])
		{
			int temp=num[i];
			num[i]=num[tag];
			num[tag]=temp;
			tag=i;
		}
	}
}
void arrayCopy(int num[],int start,int end,int target[])
{
	int i=0;
	for (i = 0; i < end-start+1; ++i)
	{
		target[i]=num[start+i];
	}
}
void printArray(int num[],int length)
{
	int i=0;
	printf("[");
	for (; i < length; ++i)
	{
		printf("%d,",num[i]);
	}
	printf("\b]\n");
}