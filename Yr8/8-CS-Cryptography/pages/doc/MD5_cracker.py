import hashlib

hashedPassword='2b058ab133ff919bb39ebf7ceb1c13e5'

with open('passwords.txt','r') as textFile:
        passwordList = textFile.read()

passwords = passwordList.split('\n')
for password in passwords:
        hashed = hashlib.md5(password.encode('utf-8')).hexdigest()
        if hashed == hashedPassword:
                print('Password is '+password)
                break
        

        
