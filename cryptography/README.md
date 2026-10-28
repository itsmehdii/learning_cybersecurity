# CRYPTO 

Small Python tools to practice encoding and hashing.

## crypto_tools.py
Takes a string and prints its Base64, hex, MD5, SHA-1 and SHA-256.

**Usage**
```
python3 crypto_tools.py <string>
```

**Example**
```
$ python3 crypto_tools.py hello
base64: aGVsbG8=
hexadecimal: 68656c6c6f
MD5: 5d41402abc4b2a76b9719d911017c592
SHA1: aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
SHA256: 2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824
```

## salt_hash.py
Asks for a password, generates a random 16-byte salt (`os.urandom`) and prints `salt:hash`, where hash = SHA-256(salt + password).
Same password, different salt each run → different hash.

## verify.py
Asks for a password and a stored `salt:hash` line, recomputes SHA-256(salt + password) and prints `True` if it matches, `False` otherwise.

## Notes
- Encoding (Base64, hex) is reversible; hashing is one-way.
- MD5 and SHA-1 are broken for security use; they are here for recognition only.
- SHA-256 is fast, so real password storage should use a slow hash (bcrypt, Argon2). This is a learning project.

## Requirements
Python 3, standard library only.
