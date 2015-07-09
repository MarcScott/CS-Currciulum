trueAlphabet = 'abcdefghijklmnopqrstuvwxyz'
shiftedAlphabet = 'defghijklmnoqprstuvwxyzabc'
plainText = 'hello world'
cipherText = ''

for i in plainText:
    position = trueAlphabet.index(i)
    cipherChar = shiftedAlphabet[position]
    cipherText = cipherText + cipherChar

print(cipherText)
    
