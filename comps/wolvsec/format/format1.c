#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void print_flag(void)
{
    char flag[] = { 0x49, 0x5d, 0x4a, 0x58, 0x45, 0x7f, 0x6d, 0x72,
                    0x6c, 0x61, 0x7a, 0x0d, 0x58, 0x0d, 0x5f, 0x6a,
                    0x0d, 0x7a, 0x4, 0x17, 0x43, 0x00 };

    for (int i = 0; i < strlen(flag); ++i) {
        flag[i] ^= 62;
    }

    printf("%s\n", flag);
    exit(0);
}

void vuln(void)
{
    char buffer0[20] = { 0 };

    printf("What is your favorite format string?\n");
    scanf("%s", buffer0);
    printf(buffer0);
    puts("");
    printf("What is your favorite overflow?\n");
    scanf("%s", buffer0);
}

int main(void)
{
    vuln();

    return 1;
}
