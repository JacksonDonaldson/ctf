#include <iostream>

int main(){
	int i = 0;

	long local_68 = 0x5e1b62514c5e495d;
	long local_60 = 0x1f5819411b424249;
	long local_58 = 0x5e75194e1b5f6d75;
	long local_50 = 0x1e6d7519425e751a;
	long local_48 = 0x1e750b0b53521e46;
	long local_40 = 0x5718;
	char result[50];

	for(int i = 0; i < 256; i++ ){

	
	for (int local_c = 0; local_c < 0x2a; local_c = local_c + 1) {
    *(char *)((long)&result + (long)local_c) =
         *(char *)((long)&local_68 + (long)local_c) ^ i;
  	}

	std::cout << result << std::endl;
	}
}