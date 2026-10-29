 xor_bruteforce.py Breaks single-byte XOR: tries all 256 keys and prints the key and the decrypted text for the one whose output contains the flag marker `NEONHAT`. 
 
 Usage: python3 xor_bruteforce.py <file> 
 
 Limitation: only finds the key if the plaintext contains `NEONHAT`.
