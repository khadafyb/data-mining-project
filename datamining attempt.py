import os
##file = open(r"C:\Users\khada\Desktop\mini_newsgroups\alt.atheism\51121", "rt")
##data = file.read()
##words=data.split()

##print("number of words is : ",len(words))
names= [ ]
def listdirs(rootdir):
    for file in os.listdir(rootdir):
        d = os.path.join(rootdir,file)
        if os.path.isdir(d):
            names.append(d)


rootdir=r"C:\Users\khada\Desktop\mini_newsgroups"
listdirs(rootdir)
print(*names,sep="\n")

