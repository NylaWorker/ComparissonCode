import csv
import json 
import math 
from decimal import *
#from ResearchAnna import Stamp
from Stamp2 import Stamps
#import Stamp
#simple functions to calculate the distance and the area
def distanceCalc(coord1,coord2):
	distance = ((int(coord1[0])-int(coord2[0]))**2 +(int(coord1[1])-int(coord2[1]))**2)**(1/2.0)
	return distance
def area(height,width,param):#param has to determine whether it should calculate the area as a oval or as a box
	if param == 'c':
		area = height/2.0*width/2.0*math.pi
		return area
	if param != 'c': 
		area = height*width
		return area 
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
	
	return(JsonArray)

# This takes a single Json string and search for the stamps that we want and return an array
#this returns a list of the stamps with the info that stamps have and the last one has the counter. 
def JsonStampCounter(SingleJson):
	Wheelcounter = 0
	Carbodycounter = 0
	Ballooncounter = 0
	Rubberbandcounter = 0
	#This class list has all stamps in the images with the things you can find in the stamp class. 
	ClassList= []
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
	
	#the out put is a list of all the elements pluss the c
	ClassList.append(['b', Ballooncounter,'r',Rubberbandcounter,'w',Wheelcounter,'c',Carbodycounter])
	return ClassList


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



def stampAnalyzer(listofstamps):
	WC = listofstamps[len(listofstamps)-1][5]
	RC = listofstamps[len(listofstamps)-1][3]
	CC = listofstamps[len(listofstamps)-1][7]
	BC = listofstamps[len(listofstamps)-1][1]
	
	for i in range(len(listofstamps)-2):
		
		if(float(listofstamps[i].getCoordinates()[0]) < 0 or int(listofstamps[i].getCoordinates()[0]) > 800 or int(listofstamps[i].getCoordinates()[1]) > 600 or int(listofstamps[i].getCoordinates()[1]) <0):
			if(listofstamps[i+1].getName() == 'Wheel'):
				WC = WC - 1
			if(listofstamps[i+1].getName() == 'Balloon'):
				BC = BC - 1 
			if(listofstamps[i+1].getName() == 'Carbody'):
				CC = CC - 1 
			if(listofstamps[i+1].getName() == 'rubberband'):
				RC = RC - 1 
		else: 
			for o in range(len(listofstamps)-3):
				if(compare(listofstamps[i+1],listofstamps[o+2])):
					if(listofstamps[i+1].getName() == 'Wheel'):
						WC = WC - 1
					if(listofstamps[i+1].getName() == 'Balloon'):
						BC = BC - 1 
					if(listofstamps[i+1].getName() == 'Carbody'):
						CC = CC - 1 
					if(listofstamps[i+1].getName() == 'rubberband'):
						RC = RC - 1 


	Counter = [WC,RC,CC, BC]
	return Counter



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

def Comparator(ArrayStamps, TeacherArray):
	ArrayBecsved = [["GroupArray", 'wheels', 'wheels Nyla', 'carbody', 'carbody Nyla']]
	for i in range(len(ArrayStamps)):
		for x in range(len(TeacherArray)-1):
			tempArr = []
			#The first line of teacher array are the names of the objects. 
			if TeacherArray[x + 1][0] ==  ArrayStamps[i][1]:
				#tempArr.append([TeacherArray[x + 1][0],TeacherArray[x + 1][1],ArrayStamps[i][len(ArrayStamps[i])-1][5],TeacherArray[x + 1][2],ArrayStamps[i][len(ArrayStamps[i])-1][7]])
				ArrayBecsved.append([TeacherArray[x + 1][0],TeacherArray[x + 1][1],ArrayStamps[i][0][0],TeacherArray[x + 1][2],ArrayStamps[i][0][2]])
	return(ArrayBecsved)


JstArray = csvReader("DrawData.csv",11)
JArray = JsonConverter(JstArray)
mat=JsonStampCounter(JArray[4])
GroupIdArray = csvReader('DrawData.csv', 14)
AnalyzedCount = []
for  i in range(len(JArray)):
	AnalyzedCount.append([stampAnalyzer(JsonStampCounter(JArray[i])),GroupIdArray[i+1]])
comparisonNH = Comparator(AnalyzedCount, MatTeach)
csvPrinter(comparisonNH,"Firstcomparison.csv")
