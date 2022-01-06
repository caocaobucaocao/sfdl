#include <stdio.h>
#include <math.h>
#include <limits.h>
typedef struct max_subarray_info
{
	int sum;
	int low;
	int high;
} Result;
Result find_max_subarray(int num[],int low,int high);
Result find_max_cross_subarray(int num[],int low,int middle,int high);
Result find_max_subarray_bypart(int num[],int low,int high);
int main(int argc, char const *argv[])
{
	int num[10]={7,-2,-8,4,-8,6,10,-11,-8,9};
	Result r=find_max_subarray(num,0,9);
	printf("form %d to %d sum=%d\n",r.low,r.high, r.sum);
	r=find_max_subarray_bypart(num,0,9);
	printf("form %d to %d sum=%d\n",r.low,r.high, r.sum);
	return 0;
}

Result find_max_subarray_bypart(int num[],int low,int high)
{
	int i=low;
	int sum=0;
	int left_sum=0;
	int start,end;
	int p=low,q=low;
	//{7,-2,-8,4,-8,6,10,-11,-8}
	for (; i <= high; ++i)
	{
		sum+=num[i];
		if (sum<0)
		{
			sum=0;
			p=i+1;
			q=i+1;
			continue;
		}
		if (left_sum<sum)
		{
			left_sum=sum;
			start=p;
			end=q;
			continue;
		}
		q++;
	}
	Result res;
	res.sum=left_sum;
	res.low=start,
	res.high=end;
	return res;
}

Result find_max_subarray(int num[],int low,int high)
{
	if (low==high)
	{
		Result result;
		result.sum=num[low];
		result.low=low;
		result.high=high;
		printf("{%d,",result.sum );
		printf("%d,",low);
		printf("%d}\n",high);
		return result;
	}
	else
	{
		float p1=(float)low;
		float r1=(float)high;
		int middle=low+(int)ceil((r1-p1+1)/2)-1;
		Result res1=find_max_subarray(num,low,middle);
		Result res2=find_max_subarray(num,middle+1,high);
		Result res3=find_max_cross_subarray(num,low,middle,high);
		if (res1.sum>res2.sum&&res1.sum>res3.sum)
		{
			return res1;
		}
		else if(res2.sum>res3.sum&&res2.sum>res1.sum)
		{
			return res2;
		}
		else
		{
			return res3;
		}
	}
}
Result find_max_cross_subarray(int num[],int low,int middle,int high)
{
	Result result;
	if (low<middle&&middle<high)
	{
		// {7,-2,-8,4,-8,6,10,-11,-8};
		printf("low=%d,mid=%d,high=%d\n",low,middle,high );
		int left_sum=num[middle];
		int right_sum=num[middle];
		int sum=left_sum;
		int left_index=middle-1;
		int right_index=middle+1;
		int i=left_index;
		for (; i >= low; --i)
		{
			sum=sum+num[i];
			if (sum>left_sum)
			{
				left_sum=sum;
				left_index=i;
			}
			
		}
		i=right_index;
		sum=right_sum;
		//{7,-2,-8,4,-8,6,10,-11,-8};
		for (; i <= high; ++i)
		{
			sum+=num[i];
			if (sum>right_sum)
			{
				right_sum=sum;
				right_index=i;
			}
			
		}
		right_index--;
		result.sum=left_sum+right_sum-num[middle];
		printf("%d,",result.sum );
		result.low=left_index,
		printf("%d,",left_index);
		result.high=right_index;
		printf("%d,\n",right_index);
	}
	else
	{
		result.sum=INT_MIN;
	}
	return result;
}