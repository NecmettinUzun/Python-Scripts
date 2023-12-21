# -*- coding: utf-8 -*-
import glob
import os

# for Queue implementation
import Queue

from threading import Thread

# kullanicinin girdigi kelimeyi dosyalarda ara ve gectigi butun satirlari dosya adi ile baska dosyaya yaz.

# get specific word from user
# 1- raw_input(): it takes exactly what is typed from the keyboard, convert it to String and return it to variable
# 2- input(): it takes value from the user and then evaluates the expression, it means Python automatically identifies --
# input type String, int , list

searchedWord = raw_input("Enter any word: ")
searched_location ="./*"

queue = Queue.Queue(maxsize=100)

print("Entered word: ", searchedWord, "type: ", type(searchedWord))

# list all files in the directory and read them step-by-step, check the word contains or not

#TODO, yalnız txt degil, diger uzantılı tum dosyalarda arasın

def write_search_result():
    try:
        # append exist file
        if (os.path.exists("./resultDir")) == False:
            os.mkdir("./resultDir")
        with open("./resultDir/resultFile.txt", "w") as fileRef:
            while True:
                str = queue.get()
                fileRef.write(str)
                queue.task_done()
            print ("Writing thread is finished")
            fileRef.close()

    except Exception as Exp:
        print("Exception during writing", Exp)


class fileOperation():

    def __init__(self):
        print("inside file operation")

    def search_word_in_file(self, file_name):
        try:
            with open(file_name, "r") as fileRef:
                for line in fileRef:
                    # search sub-string, if it find this, return index otherwise return -1
                    if line.find(searchedWord) != -1:
                        return line
            fileRef.close()
        except Exception as Exp:
            print("Exception during reading", Exp)


class searchOperation():
    def __init__(self):
        print ("inside search operation")

    def search_directory(self,searchLocation):
        listOfFiles = glob.glob(searchLocation)
        for file_name in listOfFiles:
            #print ("file_name",item_of_list)
            if os.path.isfile(file_name):
                if fileOp.search_word_in_file(file_name) != None:
                    lineContainsSearchWord= fileOp.search_word_in_file(file_name)
                    #fileOp.write_search_result(file_name, lineContainsSearchWord)
                    queue.put(file_name + "____" + lineContainsSearchWord + "\n")
            else:
                #print ("file_namee",item_of_list)
                self.search_directory(file_name+"/*")



fileOp = fileOperation()
T = Thread(target=write_search_result, args=())
T.daemon = True
T.start()
queue.join()

searchOp = searchOperation()
searchOp.search_directory(searched_location)


