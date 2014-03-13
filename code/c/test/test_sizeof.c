#include <stdio.h>

int func(int x)
{

    int arr[x];
    printf("func: %d %d\n", sizeof(arr), sizeof(arr[x++]));
    printf("%d\n", x);
    return 0;
}

int main(void)
{
    int x = 0;
    char *a, b[20];
    printf("x:%d a:%d b:%d\n", sizeof(x++), sizeof(a), sizeof(b));
    printf("x:%d a:%d b:%d\n", sizeof(x + 1), sizeof(a + 1), sizeof(b + 1));
    printf("x:%d a:%d b:%d\n", x, sizeof(a), sizeof(b));
    printf("x:%d a:%d b:%d\n", x, sizeof(a), sizeof(b));
    func(10);
}
