#include <stdio.h>

#define UINT_SIZE (sizeof(unsigned int) * 8)

#define BITMAP_OFFSET(BITMAP, OFFSET) (BITMAP[OFFSET/UINT_SIZE] & (1 << (OFFSET % UINT_SIZE)))

#define BITMAP_IS_1(BITMAP, OFFSET) (BITMAP_OFFSET(BITMAP, OFFSET) >= 1)
#define BITMAP_IS_0(BITMAP, OFFSET) !BITMAP_IS_1(BITMAP, OFFSET)

#define BITMAP_SET_1(BITMAP, OFFSET) (BITMAP[OFFSET/UINT_SIZE] |= (1 << (OFFSET % UINT_SIZE)))
#define BITMAP_SET_0(BITMAP, OFFSET) (BITMAP[OFFSET/UINT_SIZE] &= ~(1 << (OFFSET % UINT_SIZE)))

#define BITMAP_COUNT_1
#define BITMAP_COUNT_0

#define BITMAP_FIRST_1
#define BITMAP_FIRST_0

int main(void)
{
    int i;

    // 0,33,64,65
    // unsigned int bitmap[10] = {1, 2, 3};
    const int ARRSIZE = 256;
    unsigned int bitmap[ARRSIZE] = {0};
    for (i = 0; i < 50; i++) {
        BITMAP_SET_1(bitmap, i * 3);
    }

    for (i = 0; i < 100; i++) {
        if (BITMAP_IS_1(bitmap, i)) {
            printf("%d:%d ", i, BITMAP_IS_1(bitmap, i));
            printf("arr_idx:%lu, left:%lu \n", i/UINT_SIZE, (i%UINT_SIZE));
        }
    }
    printf("\n");
#if 0
    for (i = 0; i < 10; i++) {
        printf("%d:%d ", i, bitmap[i]);
    }
#endif
    return 0;
}
