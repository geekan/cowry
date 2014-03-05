#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define ARRAY_SIZE(ARRAY) (sizeof(ARRAY)/sizeof(*ARRAY))

void swap(int *a, int *b)
{
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void select_sort(int *a, int left, int right)
{
	int i, j;
	int bigValue = 0, bigIndex = 0;
	for (i = left; i <= right; i++) {
		for (j = i; j <= right; j++) {
			if (a[j] > bigValue) {
				bigValue = a[j];
				bigIndex = j;
			}
		}
		bigValue = 0;
		swap(a + i, a + bigIndex);
	}
}

int main()
{
	int i;
	int a[] = {1, 5, 9, 7, 3};
	int asize = ARRAY_SIZE(a);
	select_sort(a, 0, asize - 1);
	for (i = 0; i < asize; i++)
		printf("%d ", a[i]);
	return 0;
}