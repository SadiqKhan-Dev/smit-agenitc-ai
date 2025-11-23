
# list

# thislist = ['apple', 'banana', 'cherry', 'apple', 'cherry']
# print(thislist)
# print(len(thislist))
# print(thislist[1])
# print(thislist[-1])
# print(thislist[2:5])


thislist = ['apple', 'banana', 'cherry', 'apple', 'cherry']
thislist[1] = 'blackcurrant'
print(thislist)

thislist[1:3] = ['blackcurrant', 'watermelon']
print(thislist)

thistuple = ('kiwi', 'orange')
thislist.extend(thistuple)
print(thislist)