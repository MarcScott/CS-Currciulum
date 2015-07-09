pb1 = int(input('Public Key Part 1: '))
pb2 = int(input('Public Key Part 2: '))
plainText = input('Lowercase message (a-z only): ')
alpha = 'abcdefghijklmnopqrstuvwxyz'
cipherText = ''
for letter in plainText:
    value = alpha.index(letter)+1
    cipher = (value**pb2)%pb1
    cipherText += str(cipher)+','
print(cipherText)


