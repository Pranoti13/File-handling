#current working directory(cwd)
'''import os
cwd=os.getcwd()
print("current working directory:",cwd)
'''
#create sub directory in the current working directory
'''import os
os.mkdir("mysub")
print("mysub directory created in cwd")
'''
#create sub directory in mysub directory
'''import os
os.mkdir("mysub/mysub2")
print("mysub2 created inside mysub")
'''
#create multiple directories
'''import os
os.makedirs("sub1/sub/sub3")
print("sub1 and in that sub2 and in that sub3 directories created")
'''
#remove directory
'''import os
os.rmdir("mysub/mysub2")
print("mysub2 directory deleted")'''

#remove multiple directories in the path
'''import os
os.removedirs("sub1/sub2/sub3")
print("all 3 directories sub1,sub2 and sub3 removed")'''

#rename directory
'''import os
os.rename("mysub","newdir")
print("mysub directory renamed to newdir")
'''
#contents of directory
import os
print(os.listdir("."))      #this program display contents of current working directory but not contents of sub directory

#if we want the content of a directory including sub directories then we should go for walk()fun

#content of directory including sub directories
#os.walk(path,topdown=True,onerror=None,followlinks=False)

#to display all contents of current working directory including sub directories

import os
for dirpath,dirnames,filenames in os.walk('.'):
    print("current directory path",dirpath)
    print("directions:",dirnames)
    print("files:",filenames)
    print()

#display perticular directory

#os.walk("directoryname")

#running other program from python

import os
os.system("dir*.py")
os.system("py abcd.py")





