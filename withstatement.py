#with statement
'''with open("abcd.txt","w")as f:
    f.write("durga\n")
    f.write("software\n")
    f.write("solution\n")
    print("is file closed:",f.closed)
print("is file closed:",f.closed)'''

with open ("abcd.txt","r")as f:
    data=f.read()
    print(data)
    print(f.closed)
print(f.closed)