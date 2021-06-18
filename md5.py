import os
import hashlib

def get_hash_value(path_to_file):
    files_descriptor = open(path_to_file,'rb')
    file_entity = files_descriptor.read()
    decoded_file = hashlib.sha256(file_entity)
    return decoded_file.hexdigest()

print(get_hash_value('/Users/erickostandyan/Desktop/qwerty3223.ovpn'))