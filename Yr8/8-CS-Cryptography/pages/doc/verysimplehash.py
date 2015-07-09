alphabet = 'abcdefghijklmnopqrstuvwxyz'
alphadict = {}
count = 0
for i in alphabet:
    alphadict[i]=count
    count+=1
numString=''
for i in 'h0rs3batt3rystapl3':
    if i in alphadict:
        numString+=str(alphadict[i])+' '
    else:
        numString+=i+' '

print(numString)
    
    
