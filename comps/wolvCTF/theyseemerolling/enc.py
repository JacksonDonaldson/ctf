
from Crypto.Util.strxor import strxor
from Crypto.Util.number import long_to_bytes
import os

key = os.urandom(8)

def encrypt_block(block):
  #print(len(block))
  #print(block)
  return strxor(key, block)

def encrypt(pt):
  ct = b''
  for i in range(0, len(pt), 4):
    index = long_to_bytes(i // 4)
    index = b'\x00' * (4 - len(index)) + index
    #print(pt[i:i+4])
    #print(index)
    #print(index + pt[i:i+4])
    ct += encrypt_block(index + pt[i:i+4])
  return ct

if __name__ == '__main__':
  start = bytes.fromhex("983f687f")
  flag = bytes.fromhex("983f687f03f884a9983f687e0ff2afbc983f687d03a891bd983f687c2bf68990983f687b04e9c0a9983f687a2be8c4a6983f687910c482ff983f687818f7afb6983f687744ee8290983f687644ec9e90983f687517e989bf983f687400ab8dcf")
  flag += b'\x00' * (4 - len(flag) % 4)

  o = open("output.txt", "wb")
  for i in range(2**32):
    if(i % 10000 == 0):
      print(i)
    j = long_to_bytes(i)
    key = start + b'\x00' * (4 - len(j)) + j
    
  #flag = open('flag', 'rb').read()
    o.write(encrypt(flag))
    o.write(b"\n")

  print(encrypt(flag).hex())
