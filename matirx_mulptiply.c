#include <stdlib.h>
#include "matirx_mulptiply.h"
int main(int argc, char const *argv[])
{
	int num0[5][6]={
		{1,2,3,4,5,6},
		{6,5,4,3,2,1},
		{2,3,5,6,1,4},
		{1,2,3,4,5,6},
		{6,5,4,3,2,1}						
					};
	Squadron s0=arrto_squadron( 5,6,num0);
	int num1[6][5]={
		{1,2,3,4,5},
		{6,5,4,3,2},
		{2,3,5,6,1},
		{1,2,3,4,5},
		{6,5,4,3,2},
		{6,5,4,3,2}						
					};
	Squadron s1=arrto_squadron(6,5,num1);
	matrix_strassen(s0,s1,s1.longitude);
	free(s0.pt);
	free(s1.pt);
	return 0;
}