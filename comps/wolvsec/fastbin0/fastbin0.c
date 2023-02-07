#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MSG_SIZE 0x20

typedef struct {
    char msg[MSG_SIZE];
    unsigned int unlocked;
} vault_t;

char flag[MSG_SIZE] = {0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x0f, 0x56, 0x42,
                       0x55, 0x47, 0x5a, 0x4f, 0x11, 0x55, 0x7e, 0x52, 0x11, 0x7e,
                       0x47, 0x15, 0x14, 0x55, 0x7e, 0x49, 0x54, 0x49, 0x5c, 0x0f,
                       0x0f, 0x0f};

void vault_print_message(vault_t* vault) {
    char printMsg[MSG_SIZE + 1];
    memcpy(printMsg, vault->msg, MSG_SIZE);
    printMsg[MSG_SIZE] = '\0';

    for (int i = 0; i < MSG_SIZE; ++i) {
        printMsg[i] ^= 33;
    }

    printf("%s\n", printMsg);
}

int main(void) {
    vault_t* pAliceVault = malloc(sizeof(vault_t));
    memcpy(pAliceVault, flag, MSG_SIZE);
    pAliceVault->unlocked = 1;
    vault_t* pBobVault = malloc(sizeof(vault_t));
    memcpy(pBobVault, flag, MSG_SIZE);
    pBobVault->unlocked = 1;

    puts("Welcome to UM's super secure message vault");
    while (1) {
        puts("1) view vault\n2) delete vault\n3) new vault\n4) quit");
        char action = -1;
        scanf(" %c", &action);

        if (action == '1' || action == '2') {
            char person = -1;
            puts("A) Alice's message\nB) Bob's message");
            scanf(" %c", &person);

            if (person == 'A' || person == 'B') {
                vault_t* pVault = person == 'A' ? pAliceVault : pBobVault;

                if (action == '1') {
                    printf("Invalid authentication for bank address %p! Sorry :(\n", pVault);
                } else if (action == '2') {
                    printf("Deleted bank address: %p\n", pVault);
                    free(pVault);
                }
            } else {
                puts("Unknown person");
            }
        } else if (action == '3') {
            vault_t* pNewVault = malloc(sizeof(vault_t));
            printf("Your bank address: %p\n", pNewVault);

            pNewVault->unlocked--; // prevent people from reading our vault!!
            if (pNewVault->unlocked) {
                vault_print_message(pNewVault);
            } else {
                puts("Done!");
            }
        } else if (action == '4') {
            break;
        } else {
            puts("Unknown command!");
        }
        puts("");
    }
    return EXIT_SUCCESS;
}
