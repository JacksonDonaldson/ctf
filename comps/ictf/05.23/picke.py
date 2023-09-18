import pickle
import pdb
import io
flag = "80 04 7D 28 4B 2A 4B 75 4B 12 4B 37 4B 26 4B 67 4B 15 4B 5F 4B 28 4B 72 4B 1E 4B 5F 4B 05 4B 70 4B 19 4B 33 4B 22 4B 5F 4B 07 4B 63 4B 2C 4B 7D 4B 11 4B 5F 4B 13 4B 68 4B 10 4B 6D 4B 0F 4B 30 4B 0A 4B 33 4B 24 4B 34 4B 20 4B 72 4B 25 4B 6E 4B 1A 4B 72 4B 23 4B 64 4B 1B 4B 6E 4B 08 4B 6B 4B 03 4B 66 4B 0B 4B 35 4B 0E 4B 72 4B 1C 4B 33 4B 21 4B 33 4B 29 4B 30 4B 04 4B 7B 4B 18 4B 37 4B 14 4B 33 4B 2B 4B 35 4B 1F 4B 34 4B 0D 4B 66 4B 17 4B 6E 4B 01 4B 63 4B 00 4B 69 4B 0C 4B 5F 4B 27 4B 33 4B 1D 4B 37 4B 02 4B 74 4B 06 4B 31 4B 09 4B 31 4B 16 4B 31 75 2E"
flag = flag.replace(" ", "")
flag = bytes.fromhex(flag)

flag = pickle.loads(flag)

keys = list(flag.keys())
keys.sort()

for i in keys:
    print(chr(flag[i]), end = "")
    

