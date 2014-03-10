#include <stdio.h>
#define UINT_SIZE (sizeof(unsigned int) * 8)
#define BITMAP_OFFSET(BITMAP, OFFSET) (BITMAP[OFFSET/UINT_SIZE] & (1 << (OFFSET % UINT_SIZE)))
#define BITMAP_IS_1(BITMAP, OFFSET) (BITMAP_OFFSET(BITMAP, OFFSET) >= 1)

int main(void)
{
	int i;
	unsigned int bitmap[10] = {1, 2, 3};
	for (i = 0; i < 100; i++) {
		if (BITMAP_IS_1(bitmap, i)) {
			printf("[%d %d] ", i/UINT_SIZE, 1<<(i%UINT_SIZE));
			printf("%d:%d ", i, BITMAP_IS_1(bitmap, i));
		}
	}
	printf("\n");
	for (i = 0; i < 10; i++) {
		printf("%d:%d ", i, bitmap[i]);
	}
	return 0;
}
