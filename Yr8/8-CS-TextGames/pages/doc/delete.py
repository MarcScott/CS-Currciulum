items=['foo','bar','baz']

for i, item in enumerate(items):
    if i == len(items) - 1:
        print('and ' + item)
    else:
        print(item+',',end=" ")
