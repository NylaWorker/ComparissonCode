import csv
import json 
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
			#Here I count how many of the cells of the excel document we cannot read... I wonder why
			count = count + 1
			#In order to mess up the order of the Jsonarray I plugg them in with a dummy name 
			JsonArray.append({})
	#print(count) 
	return(JsonArray)

# This takes a single Json string and search for the stamps that we want and return an array
#that contains [#wheels,#Carbody, #Ballons, #rubberbands]
def JsonStampCounter(SingleJson):
	Wheelcounter = 0
	Carbodycounter = 0
	Ballooncounter = 0
	Rubberbandcounter = 0
	keyErr = 0 
	for i in range(len(SingleJson)):
		try:
			src = SingleJson[i]['src']
			print(src)
			#I split the string with the link in order to be able to check what stamp is being used. 
			feautures = src.split('/')
			if feautures[6] == 'Wheel.png':
				Wheelcounter = Wheelcounter + 1
			if feautures[6] == 'carbody_short.png':
				Carbodycounter = Carbodycounter + 1
			if feautures[6] == 'Balloon.png':
				Ballooncounter = Ballooncounter + 1
			if feautures[6] == 'rubberband.png':
				Rubberbandcounter = Rubberbandcounter+ 1
		except KeyError:
			keyErr = keyErr + 1
	return [Wheelcounter,Carbodycounter,Ballooncounter,Rubberbandcounter]

JstArray = csvReader("DrawData.csv",11)
JArray = JsonConverter(JstArray)


