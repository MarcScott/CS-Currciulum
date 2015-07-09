def backwards(plainText):
    cipherText = plainText[::-1]
    return cipherText

message = input('What is the message')
cipherText = backwards(message)

print(cipherText)
