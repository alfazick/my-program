""" List is useful when you try to keep data in a structure,
so your program is much more flexible in processing the data
than it would be with several repetitive variables"""

catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames)+1)
    +
    '(Or enter print to stop.):')
    name = input()
    if name == 'print':
        break
    catNames = catNames + [name]
print('The cat names are: ')
for name in catNames:
    print(' ' + name)
