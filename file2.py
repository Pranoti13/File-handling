#file1.py=abcd.txt file  read in file2
#read total data from thr file
'''f=open("abcd.txt",'r')
data=f.read()
print(data)
f.close()'''

#to read only 1st 10 characters
f=open("abcd.txt",'r')
data=f.read(10)
print(data)
f.close()