#to read data line by line

'''f=open("abcde.txt",'r')
line1=f.readline()
print(line1,end=" ")
line2=f.readline()
print(line2,end=" ")
line3=f.readline()
print(line3,end=" ")
f.close()'''

#to read all lines into list
'''f=open("abcde.txt",'r')
lines=f.readlines()
for line in lines:
    print(line,end="")
f.close()'''

f=open("abcde.txt",'r')
print(f.read(3))
print(f.readline())
print(f.read(4))
print("remaining data")
print(f.read())
f.close()

