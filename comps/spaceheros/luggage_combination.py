from pwn import *

plaintext = b'****************************************'
key1 = b'****************************************'
key2 = b'****************************************'

def shield_combination(p, k1, k2):
	A = xor(p, k1, k2)
	B = xor(p, k1)
	C = xor(p, k2)
	return A + B + C

print(shield_combination(plaintext, key1, key2).hex())

vals = "783f3977627a693a320f313e421e29513e036e485565360a172b00790c211a7b117b4a7814510b2d4b0b01465448580a0369520824294c670c3758706407013e271b624934147f1e70187c1c72666949405c5b4550495e5e02390607217f11695a61587c6351536b741d301d6d182c48254e7f4927683d19"
a = bytearray.fromhex(vals[:80])
b = bytes.fromhex(vals[80:160])
c = bytes.fromhex(vals[160:])

print(xor(a, b, c))
