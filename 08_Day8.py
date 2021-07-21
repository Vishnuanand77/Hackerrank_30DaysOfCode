# Day 8 : Dictionaries and Maps

phonebook = {}
entries = int(input())

#Using try-except to catch any errors
for n in range(entries):
    name, num = input().strip().split(' ')
    name, num = [str(name), int(num)]
    phonebook[name] = num

while True:
    try:  
        search = str(input())

        if search in phonebook:
            output = ''.join('%s=%r' % (search, phonebook[search]))
            print(output) 
        else:
            print("Not found")
    except EOFError:
        break
