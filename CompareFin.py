import csv
import json 
import math 
from decimal import *
#from ResearchAnna import Stamp
from Stamp2 import Stamps
#import Stamp
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

#This creates a csv file from a matrix. 
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

# This takes a single Json string and search for the stamps that we want and return an array
#this returns a list of the stamps with the info that stamps have and the last one has the counter. 
# The output is a list [Id,stamp,...,stamps,.., [b,#,r,#,w,#,c,#]]
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
				
			if feautures[6] == 'carbody_short.png':
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
	#print(ClassList)
	# for i in range(len(ClassList)):
	# 	print(ClassList[i].getAll())
	#the out put is a list of all the elements pluss the c
	ClassList.append(['b', Ballooncounter,'r',Rubberbandcounter,'w',Wheelcounter,'c',Carbodycounter])
	return ClassList

# This compares two stamps coordinates and if they are on top of each other it should give true.
def compare(stamp1, stamp2):

	x1stamp1 = stamp1.getCoordinates()[0]+1/2*stamp1.getWidth()
	x2stamp1 = stamp1.getCoordinates()[0]-1/2*stamp1.getWidth()
	x1stamp2 = stamp2.getCoordinates()[0]+1/2*stamp2.getWidth()
	x2stamp2 = stamp2.getCoordinates()[0]-1/2*stamp2.getWidth()
	y1stamp1 = stamp1.getCoordinates()[1]+1/2*stamp1.getHeight()
	y2stamp1 = stamp1.getCoordinates()[1]-1/2*stamp1.getHeight()
	y1stamp2 = stamp2.getCoordinates()[1]+1/2*stamp2.getHeight()
	y2stamp2 = stamp2.getCoordinates()[1]-1/2*stamp2.getHeight()
	if(x1stamp1<x1stamp2 and y1stamp1<y1stamp2 and x2stamp1<x2stamp2 and y2stamp1<y2stamp2):
		return True 
	else:
		return False 

#This analyzes a list of stamps of each Json string (the list of stamps of each one). It is designed to take the info from JsonCounter
#It uses 
def stampAnalyzer(listofstamps):
	# This gets the last value of  
	WC = listofstamps[len(listofstamps)-1][5]
	RC = listofstamps[len(listofstamps)-1][3]
	CC = listofstamps[len(listofstamps)-1][7]
	BC = listofstamps[len(listofstamps)-1][1]
	
	for i in range(len(listofstamps)-2):
		print(listofstamps[i+1])
		
		if(float(listofstamps[i+1].getCoordinates()[0]) < 0.0 or float(listofstamps[i+1].getCoordinates()[0]) > 800 or float(listofstamps[i+1].getCoordinates()[1]) > 600.0 or float(listofstamps[i+1].getCoordinates()[1]) <0.0):
			if(listofstamps[i+2].getName() == 'Wheel'):
				WC = WC - 1
			if(listofstamps[i+2].getName() == 'Balloon'):
				BC = BC - 1 
			if(listofstamps[i+2].getName() == 'Carbody'):
				CC = CC - 1 
			if(listofstamps[i+2].getName() == 'rubberband'):
				RC = RC - 1 
		else: 
			for o in range(len(listofstamps)-3):
				if(compare(listofstamps[i+2],listofstamps[o+3])):
					if(listofstamps[i+2].getName() == 'Wheel'):
						WC = WC - 1
					if(listofstamps[i+2].getName() == 'Balloon'):
						BC = BC - 1 
					if(listofstamps[i+2].getName() == 'Carbody'):
						CC = CC - 1 
					if(listofstamps[i+2].getName() == 'rubberband'):
						RC = RC - 1 


	Counter = [WC,RC,CC, BC]
	return Counter







# Makes and a matrix of values
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

GroupIdArray = csvReader('DrawData.csv', 14)
JstArray = csvReader("DrawData.csv",11)
JArray = JsonConverter(JstArray)
print(JsonStampCounter(JArray[4],2))
jCountArray =[]
for i in range(len(JArray)):
	jCountArray.append(stampAnalyzer(JsonStampCounter(JArray[i],GroupIdArray[i+1])))

MatTeach = ArrayMaker('Drawing Coding_AMS_Fall2015.EG.LA_160926.csv', [0,5,7])
#print(MatTeach)
#print(jCountArray)









