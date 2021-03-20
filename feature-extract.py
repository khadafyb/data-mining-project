#Hannibal Santiago
#Khadafy Bilal
#Data Minnig Project 1

#imports
import os
import _pickle as pickle
import numpy as np
from nltk.stem import SnowballStemmer
import math

folderpath=r"D:\my_data"
folder="C:/Users/hanfs/Desktop/data-mining-project/mini_newsgroups"
punc = '''1234567890!()-[]{};:'"\, <>./=?@#|$%^&*_~'''
stopwords=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
stemmer = SnowballStemmer("english")


## loading data and preprocessing
##alldocuments = []
##iterate the directories
##   for each file 
##      open the file and use readlines() to read all lines
##      fetch the lines related to "Subject" and the body started with "Lines: number"
##      preprocessing the lines and convert them to terms
##      collect terms and add to a dictionary of {term: term-frequency}
##      put all document related information into a list ["subdirectory", {term: term-frequency, term:term-freq, ...}] (or other structures you like)
##      append the list to the alldocuments

##Do this part Here
alldocs =[]
filepaths = [folder+'/'+name for name in os.listdir(folder)]
#print(filepaths)
all_files=[] #not sure why this
yes_lines= False
for subdir in filepaths: ##i is the subdirectories, the folders within the folder
    #print(subdir)
    morepaths = [os.path.join(subdir, name) for name in os.listdir(subdir)]
    for path in morepaths:
        #print(subdir)
        with open(path, 'r') as f:
            file = f.readlines()
            lc= 0 #line counter
            needed_data= ""
            yes_lines=False
            for line in file:
                
                if (line[0:7]=="Subject"): #look for the line that has "Subject" and return the contents in that line
                    #line[12:len(line)-1] will be the rest of the lines we need for subject minus the /n
                    #print(line[9:len(line)-1]) #returns the whole line Re:.... and removes the /n
                    needed_data= needed_data + line[9:len(line)-1] 
                    
                if (line[0:5]=="Lines"):
                    #looking for the number that follows so we can look for those
                    #the integer should be returned
                    #print(line)
                    #print(file)#this is not working as it should, I want to check that when it is casted that it is an int
                    yes_lines=True
                    try:
                        number = int(line[7:len(line)-1])#this shows us the the number (doesn't import the new line element)
                    except:
                        number=0
                        needed_data=""
                        yes_lines=False
                    if(yes_lines==True):
                        
                        #print(number) #works: finds the number, then uses it below
                        nlc=lc #new line counter
                        for l in file[lc:len(file)]:
                            if (l[0] == '\n'):
                                nlc=nlc+1
                                for each_line in file[nlc:number+nlc]:
                                    #print(each_line[0:len(each_line)-1])#works now too, we will need to append this all to a larger string and process that string
                                    needed_data= needed_data + each_line[0:len(each_line)-1] + " "
                                break
                            else:
                                nlc = nlc+1
                lc= lc +1

            ##add in the line Lines: XX if boolean is still false

                
            if(yes_lines==True):
            
                #print(needed_data) #works, contains all the data needed
                words = needed_data.split(" ") #make an array
                #print(words) working so far we are good here
                
                wording_ctr=0 #counter
                
                for element in words:
                    wording=""
                    for char in element:
                        if char in punc:
                            wording=wording + ""
                        else:
                            wording=wording+char
                    fixed=wording.lower()
                    help1=fixed.rstrip('\t',)
                    help2=help1.rstrip('\t')
                    fixed_again=help2.rstrip('\r')
                    
                    #print(fixed) works here
                    for a in stopwords:
                        if(fixed_again==a):
                            fixed_again=""
                    #if(fixed == stpwrd for stpwrd in stopwords): #something is wrong with this
                    #    fixed=""
                    #print(fixed) works here now as well
                    words[wording_ctr]=fixed_again
                    wording_ctr= wording_ctr+1
                #print(words) works here now as well
                i =0
                while(i<10):
                    for e in words:
                        if (e==""):
                            words.remove(e)
                    i=i+1
                    
                #print(words) #should be good now, seems to work

                
                terming=[]
                for e in words:
                    stemmed=stemmer.stem(e)
                    terming.append(stemmed)
                #print(terming) #working so far!!
                #print(terming)

                #this is getting the count of i for us in the terming list
                termfreq={}
                for i in terming: #this is now adding the term and it's frequency to a dictionary
                    if i not in termfreq:
                        termfreq[i]=terming.count(i)
                        #print("adding")

                #print(termfreq) #this works!!
                #print(subdir)
                #subdictionary = subdir #need the folder that the files lay in 

                bigger_list=[subdir[len(folder)+1:len(subdir)],termfreq] #gets a list with the name sent and the dictionary created and sent in this is subdir

                ##I need to now sent in the bigger_list to the alldoc[]
                alldocs.append(bigger_list)
            #else:
                ##Do the function of writing "Lines: XX" into the file, do this for last step
            
