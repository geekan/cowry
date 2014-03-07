#include <stdio.h>

int swap(int *a, int *b)
{
 	int tmp = *a;
	*a = *b;
	*b = tmp;
	return tmp;
}

int main(void)
{
	int x = 16;
	int y = 32;
	int ret = swap(&x, &y);
	printf("ret: %d", ret);
	return 0;
}
