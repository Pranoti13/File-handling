'''f=open("abcd.txt","r")
f.seek(4)
print(f.read(10))

f.close()'''

data="all students are stupids"
f=open("student.txt","w")
f.write(data)
with open("student.txt","r+")as f:
    text=f.read()
    print(text)
    print("current cursor position:",f.tell())
    f.seek(17)
    print("current cursor position:",f.tell())
    f.write("gems!!!!")
    f.seek(0)
    text=f.read()
    print("data after modification:")
    print(text)
