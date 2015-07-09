def getFile(textfile):
    with open(textfile,'r') as f:
        data = f.read()
    return data

def splitData(data):
    data = data.split()
    data = [i.strip() for i in data]
    return data


data = getFile('passwords.txt')
data = splitData(data)
print('DATA')
print(data)
frequency = data[1::4]
frequency = [int(i) for i in frequency]
print('FREQ')
print(frequency)
passwords = data[3::4]
passwords = [i.rstrip() for i in passwords]
print(passwords)

with open('biglist.txt','w') as f:
    for i in range(0,len(passwords)):
        f.write(frequency[i]//1000*(passwords[i]+' '))
                
