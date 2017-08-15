import os, re
from matplotlib import pyplot as plt
from numpy import std, mean #std = standard deviation, mean = average


def getGripDistance():
    gripDistance = input("Zadej vzdalenost mezi celistmi")
    try:
        gripDistance =
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
                        "force":float(testSpecimenData[2]),
                        "elongation":float(float(testSpecimenData[4])/gripDistance*100)}
        """elongation in %, max force in kN, strength in MPa"""
        valuesJSON.append(valuesDictionary)
        
    strengthValues = []
    for element in valuesJSON:
        strengthValues.append(element["strength"])
    forceValues = []
    for element in valuesJSON:
        forceValues.append(element["force"])
    elongationValues = []
    for element in valuesJSON:
        elongationValues.append(element["elongation"])
        
    resultsFileName = "Evaluation_%s" %fileName
    with open(resultsFileName, "w") as file:
        file.write("""Source file name:\t%s
Number of tests:\t%d
Maximal force:\t\t%.2f +- %.2fkN
Average strength:\t%.2f +- %.2f MPA
Average elongation:\t%.2f +/ %.2f"""
                    %(fileName, lineCount,
                      mean(forceValues), std(forceValues),
                      mean(strengthValues), std(strengthValues),
                      mean(elongationValues), std(elongationValues)))
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
