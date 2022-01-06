#include <math.h>
#include "merger.h"
void decompose(int num[],int p,int r)
{
	float p1=(float)p;
	float r1=(float)r;
	int q=p+(int)ceil((r1-p1+1)/2)-1;
	if (p<r)
	{
		decompose(num,p,q);
		decompose(num,q+1,r);
		meger(num,r-p+1,p,q,r);
	}

}