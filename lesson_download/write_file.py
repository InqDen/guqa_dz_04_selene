f = open('examle.txt', 'w')
f.write('abc')
f.close()

f= open('examle.txt')
for row in f:
    print(row)

