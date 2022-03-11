#create zip file    f= ZipFile("files.zip","w","ZIP_DEFLATED")
from zipfile import*
f=ZipFile("files.zip",'w',ZIP_DEFLATED)
f.write("abc.txt")
f.write("abcd.txt")
f.write("abcde.txt")
f.close()
print("files.zip file created successfully")

#unzip operation               f = ZipFile("files.zip","r",ZIP_STORED)
from zipfile import*
f=ZipFile("files.zip",'r',ZIP_STORED)
names=f.namelist()
for name in names:
    print("file name:",name)
    print("the content of this file:")
    f1=open(name,'r')
    print(f1.read())
    print()

