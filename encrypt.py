
import base64 
import hashlib 
from Crypto import Random
from Crypto.Cipher import AES
import Crypto.Random 
import base64
import os

def encrypt(raw, key, bs=32):
    key = hashlib.sha256(key.encode()).digest()
    def pad(s):
        return s + (bs - len(s) % bs) * chr(bs - len(s) % bs)

    raw = pad(raw)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw))


if __name__ == "__main__":
    ret = encrypt('ola', 'PASSWORD')
    print(ret)


