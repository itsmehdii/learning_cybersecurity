import sys

if(len(sys.argv) != 2):
        print("Error: wrong number of arguments\nxor_bruteforce.py <file>")
        sys.exit(1)

with open(sys.argv[1], "rb") as f:
    data = f.read()

for key in range(256):
	result = bytes(key ^ byte for byte in data)
	if b"NEONHAT" in result: 
		print(f"key: {hex(key)}, result: {result.decode()}")

