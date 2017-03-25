import csv
import json 
import math 
from decimal import *
#from ResearchAnna import Stamp
from Stamp import Stamps
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
			jsT = SingleJson[i]['top']
			jsL = SingleJson[i]['left']
			#scale of the width fix..!!!

			jsH = float(SingleJson[i]['scaleY'])* float(SingleJson[i]['height'])
			jsW = float(SingleJson[i]['scaleX'])* float(SingleJson[i]['width'])
			
			#I split the string with the link in order to be able to check what stamp is being used. 
			feautures = src.split('/')
			if feautures[6] == 'Wheel.png':
				Wheelcounter = Wheelcounter + 1
				order += 1 
				ClassList.append(Stamps('Wheel',[jsL,jsT],area(jsH,jsW,'c'),order))
				
			if feautures[6] == 'carbody_short.png':
				Carbodycounter = Carbodycounter + 1
				order += 1 
				ClassList.append(Stamps('Carbody',[jsL,jsT],area(jsH,jsW,'lk'),order))
				
			if feautures[6] == 'Balloon.png':
				Ballooncounter = Ballooncounter + 1
				order += 1 
				ClassList.append(Stamps('Balloon',[jsL,jsT],area(jsH,jsW,'c'),order))
				
			if feautures[6] == 'rubberband.png':
				Rubberbandcounter = Rubberbandcounter+ 1
				order += 1 
				ClassList.append(Stamps('rubberband',[jsL,jsT],area(jsH,jsW,'asf'),order))

		except KeyError:
			keyErr = keyErr + 1
	# for i in range(len(ClassList)):
	# 	print(ClassList[i].getAll())
	#the out put is a list of all the elements pluss the c
	ClassList.append(['b', Ballooncounter,'r',Rubberbandcounter,'w',Wheelcounter,'c',Carbodycounter])
	return ClassList


def compare(stamp1, stamp2):
	#within a range 
	if(distanceCalc(stamp1.getCoordinates(), stamp2.getCoordinates()) > 2*(int(stamp1.getArea())**(1/2.0))):
		return False
	else:
		return True

def stampAnalyzer(listofstamps):
	WC = listofstamps[len(listofstamps)-1][5]
	RC = listofstamps[len(listofstamps)-1][3]
	CC = listofstamps[len(listofstamps)-1][7]
	BC = listofstamps[len(listofstamps)-1][1]
	
	for i in range(len(listofstamps)-1):
		
		if(float(listofstamps[i].getCoordinates()[0]) < 0 or int(listofstamps[i].getCoordinates()[0]) > 800 or int(listofstamps[i].getCoordinates()[1]) > 600 or int(listofstamps[i].getCoordinates()[1]) <0):
			if(listofstamps[i].getName() == 'Wheel'):
				WC = WC - 1
			if(listofstamps[i].getName() == 'Balloon'):
				BC = BC - 1 
			if(listofstamps[i].getName() == 'Carbody'):
				CC = CC - 1 
			if(listofstamps[i].getName() == 'rubberband'):
				RC = RC - 1 
		else: 
			for o in range(len(listofstamps)-2):
				if(compare(listofstamps[i],listofstamps[o+1])==True):
					if(listofstamps[i].getName() == 'Wheel'):
						WC = WC - 1
					if(listofstamps[i].getName() == 'Balloon'):
						BC = BC - 1 
					if(listofstamps[i].getName() == 'Carbody'):
						CC = CC - 1 
					if(listofstamps[i].getName() == 'rubberband'):
						RC = RC - 1 


	Counter = [WC,RC,CC, BC]
	return Counter

JstArray = csvReader("DrawData.csv",11)
JArray = JsonConverter(JstArray)
mat=JsonStampCounter(JArray[2])
print(stampAnalyzer(mat))







 		