#print(alldocs) #this works as it is meant to YES
######

##getting term dictionary and document frequency
##term-dict = {}
##term-doc-freq = {} # document-frequency
##iterate alldocuments:
##   for each document:
##      for each term in the term:term-freq dictionary of the document structure
##          if it's not in term-dict
##          	add the term to term-dict, with default feature-id set to 0
##          if not in term-doc-freq
##          	term-doc-freq [term] = 1
##          else
##            term-doc-freq[term] += 1

##Do this part here
termdict = {}
termdocfreq = {}
#print(alldocs[1])
for doc in alldocs:
    #print(i[1]) this gets the data I need and am looking for [name, term-freq]

    #termlist = pairing[1].keys()

    for term in doc[1]:
        #print(term)
        if term not in termdict:
            termdict[term]=0
        if term not in termdocfreq:
            termdocfreq[term]=1
        else:
            termdocfreq[term] +=1

######

##assign feature id
##get all keys from term-dict and sort them
##feature-id =0 
##for each key in sorted keys
##   term-dict[key] = feature-id
##   feature-id +=1

##Do this part here
#print(termdict)
termdict.keys() #now a list so sort this
dictkeys=sorted(termdict)
feature_id=0
for key in dictkeys:
    termdict[key]= feature_id #interested on how the data is written on the dictionary
    feature_id +=1

#####


#class-dict ={}
#create the dictionary for subdirectory -> class id

##Do this part here
class_dict={
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
            "talk.religion.misc":5,
            "alt.atheism":5,
            "soc.religion.christian":5
} 

#print(class_dict)

#####


##generating the training data file(s)
##iterate alldocuments:
##for each document:
##   find the class-id with class-dict["subdirectory"] of the document
##   for each term in the last part:
##   	 use term-dict[term] to find the feature id
##   put all information to the output string and write to the training data file
##   you can also generate other files with all the information ready

##Do this part here Made 3 of the 4 training data information, So I won't do all the task 2 and 3 stuff
#print(class_dict)
#print(len(alldocs))
f1 = open("training_data_file.TF.txt", "w")
f2 = open("training_data_file.IDF.txt", "w")
f3 = open("training_data_file.TFIDF.txt", "w")
f4 = open("training_data_file.Boolean.txt","w")
#print(termfreq)
for doc in alldocs:
    #print(doc)
    #doc[1] == termfreq dict
    
    class_id=(class_dict[doc[0]])
    tf = str(class_id)
    idf = str(class_id)
    tfidf = str(class_id)
    boolean = str(class_id)
    #termlist = i[1].keys()
    #print(doc[1])
    #print(len(doc[1]))
    sortdoc=sorted(doc[1])
    for term in sortdoc:
        x=(doc[1][term]/len(doc[1]))
        y=( math.log( (len(alldocs) / termdocfreq[term]) , 10))
        z=x*y
        tf = tf +" "+ str(termdict[term])+":"+ str(x) #get the value at term
        idf = idf +" "+ str(termdict[term])+":" + str(y)
        tfidf = tfidf + " " + str(termdict[term])+":"+ str(z)
        
        boolean = boolean + " " + str(termdict[term])+":1"
        
    #print(tf) #we finally generated the file, make sure we write this string down
    f1.write(tf+ '\n')
    f2.write(idf + '\n')
    f3.write(tfidf + '\n')
    f4.write(boolean + '\n')

f1.close()
f2.close()
f3.close()
f4.close()
        

####

##write class definition
##iterate class-dict:
## write each (subdirectory, classid) pair to class-definition file
f5 = open("class-definition-file", "w")
for label in class_dict:
    f5.write(str(label) + ":" + str(class_dict[label])+ '\n')
f5.close()
    
##Do this part here


####


##write feature definition
##iterate term-dict
##  write each (term, feature id) pair to feature definition file

##Do this part here
f6=open("feature-definition-file", "w")

for term in termdict:
    f6.write(str(term)+":" +str(termdict[term]) + '\n')
f6.close()


#####
