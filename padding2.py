from cryptography.hazmat.primitives.ciphers import Cipher, algorithms,modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

class EncryptionManager:
    def  __init__(self):
        key = os.urandom(32)
        iv = os.urandom(16)
        aesContext = Cipher (algorithms.AES(key),
                             modes.CBC(iv),
                             backend=default_backend())

        self.encryptor = aesContext.encryptor()
        self.decryptor = aesContext.decryptor()
        self.padder = padding.PKCS7(128).padder()
        self.unpadder = padding.PKCS7(128).unpadder()

    def update_encryptor(self,plaintext):
            return self.encryptor.update(self.padder.update(plaintext))

    def finalize_encryptor(self):
            return self.encryptor.update(self.padder.finalize()) + self.encryptor.finalize()

    def update_decryptor(self,ciphertext):
            return self.unpadder.update(self.decryptor.update(ciphertext))

    def finalize_decryptor(self):
            return self.unpadder.update(self.decryptor.finalize()) + self.unpadder.finalize()

manager = EncryptionManager()
`
string = input()

plaintext = [bytes(string, 'utf-8') for i in string]

ciphertext = []

ciphertext2 =[]

for m in plaintext:
    ciphertext.append(manager.update_encryptor(m))
ciphertext.append(manager.finalize_encryptor())

manager2 = EncryptionManager()

for k in plaintext:
    ciphertext2.append(manager2.update_encryptor(k))
ciphertext2.append(manager2.finalize_encryptor())

# for c in ciphertext:
#     print("Recovered", manager.update_decryptor(c))
# print("Recovered", manager.finalize_decryptor())