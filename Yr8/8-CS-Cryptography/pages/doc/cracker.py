import hashlib
import binascii
hashedPassword=b'@K1$^M^J4K:^0H.\\&!<YXP&=$5FJ5RNJBFM?-=-Q=+7, \n'

with open('passwords.txt','r') as textFile:
        passwordList = textFile.read()

passwords = passwordList.split('\n')

hashlib.pbkdf2_hmac('sha256', b'password', b'', 1)

for password in passwords:
        hashed = hashlib.pbkdf2_hmac('sha256',bytes(password,'utf-8'),b'',1000)
        asciiHashed = binascii.b2a_uu(hashed)
        if asciiHashed == hashedPassword:
                print('Password is '+password)
                break
        

        
