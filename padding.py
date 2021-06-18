from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os
key = os.urandom(32)
iv = os.urandom(16)

aesCipher = Cipher(algorithms.AES(key), modes.CBC(iv),
            backend=default_backend())

aesEncryptor = aesCipher.encryptor()
aesDecryptor = aesCipher.decryptor()

padder = padding.PKCS7(128).padder()
unpadder = padding.PKCS7(128).unpadder()

plaintexts = [ b"SHORTASDKJHASDPOIQWEOIASd",
b"MEDIUM MEDIUM MEDIUM",
b"LONG LONG LONG LONG LONG LONG",]


ciphertexts = []
for m in plaintexts:
    padded_message = padder.update(m)
    ciphertexts.append(aesEncryptor.update(padded_message))
    
ciphertexts.append(aesEncryptor.update(padder.finalize()))

for c in ciphertexts:
    padded_message = aesDecryptor.update(c)
    print("recovered", unpadder.update(padded_message))

print("recovered", unpadder.finalize())


def sslv3Pad(msg):
    padNeeded = (-len(msg) % 16) - 1
    padding = padNeeded.to_bytes(padNeeded+1,"big")

def sslv3Unpad(padded_message):
    paddingLen = padded_message[-1]+1
    return 