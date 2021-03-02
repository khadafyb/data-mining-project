#imports

#We need to create dictionaries, token:entry_number, classname:class_id_number(label)

#open the unzipped file = "mini_newsgroups"

#files = [file for file in PATH()]
#   for file_name in files:
#       with io.open(file_name, 'r') as name:
#           content=name.read()

#Loop: we need to open each folder (newgroup names), and the read each document within the newsgroups



    int counter_id=0 #this is the counter used for the id_number and this gets manipulated for each document
    #Loop: Read each document and do this loop for each document


        #create tokens and assign value (bag of terms and index number)
            #while creating the bag of terms remove the stopwords and stem the bag of words to yield the token
                #produce file named "feature_definition_file" and it is the information from the Loop of Tokens
                #each document is one row and contains terms and their associated id number, so one big output

        #when a new word is ready to become a token add to this dictionary
        feature_definition_file={

        }
        #feature_definition_file.update({"token": counter_id})
        counter_id++

#assign newsgroup names a class value 20:6
    #make the file named "class_definition_file" that uses the information from the dictionary
        class_definition_file={
            "comp.graphics":0,
            "comp.os.ms-windows.misc":0,
            "comp.sys.ibm.pc.hardware":0,
            "comp.sys.mac.hardware":0,
            "comp.windows.x":0;
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

        
#have code that produces that training_data_file.TD/IDF/TFIDF
    #it should use the be all 3 produced with the information given from above (not sure where this should be in the loop
