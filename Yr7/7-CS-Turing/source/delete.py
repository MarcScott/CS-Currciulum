prime = False
number = input('Give me a number')

while prime == False:
    divisor = number -1
    while divisor > 1:
        if prime % divisor != 0:
            divisor = divisor - 1
        
