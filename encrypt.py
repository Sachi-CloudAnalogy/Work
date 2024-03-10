# encrypt and decrypt text using a simple substitution cipher."

import string
import random

letters = string.ascii_letters
dict1 = {}
key = random.randint(1, 9)
print("key = ", key)

#encryption
for i in range(len(letters)):
    dict1[letters[i]] = letters[(i+key)%len(letters)]

plain_txt = input("Data to encrypt : ")
cipher_txt = []

for char in plain_txt:
    if char in letters:
        temp = dict1[char]
        cipher_txt.append(temp)
    else:
        temp = char
        cipher_txt.append(temp)

cipher_txt = "".join(cipher_txt)
print("Cipher Text : ", cipher_txt)

dict2 = {}

#decryption
for i in range(len(letters)):
    dict2[letters[i]] = letters[(i-key)%len(letters)]

decrypt_txt = []

for char in cipher_txt:
    if char in letters:
        temp = dict2[char]
        decrypt_txt.append(temp)
    else:
        temp = char
        decrypt_txt.append(temp)  

decrypt_txt = "".join(decrypt_txt)
print("Original Text : ", decrypt_txt)          