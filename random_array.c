#include <stdio.h>
#include <stdlib.h>
#include "array_oper.h"

int main(int argc, char const *argv[])
{
	/* code */
	int num[6]={7,2,8,4,8,6};
	print_int(num,6);
	randomize_in_place(num,6);
	print_int(num,6);
	return 0;
}