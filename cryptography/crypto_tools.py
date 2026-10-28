import hashlib
import base64
import sys

if(len(sys.argv) != 2 ): 
	print("Error: wrong arguments. \nUsage: python3 crypto_tools.py <string>")
	sys.exit(1)

data = sys.argv[1]
data = data.encode()

data_base64 = base64.b64encode(data)
data_base64 = data_base64.decode()

data_hex = data.hex()

data_md5 = hashlib.md5(data)

data_sha1 = hashlib.sha1(data)

data_sha256 = hashlib.sha256(data) 

print(f"base64: {data_base64}")
print(f"hexadecimal: {data_hex}")
print(f"MD5: {data_md5.hexdigest()}")
print(f"SHA1: {data_sha1.hexdigest()}")
print(f"SHA256: {data_sha256.hexdigest()}")
