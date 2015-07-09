import hashlib
with open('passwords.txt','r') as f:
    passwords = f.read()
    passwords = passwords.split()

count = 0
for password in passwords:
    count += 1
    hashlib.md5(password.encode('utf-8')).hexdigest()
print(count)
