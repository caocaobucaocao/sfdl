/*
	将两个有序子列合并
*/
void meger(int num[],int length,int p,int q,int r)
{
	int n1=q-p+1;
	int n2=r-q;
	int *ptleft;
	int *ptright;
	ptleft=(int *)malloc(n1*sizeof(int));
	ptright=(int *)malloc(n2*sizeof(int));
	int i=0;
	for (; i < n1; ++i)
	{
		ptleft[i]=num[p+i];
	}
	int j=0;
	for (; j < n2; ++j)
	{
		ptright[j]=num[q+j+1];
	}
	i=0;
	j=0;
	int k=p;
	for (; i < n1 && j < n2 && k <= r; ++k)
	{
		if (ptleft[i]<ptright[j])
		{
			num[k]=ptleft[i];
			++i;
		}
		else
		{
			num[k]=ptright[j];
			++j;
		}

	}
	/*
		处理剩余情况
	*/
	if (i!=n1-1||j!=n2-1)
	{
		/*
		右侧有剩余
		*/
		if (i==n1)
		{
			for (; j < n2; ++j,++k)
			{
				num[k]=ptright[j];
			}
		}
		/*
		左侧有剩余
			*/
		else
		{	
			for (; i < n1; ++i)
			{
				num[k]=ptleft[i];
				++k;
			}	
		}
	}
	free(ptleft);
	free(ptright);
}