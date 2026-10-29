import sys

if(len(sys.argv) != 4): 
	print("Error: wrong number of arguments\nUsage: python3 xor.py <input> <key> <output>")
	sys.exit(1)

Input = open(sys.argv[1], "rb")
try:
	key = int(sys.argv[2], 0)
except ValueError:
	print("Wrong key!\nkey must be a number (e.g. 75 or 0x4B)")
	sys.exit(1)

if(key<0 or key>255) : 
	print("wrong key!\nKey must be in range [0; 255]")
	sys.exit(1)
output = sys.argv[3]

with open(output, "wb") as out:
	data = Input.read()
	for byte in data:
		out.write(bytes([key^byte]))
