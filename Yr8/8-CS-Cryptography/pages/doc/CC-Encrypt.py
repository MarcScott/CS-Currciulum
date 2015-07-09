trueAlphabet = 'abcdefghijklmnopqrstuvwxyz'
shiftedAlphabet = 'defghijklmnopqrstuvwxyzabc'
plainText = 'lajeuc ajwnx, ignore those first two words they are just there to confuse a cracker. anyway the secret message is, nobody expects the spanish inquisition'
cipherText = ''

for letter in plainText:
    if letter not in trueAlphabet:
        shiftedLetter = letter
    else:
        position = trueAlphabet.index(letter)
        shiftedLetter = shiftedAlphabet[position]
    cipherText = cipherText + shiftedLetter
print(cipherText)
