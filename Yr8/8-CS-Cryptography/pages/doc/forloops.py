  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  cipherText = '''odmhxf dmzqa, ljqruh wkrvh iluvw wzr zrugv wkhb duh mxvw wkhuh wr 
  frqixvh d fudfnhu. dqbzdb wkh vhfuhw phvvdjh lv,
  qrergb hashfwv wkh vsdqlvk lqtxlvlwlrq'''

  for i in range(1,26):
      plainText = ''
      for letter in cipherText:
          index = alphabet.index(letter)
          shiftedLetter = alphabet[shiftIndex]
