import hashlib

password = input("Enter your password: ") 
line = input ("Enter your salt:hash line: ") 

salt_hex, stored_hash = line.split(":") 
salt_hex = salt_hex.strip()
stored_hash =stored_hash.strip()

salt = bytes.fromhex(salt_hex)

h_object = hashlib.sha256(salt)

h_object.update(password.encode())

if(h_object.hexdigest() == stored_hash): 
	print("True") 
else: 
	print("False")


