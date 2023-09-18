#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main(){
    uint t = time(NULL);
    cout << t << endl;
    
    FILE* inputFile = fopen("out.bin", "r");

    byte chars[64];

    fscanf(inputFile, "%s", chars);
    fclose(inputFile);


    //cout << (u_char)chars[0] << endl;


    while(true){
        t--;
        srand(t);

        byte testChar[64];
        for(int i = 0; i < 0x40; i++){
            testChar[i] = chars[i];
        }

        for(int c = 0; c < 0x40; c++){
            for(int local_10 = 0; local_10 <= c; local_10++){
                int iVar = rand();
                testChar[c] = (byte)((u_char)iVar ^ (u_char)testChar[c]);

            }
            if(testChar[0] != (byte)'i'){
                break;
            }
            if(c == 1 && testChar[1] != (byte)'c'){
                break;
            }
            if(c == 2 && testChar[2] != (byte)'t'){
                break;
            }
            if(c == 3 && testChar[3] != (byte)'f'){
                break;
            }
            if(c == 4 && testChar[4] != (byte)'{'){
                break;
            }
        }

        if(testChar[0] == (byte)'i' && testChar[1] == (byte)'c' && testChar[2] == (byte)'t' && testChar[3] == (byte)'f'){
            for(int j = 0; j < 0x40; j++){
                cout << (u_char)testChar[j];
            }
            cout << endl;
        }

        if(t % 10000000 == 0){
            cout << t;
            cout << endl;
        }
        
    }
}