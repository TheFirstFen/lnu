import hashlib

pwd = "Hejjjj123"

def hashit(pwd):
    binary = pwd.encode()
    print(binary)
    hashed = hashlib.sha256().hexdigest()
    print(hashed)
    
hashit(pwd)
hashit(pwd)