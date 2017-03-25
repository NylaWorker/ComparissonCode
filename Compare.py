import csv
import json 
import math 
from decimal import *
#from ResearchAnna import Stamp
from Stamp2 import Stamps
#This functions takes the csv file and goes to the row with the desired information,then this will return an 
#array with json strings.
def csvReader(File, rowWanted):
	dataFile = open(File)
	readData = csv.reader(dataFile)
	JsonStArray = []
	for row in readData:
		JsonStArray.append(row[rowWanted])
	dataFile.close()
	return JsonStArray
#Creates a csv file
def csvPrinter(Matrix, nameFile):
	writer = csv.writer(open(nameFile, 'w'), delimiter = ',')
	for x in range(len(Matrix)):
		try:
			writer.writerow(Matrix[x])
		except IndexError:
			print('Oh No')

#This takes in an array of strings and convert the strings to Jsons, if possible. 
def JsonConverter(JsonStArray):
	count = 0 
	JsonArray = []
	for i in range(len(JsonStArray)-1):
		#If any value in the inserted array is checked to see if it is a json.
		try:
			js = json.loads(JsonStArray[i+1])
			js2 = json.loads(js["drawData"])
			JsonArray.append(js2['canvas']['objects'])
		except ValueError:
			#In order to mess up the order of the Jsonarray I plug an empty dictionary 
			JsonArray.append({})
	#print(count) 
	return(JsonArray)


def JsonStampCounter(SingleJson,Id):
	Wheelcounter = 0
	Carbodycounter = 0
	Ballooncounter = 0
	Rubberbandcounter = 0
	#This class list has all stamps in the images with the things you can find in the stamp class. 
	ClassList= [Id]
	order = 0
	keyErr = 0 
	for i in range(len(SingleJson)):
		try:
			src = SingleJson[i]['src']
			jsT = float(SingleJson[i]['top'])
			jsL = float(SingleJson[i]['left'])
			#scale of the width fix..!!!

			jsH = float(SingleJson[i]['scaleY'])* float(SingleJson[i]['height'])
			jsW = float(SingleJson[i]['scaleX'])* float(SingleJson[i]['width'])
			
			#I split the string with the link in order to be able to check what stamp is being used. 
			feautures = src.split('/')
			if feautures[6] == 'Wheel.png':
				Wheelcounter = Wheelcounter + 1
				order += 1 
				ClassList.append(Stamps('Wheel',[jsL,jsT],jsH,jsW,order))
				
			if feautures[6] == 'carbody_short.png' or feautures[6] == 'carbody_long.png':
				Carbodycounter = Carbodycounter + 1
				order += 1 
				ClassList.append(Stamps('Carbody',[jsL,jsT],jsH,jsW,order))
				
			if feautures[6] == 'Balloon.png':
				Ballooncounter = Ballooncounter + 1
				order += 1 
				ClassList.append(Stamps('Balloon',[jsL,jsT],jsH,jsW,order))
				
			if feautures[6] == 'rubberband.png':
				Rubberbandcounter = Rubberbandcounter+ 1
				order += 1 
				ClassList.append(Stamps('rubberband',[jsL,jsT],jsH,jsW,order))

		except KeyError:
			keyErr = keyErr + 1
	# print(ClassList[0])

	# for i in range(len(ClassList)-1):
	# 	print(ClassList[i+1].getAll())
	#the out put is a list of all the elements pluss the c
	ClassList.append(['b', Ballooncounter,'r',Rubberbandcounter,'w',Wheelcounter,'c',Carbodycounter])
	# print(ClassList[len(ClassList)-1])
	return ClassList

JstArray = csvReader("DrawData.csv",11)
JArray = JsonConverter(JstArray)
mat=JsonStampCounter(JArray[4],2)
GroupIdArray = csvReader('DrawData.csv', 14)
jCountArray =[]
#this creates an array with all the json strings. 
for i in range(len(JArray)):
	jCountArray.append(JsonStampCounter(JArray[i],GroupIdArray[i+1]))

#rows colums 0,5,7  only wheels and carbodies. This creates an array from a csv file with any list of desired rows 
def ArrayMaker(CsvFileToberead, listOfRows):
	dataFile = open(CsvFileToberead)
	readData = csv.reader(dataFile)
	JsonStArray = []
	for row in readData:
		tempArr = []
		for x in range(len(listOfRows)):
			tempArr.append(row[listOfRows[x]])
		JsonStArray.append(tempArr)
	dataFile.close()
	return JsonStArray
MatTeach = ArrayMaker('Drawing Coding_AMS_Fall2015.EG.LA_160926.csv', [0,5,7])


#ompares both the teacher and my values. 
def stampComparator(ArrayStamps, TeacherArray):
	ArrayBecsved = [["GroupArray", 'wheels', 'wheels Nyla', 'carbody', 'carbody Nyla']]
	for i in range(len(ArrayStamps)):
		for x in range(len(TeacherArray)-1):
			tempArr = []
			#The first line of teacher array are the names of the objects. 
			if TeacherArray[x + 1][0] ==  ArrayStamps[i][0]:
				#tempArr.append([TeacherArray[x + 1][0],TeacherArray[x + 1][1],ArrayStamps[i][len(ArrayStamps[i])-1][5],TeacherArray[x + 1][2],ArrayStamps[i][len(ArrayStamps[i])-1][7]])
				ArrayBecsved.append([TeacherArray[x + 1][0],TeacherArray[x + 1][1],ArrayStamps[i][len(ArrayStamps[i])-1][5],TeacherArray[x + 1][2],ArrayStamps[i][len(ArrayStamps[i])-1][7]])
	return ArrayBecsved 
print(stampComparator(jCountArray,MatTeach))
print(jCountArray[1][0])
csvPrinter( stampComparator(jCountArray,MatTeach),'new.csv')




