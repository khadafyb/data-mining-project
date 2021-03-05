import os
import _pickle as pickle
##file = open(r"C:\Users\khada\Desktop\mini_newsgroups\alt.atheism\51121", "rt")
##data = file.read()
##words=data.split()

##print("number of words is : ",len(words))
#names= [ ]
##def listdirs(rootdir):
##    for file in os.listdir(rootdir):
##        d = os.path.join(rootdir,file)
##        if os.path.isdir(d):
##            names.append(d)
##
##
##rootdir=r"C:\Users\khada\Desktop\mini_newsgroups"
##listdirs(rootdir)
##print(*names,sep="\n")


class_definition_file={
            "comp.graphics":0,
            "comp.os.ms-windows.misc":0,
            "comp.sys.ibm.pc.hardware":0,
            "comp.sys.mac.hardware":0,
            "comp.windows.x":0,
            "rec.autos":1,
            "rec.motorcycles":1,
            "rec.sport.baseball":1,
            "rec.sport.hockey":1,
            "sci.crypt":2,
            "sci.electronics":2,
            "sci.med":2,
            "sci.space":2,
            "misc.forsale":3,
            "talk.politics.misc":4,
            "talk.politics.guns":4,
            "talk.politics.mideast":4,
            "talk.religion.mis":5,
            "alt.atheism":5,
            "soc.religion.christian":5
        }
f = open("class_definition_file", "w")
data=str(class_definition_file)
f.write(data)
#could modify this document and what gets sent here from the str parse to remove the brackets
f.close()
f=open("class_definition_file","r")
print(f.read())
f.close()



folderpath=r"D:\my_data"
folder= "C:/Users/hanfs/Desktop/data-mining-project/mini_newsgroups"

filepaths = [folder+'/'+name for name in os.listdir("C:/Users/hanfs/Desktop/data-mining-project/mini_newsgroups")]
all_files=[]


for i in filepaths:
    morepaths = [os.path.join(i, name) for name in os.listdir(i)]

    for path in morepaths:
        with open(path, 'r') as f:
            file = f.readlines()
            for line in file:
                #print(line)
                for word in line:
                    break
#now we can create that bag of words and check for words as well, do the split here
#print the dictionary created on one single document
##we need to find a way to create the training documents

#print("done")
