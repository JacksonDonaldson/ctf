#include <string.h>
#include <openssl/aes.h>
#include <stdio.h>
int main(){
    AES_KEY *key;

    unsigned char *pw = "Prestidigitation";

    const int b = 0x80;

    
    AES_set_encrypt_key(pw , b, key);

    printf("test\n");
}