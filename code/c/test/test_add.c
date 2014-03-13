#include <stdio.h>

int main(void)
{
    char c = 'a';
    printf("%d %d %d\n", c, (char)(c + 50), (char)(c + '0' + '0'));
    printf("%d %d %d\n", c, (c + 50), (c + '0' + '0'));
}
