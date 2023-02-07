#include <stdio.h>
#include <string.h>
#include <stdlib.h>


void print_flag(void)
{
    char flag[] = { 0xf2, 0xe6, 0xf1, 0xe3, 0xfe, 0xc3, 0xe8, 0xf1, 0xda,
                    0xf6, 0xd1, 0xf7, 0xb4, 0xeb, 0xe2, 0xb6, 0xda, 0xe1,
                    0xb1, 0xeb, 0xe2, 0xb6, 0xf7, 0xa4, 0xf8, 0x00 };

    for (int i = 0; i < strlen(flag); ++i) {
        flag[i] ^= 133;
    }

    printf("%s\n", flag);
    exit(0);
}

void vuln(void)
{
    char buffer0[16] = { 0 };

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
