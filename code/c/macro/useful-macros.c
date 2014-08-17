#include <stdio.h>
#include <stdlib.h>


#define PRINT(STH) printf("%s\n", #STH)
#define DO(STH) \
    PRINT(STH); \
    STH

#define TRY
#define CATCH


int foo(void)
{
    return 0;
}

int bar(void)
{
    return 1;
}

int macro(void)
{
    printf("%d\n", 2);
    return 2;
}

#define M1 macro()
#define M2 M1
#define M3 M2
#define M4() M3

int main(void)
{
    DO(foo());
    DO(bar());
    DO(M4());

    return 0;
}
