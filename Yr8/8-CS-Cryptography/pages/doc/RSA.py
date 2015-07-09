import fractions
import random

def calcKeyPairs(p1,p2,p3):
    result = p1*p2
    totient = phi(result)
    d = calcMod(p3,totient)
    print('Your private key is ',result,' and ',d)
    print('Your public key is ',result,'and',p3)
    return result,d

def phi(n):
    amount = 0
    for k in range(1, n + 1):
        if fractions.gcd(n, k) == 1:
            amount += 1
    return amount

def calcMod(p3,totient):
    d = 0
    for k in range(1,totient):
        if ((k * totient)  + 1)%p3 == 0:
            d = ((k * totient)  + 1)/p3
            return int(d)

def encrypt(pub1,pub2,message):
    return((message**pub2)%pub1)

def decrypt(pri1,pri2,message):
    return((message**pri2)%pri1)

def stringToInt(string):
    bytes = string.encode('utf-8')
    integer = int.from_bytes(bytes,'little')
    return integer

def intToString(integer):
    bytes = integer.to_bytes(2048,'little')
    text = (bytes.decode('utf-8').rstrip("\x00"))
    return text

def is_prime(num):
    if num == 0 or num == 1:
        return False
    for x in range(2, num):
        if num % x == 0:
            return False
    else:
        return True

def getPrime(potPrime):
    while is_prime(potPrime) == False:
        potPrime += 1
    return potPrime

#prime1 = getPrime(random.randint(10,100))
#prime2 = getPrime(random.randint(10,100))
#prime3 = getPrime(random.randint(2,50))

p1 = getPrime(random.randint(100,1000))
p2 = getPrime(random.randint(100,1000))
p3 = getPrime(random.randint(10,20))
print('Got Primes')


result,d = calcKeyPairs(p1,p2,p3)
plainText = 'a'
plainInt = stringToInt(plainText)
print('Integer to encrypt = ',plainInt)
cipherInt = encrypt(result,p3,plainInt)
print('Encrypted integer = ',cipherInt)
plainInt = decrypt(result,d,cipherInt)
print('Decrypted Integer = ',plainInt)
plainText = intToString(plainInt)
print('Decrypted Text =',plainText)
