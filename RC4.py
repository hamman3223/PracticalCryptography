import numpy as np

def KSA(key): #key-scheduling algorithm
    key_lenght = len(key)
    S = list(range(256))
    j = 0
    for i in range(256):
        j=(j + S[i] + key[i % key_lenght]) % 256
        S[i], S[j] = S[j], S[i]
    return S

def PRGA(S, n):
    i=0
    j=0
    key=[]

    while n > 0:
        n-=1
        i = (i+1) % 256
        j = (j+ S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S [ (S[i] + S[j])%256 ]
        key.append(K)
    return key

key_origin = 'myMom'
plaintext_origin = 'my mom cooks cool'
def preparing_key_array(S):  # Converting ASCII symbols to their decimal value
    return [ord(c) for c in S]

# Here we got workable key for subsequent proccsessing.
# Word 'Workable' means, that it got operational form (list of numbers)
key = preparing_key_array(key_origin)

#my IV or initialization vector
S=KSA(key)

key_stream = np.array(PRGA(S, len(plaintext_origin) ))

plaintext = np.array([ord(c) for c in plaintext_origin])

cipher = key_stream ^ plaintext
cipher_finished = cipher.astype(np.uint8).data.hex()

print(f'My message was -> {plaintext_origin} \nIt\'s turned into {cipher_finished} \nUsed key is {key_origin}  ' )


