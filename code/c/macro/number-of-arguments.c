#include <stdio.h>
#include <string.h>
#include <stdarg.h>

#define NUMARGS(...)  (sizeof((int[]){__VA_ARGS__})/sizeof(int))
#define SUM(...)  (sum(NUMARGS(__VA_ARGS__), __VA_ARGS__))

void sum(int numargs, ...);

int main(int argc, char *argv[]) {

    SUM(1);
    SUM(1, 2);
    SUM(1, 2, 3);
    SUM(1, 2, 3, 4);

    return 1;
}

void sum(int numargs, ...) {
    int     total = 0;
    va_list ap;

    printf("sum() called with %d params:", numargs);
    va_start(ap, numargs);
    while (numargs--)
        total += va_arg(ap, int);
    va_end(ap);

    printf(" %d\n", total);

    return;
}
