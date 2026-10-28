import hashlib
import os

pass_w = input("Enter your password: ")
salt = os.urandom(16) 

h_object = hashlib.sha256(salt + pass_w.encode())

print(f"{salt.hex()}:{h_object.hexdigest()}")
