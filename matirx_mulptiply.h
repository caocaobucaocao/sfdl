#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "array_oper.h"
/*
	tcc 不支持变长数组
	gcc 支持
*/
typedef struct coordinate
{
	int row0;
	int row1;
	int col0;
	int col1;
}Coordinate;
typedef struct squadron
{
	int **pt;
	int longitude;
	Coordinate cdat;
}Squadron;
Squadron matrix_strassen(Squadron left,Squadron right,int longitude);
Squadron** squadron_decompose(Squadron sqdn);
Squadron squadron_compose(Squadron** sqdns);
Squadron create_squadron(int longitude);
void and_squadron(Squadron left,Squadron right,Squadron res);
void sub_squadron(Squadron left,Squadron right,Squadron res);
void print_squadron(Squadron arg);
Squadron arrto_squadron(int rows, int cols, int arr[rows][cols]);

Squadron matrix_strassen(Squadron left,Squadron right,int longitude)
{
	printf("matrix_strassen,and longitude=%d\n",longitude);
	print_squadron(left);
	print_squadron(right);
	if (left.longitude>1)
	{
		int ltd=longitude/2;
		Squadron** A=squadron_decompose(left);
		Squadron** B=squadron_decompose(right);
		Squadron *S=(Squadron *)malloc(10*sizeof(Squadron));
		int i;
		for (i = 0; i < 10; ++i)
		{
			S[i]=create_squadron(ltd);
		}

		sub_squadron(B[0][1],B[1][1],S[0]);
		and_squadron(A[0][0],A[0][1],S[1]);
		and_squadron(A[1][0],A[1][1],S[2]);
		sub_squadron(B[1][0],B[0][0],S[3]);
		and_squadron(A[0][0],A[1][1],S[4]);
		and_squadron(B[0][0],B[1][1],S[5]);
		sub_squadron(A[0][1],A[1][1],S[6]);
		and_squadron(B[1][0],B[1][1],S[7]);
		sub_squadron(A[0][0],A[1][0],S[8]);
		and_squadron(B[0][0],B[0][1],S[9]);

		Squadron *P=(Squadron *)malloc(7*sizeof(Squadron));
		for (i = 0; i < 7; ++i)
		{
			P[i]=create_squadron(ltd);
		}
		P[0]=matrix_strassen(A[0][0],S[0],ltd);
		P[1]=matrix_strassen(S[1],B[1][1],ltd);
		P[2]=matrix_strassen(S[2],B[0][0],ltd);
		P[3]=matrix_strassen(A[1][1],S[3],ltd);
		P[4]=matrix_strassen(S[4],S[5],ltd);
		P[5]=matrix_strassen(S[6],S[7],ltd);
		P[6]=matrix_strassen(S[8],S[9],ltd);

		Squadron **R=(Squadron **)malloc(2*sizeof(Squadron*));
		
		for (i = 0; i < 2; ++i)
		{
			R[i]=(Squadron *)malloc(2*sizeof(Squadron));
			int j;
			for (j = 0; j < 2; ++j)
			{
				R[i][j]=create_squadron(ltd);
			}
		}
		Squadron temp1=create_squadron(ltd);
		and_squadron(P[4],P[3],temp1);
		Squadron temp2=create_squadron(ltd);
		sub_squadron(P[1],P[5],temp2);
		sub_squadron(temp1,temp2,R[0][0]);
		and_squadron(P[0],P[1],R[0][1]);
		and_squadron(P[2],P[3],R[1][0]);
		and_squadron(P[4],P[0],temp1);
		and_squadron(P[2],P[6],temp2);
		sub_squadron(temp1,temp2,R[1][1]);
		Squadron res=squadron_compose(R);

		for ( i = 0; i < 10; ++i)
		{
			free(S[i].pt);
		}
		for ( i = 0; i < 7; ++i)
		{
			free(P[i].pt);
		}
		for (i = 0; i < 2; ++i)
		{
			int j;
			for (j = 0; j < 2; ++j)
			{
				free(R[i][j].pt);
			}
			free(R[i]);
		}
		return res;
	}
	else
	{
		printf("understratum\n");
		Squadron res=create_squadron(1);
		res.pt[0][0]=left.pt[left.cdat.row0][left.cdat.col0]*right.pt[right.cdat.row0][right.cdat.col0];
		print_squadron(res);
		return res;
	}
}

Squadron squadron_compose(Squadron** sqdns)
{
	printf("%s\n","squadron_compose");
	
	int ltd1=sqdns[0][0].longitude;
	int ltd2=sqdns[0][0].longitude*2;
	Squadron res=create_squadron(ltd2);

	int i;
	for ( i = 0; i < 2; ++i)
	{
		int j;
		for (j = 0; j < 2; ++j)
		{
			print_squadron(sqdns[i][j]);
			int k;
			for ( k = 0; k < ltd1; ++k)
			{
				int v;
				for (v = 0; v < ltd1; ++v)
				{
					res.pt[k+i*ltd1][v+j*ltd1]=
					sqdns[i][j].pt[k][v];
				}
			}
		}
	}
	print_squadron(res);
	return res;
}

