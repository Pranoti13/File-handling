#tell()=return current position of curso    r

f=open("abcd.txt","r")
print(f.tell())
print(f.read(2))
print(f.tell())
print(f.read(3))
print(f.tell())