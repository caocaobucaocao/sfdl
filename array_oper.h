#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int random_int(int index_start,int length)
{
	return rand()%(length-index_start)+index_start;
}
void randomize_in_place(int data[],int length)
{
	srand(time(0));
	int i;
	for (i = 0; i < length; ++i)
	{
		int temp=data[i];
		int rdm=random_int(i,length);
		data[i]=data[rdm];
		data[rdm]=temp;

	}
}

void print_int(int num[],int length)
{
	int i = 0;
	printf("%c",'{' );
	for (; i < length; ++i)
	{
		printf("[%d,%d]",i,num[i] );
	}
	printf("%c",'}' );
	printf("\n");
}
void array_copy(int num[],int start,int end,int * targer)
{
	
	int i=start;
	for (; i <= end; ++i)
	{
		targer[i]=num[i];
	}
}
int duplicate_removal(int num[],int length,int *res)
{
	int i=1;
	int j=0;
	for (; i <= length; i++)
	{
		if (num[i]!=num[i-1])
		{
			res[j]=num[i-1];
			j++;
		}
	}
	return --j;
}
void array_uinon(int num1[],int start1,int end1 ,int num2[],int start2,int end2,int target[])
{
	int i=start1;
	for (; i <= end1; ++i)
	{
		target[i]=num1[i];
	}
	int j=start2;
	for (; j <= end2; ++j)
	{
		target[i]=num2[j];
		i++;
	}
}