Squadron** squadron_decompose(Squadron sqdn)
{	
	Squadron **res=(Squadron **)malloc(2*sizeof(Squadron*));
	int i;
	for (i = 0; i < 2; ++i)
	{
		res[i]=(Squadron *)malloc(2*sizeof(Squadron));
	}
	int ltd=sqdn.longitude/2;
	int x1=sqdn.cdat.col0+ltd-1;
	int x2=sqdn.cdat.col0+ltd;
	int y1=sqdn.cdat.row0+ltd-1;
	int y2=sqdn.cdat.row0+ltd;
	Coordinate cdat;
	cdat=(Coordinate){sqdn.cdat.row0,y1,sqdn.cdat.col0,x1};
	res[0][0]=(Squadron){sqdn.pt,ltd,cdat};
	cdat=(Coordinate){sqdn.cdat.row0,y1,x2,sqdn.cdat.col1};
	res[0][1]=(Squadron){sqdn.pt,ltd,cdat};
	cdat=(Coordinate){y2,sqdn.cdat.row1,sqdn.cdat.col0,x1};
	res[1][0]=(Squadron){sqdn.pt,ltd,cdat};
	cdat=(Coordinate){y2,sqdn.cdat.row1,x2,sqdn.cdat.col1};
	res[1][1]=(Squadron){sqdn.pt,ltd,cdat};
	return res;
}
void print_squadron(Squadron arg)
{
	printf("{longitude=%d,row0=%d,row1=%d,col0=%d,col1=%d}\n",
		arg.longitude,arg.cdat.row0,arg.cdat.row1,arg.cdat.col0,arg.cdat.col1);
	int i;
	for ( i = arg.cdat.row0; i <= arg.cdat.row1; ++i)
	{
		
		int j;
		for (j = arg.cdat.col0; j <= arg.cdat.col1; ++j)
		{
			printf("[%d,%d]=%d,",i,j,arg.pt[i][j]);
		}
		printf("\b \b");
		printf("\n");
	}
}
Squadron create_squadron(int longitude)
{
	int **pt=(int **)malloc(longitude*sizeof(int *));
	int i=0;
 	for (; i < longitude; ++i)
 	{
 		pt[i]=(int *)malloc(longitude*sizeof(int));
 		int j;
 		for (j = 0; j < longitude; ++j)
 		{
 			pt[i][j]=0;
 		}
 	}
 	Coordinate cdat={0,longitude-1,0,longitude-1};
 	Squadron res={pt,longitude,cdat};
	return res;
}
void and_squadron(Squadron left,Squadron right,Squadron res)
{
	printf("and_squadron\n");
	
	int i;
	for ( i = 0; i < res.longitude; ++i)
	{
		int j;
		for (j = 0; j < res.longitude; ++j)
		{
			res.pt[i][j]=left.pt[left.cdat.row0+i][left.cdat.col0+j]
				+right.pt[right.cdat.row0+i][right.cdat.col0+j];
		}
	}
	print_squadron(left);
	print_squadron(right);
	print_squadron(res);
}
void sub_squadron(Squadron left,Squadron right,Squadron res)
{
	printf("sub_squadron\n");
	int i;
	for ( i = 0; i < res.longitude; ++i)
	{
		int j;
		for (j = 0; j < res.longitude; ++j)
		{
			res.pt[i][j]=left.pt[left.cdat.row0+i][left.cdat.col0+j]
				-right.pt[right.cdat.row0+i][right.cdat.col0+j];
		}
	}
	print_squadron(left);
	print_squadron(right);
	print_squadron(res);
}
Squadron arrto_squadron(int rows, int cols, int arr[rows][cols])
{
	printf("arrto_squadron\n");
	double f=(rows>cols)?log(rows)/log(2):log(cols)/log(2);
 	double n= pow(2,ceil(f));
 	int **pt=(int **)malloc(n*sizeof(int *));
 	int i;
 	for (i=0; i < n; ++i)
 	{
 		pt[i]=(int *)malloc(n*sizeof(int));
 	}
 	for (i = 0; i < rows; ++i)
 	{
 		int j;
 		for (j = 0; j < cols; ++j)
 		{
 			pt[i][j]=arr[i][j];
 		}
 	}
 	for (i = 0; i < n; ++i)
 	{
 		int j;
 		for (j =0; j < n; ++j)
 		{
 			if (i>=rows||j>=cols)
 			{
 				pt[i][j]=0;
 			}
 		}
 	}
 	Coordinate cdat={0,n-1,0,n-1};
 	Squadron squadron={pt,(int)n,cdat};
 	print_squadron(squadron);
 	return squadron;
 }