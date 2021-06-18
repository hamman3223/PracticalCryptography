import string

def create_shift_substitutions(n):
    encoding = {}
    decoding = {}
    alphabet_size = len(string.ascii_uppercase)
    for i in range(alphabet_size):
        letter = string.ascii_uppercase[i]
        substr_letter = string.ascii_uppercase[(i+n)%alphabet_size]

        encoding[letter] = substr_letter
        decoding[substr_letter] = letter

    return encoding, decoding

encoding, decoding = create_shift_substitutions(3)

def encrypt(message, subst):
    return "".join(subst.get(x,x) for x in message)

def decrypt (message, subst):
    return encrypt(message,subst)

cipher = encrypt('HI MY NAME IS ERIC', encoding)
print (f'Our encrypted message: {cipher}')
print(f'Now we will decrypt the message: {decrypt(cipher, decoding)}')


def bruteforceattack(cipher):
    for i in range(len(string.ascii_uppercase)):
        encoding, decoding = create_shift_substitutions(i)
        print(f'{i} : {decrypt(cipher,decoding)}')

bruteforceattack(cipher)


