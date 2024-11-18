firstfile - input("Enter the name of the 1st file")
secondfile - input("Enter the name of 2nd file")

f1 = open(firstfile,'r')
f2 = open(secondfile,'r')

print('content of the first file before appending -\n', f1.read())
print('content of the second file before appending -\n', f2.read())

f1.close()
f2.close()

f1.open(firstfile, 'a+')
f2.open(secondfile, 'r')

f1.write(f2.read())

f1.seek(0)
f2.seek(0)

print('content of the first file after appending -\n', f1.read())
print('content of the second file after appending -\n', f2.read())

f1.close()
f2.close()