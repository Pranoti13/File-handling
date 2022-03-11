s=input("enter some string")
i=0
l=len(s)
print(l)
for i in len(s):
    print("the char present at positive index",i,"and negative index",i-s,"is",s[i])
    i=i+1