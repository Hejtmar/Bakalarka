import os, re
from matplotlib import pyplot as plt
from numpy import std, mean #std = standard deviation, mean = average

#get list of files in current directory
#files must start with "Tensile" and end with ".txt"
def giveMeDataFiles():
    filesList = [f for f in os.listdir('.')
                     if (os.path.isfile(f)
                         and f.startswith("Tensile") and f.endswith(".txt"))]
    return filesList


#function for evaluation of data, accepts raw string from the file
def evaluateData(fileName):
    dataList = (str(open(fileName, 'r').readlines())).split(r"\n")
    #clear unwanted chars in the list of strings
    forbiddenChars = ["[", "]", "'", " ", ","]
    clearData = []
    for element in dataList:
        for char in forbiddenChars:
            element = element.replace(char, "")
        clearData.append(str((element)[:-1:])) #append the string without last ; char
    #print(line, end = "\n\n")

    #make JSON dictionary
    valuesJSON = []
    lineCount = 0
    for element in clearData:
        testSpecimenData = element.split(";")
        if len(testSpecimenData) != 5:
            continue
            #exit function and return?
        lineCount += 1
        #invalid line
        valuesDictionary = {"date":testSpecimenData[0],
                        "strength":float(testSpecimenData[3]),
                        "force":float(testSpecimenData[2])}
        valuesJSON.append(valuesDictionary)
        
    strengthValues = []
    for element in valuesJSON:
        strengthValues.append(element["strength"])
    forceValues = []
    for element in valuesJSON:
        forceValues.append(element["force"])

    resultsFileName = "Evaluation_%s" %fileName
    with open(resultsFileName, "w") as file:
        file.write("""Source file name:\t%s
Number of tests:\t%d
Average strength:\t%.2f MPA
Standard deviation:\t%.2f MPA\n"""
                    %(fileName, lineCount, mean(strengthValues), std(strengthValues)))
        print("Data written to file %s!" %resultsFileName)
#actual programm
filesList = giveMeDataFiles()

#print the list of files found in current directory
print("Files found in current dericterory: ")
for file in filesList:
    print(file, end = "\n")
#
#
#
#get the data from the file into single string
for fileName in filesList:
    evaluateData(fileName)
