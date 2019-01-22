

import base64
import hashlib
from Crypto import Random
from Crypto.Cipher import AES
import Crypto.Random 
import base64
import os

def decrypt(enc, decryption_key):
    def unpad(s):
        return s[:-ord(s[len(s)-1:])]

    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    key = hashlib.sha256(decryption_key.encode()).digest()
        
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[AES.block_size:]))



if __name__=='__main__':
    ter = decrypt('yI1Gmxz+Zlr3YTM6902OUGeMTkLOOWWIkOKIQBJGL4xr13/bNO0dzlEoqUF+hYUk', 'PASSWORD')
    print(ter)