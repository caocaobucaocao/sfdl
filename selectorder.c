#include <stdio.h>
void selectorder(int[],int);
int main(int argc, char const *argv[])
{
	int num[6]={7,2,8,4,8,6};
	int length=sizeof(num)/sizeof(int);
	selectorder(num,length);
	int i;
	for (i = 0; i <length; ++i)
	{
		printf("%d==%d\n",i,num[i]);
	}
	return 0;
}
void selectorder(int num[],int length)
{
	printf("%d\n", length);
	int i;
	int key;
	int index;
	for (i=0; i < length; ++i)
	{
		index=i;
		key=num[i];
		int j=i+1;
		for(;j<length;j++)
		{	
			if(key>num[j])
			{
				index=j;
				key=num[j];
			}
			
		}
		int temp;
		temp=num[i];
		num[i]=key;
		num[index]=temp;
		printf(",i=%d,index=%d,key=%d\n",i,index,key );
	}

}