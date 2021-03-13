import os
import _pickle as pickle


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
f.write(data[1:len(data)-1])

f.close()


folderpath=r"D:\my_data"
folder= "C:/Users/hanfs/Desktop/data-mining-project/mini_newsgroups"

filepaths = [folder+'/'+name for name in os.listdir(folder)]
all_files=[]


# initializing punctuations string  
punc = '''!()-[]{};:'"\, <>./?@#|$%^&*_~'''

nltk=["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

#this whole loop allows us to open each folder within the larger directory, and then to create dictionaries for each
for i in filepaths:
    morepaths = [os.path.join(i, name) for name in os.listdir(i)]
    #we should look to see when i is equal to the above directory to then print it's ID number onto the tidy files
    for path in morepaths:
        with open(path, 'r') as f:
            file = f.readlines()
            #we are now exploring lines within the file
            for line in file:

                words = ""
                #checking each word in the line and we are creating a string that removes the punctuation
                for element in line:
                    if element in punc:
                       words = words + " "
                    else:
                        words = words + element
                word = words.rstrip("\n")
                word = word.lower()
                word = word.split(" ")

                #after spliting at spaces we are running both of these loops to remove empty lists within the larger list (which is the line) and the stop words but for some reason it has to be done multiple times
                i=0
                while i<10:
                    for element in word:
                        if element == '':
                            word.remove(element)
                        for a in nltk:
                            if element == a:
                                word.remove(element)
                    i = i+1
                
                #now that all blanks within the list are removed we need to stem, then after stemming we then create the bag of words
                    
                print(word)

                
                

print("done")
