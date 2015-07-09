secretNumber = 1

#Pick a prime number
prime1 = 23
#Pick another prime number
prime2 = 11
#Pick another prime number
prime3 = 7

publicKey = prime1*prime2, prime3

print('Your public key is',publicKey)

phi1 = prime1-1
phi2 = prime2-1

for d in range(1,phi1*phi2):
    if (d * prime3)%(phi1 * phi2) == 1:
        privateKey = prime1*prime2,d
        break


print('Your private key is',privateKey)
    
cipherText = (secretNumber**publicKey[1])%publicKey[0]
plainText = (cipherText**privateKey[1])%privateKey[0]

print(cipherText)
print(plainText)

