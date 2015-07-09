alphabet = 'abcdefghijklmnopqrstuvwxyz'
cipherText = '''odmhxf dmzqa, ljqruh wkrvh iluvw wzr zrugv wkhb duh mxvw wkhuh wr 
frqixvh d fudfnhu. dqbzdb wkh vhfuhw phvvdjh lv,
qrergb hashfwv wkh vsdqlvk lqtxlvlwlrq'''

for i in range(1,26):
    plainText = ''
    for letter in cipherText:
        if letter not in alphabet:
            shiftedLetter = letter
        else:
            position = alphabet.index(letter)
            shiftIndex = (position + i)
            shiftedLetter = alphabet[shiftIndex]
        plainText += shiftedLetter
    print('With a shift of',i,'the message is\n\n',plainText,'\n')
        
