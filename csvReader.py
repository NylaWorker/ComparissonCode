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
def JsonConverter(JsonStArray,errorType):
	count = 0 
	JsonArray = []
	for i in range(len(JsonStArray)-1):
		#If any value in the inserted array is checked to see if it is a json.
		try:
			js = json.loads(JsonStArray[i+1])
			JsonArray.append(js)
			#print(i+1) 
		except errorType: 
			#Here I count how many of the cells of the excel document we cannot read... I wonder why
			count = count + 1
			#In order to mess up the order of the Jsonarray I plugg them in with a dummy name 
			JsonArray.append("Wah Wah Wah")
	#print(count) 
	return(JsonArray)


JstArray = csvReader("DrawData.csv",11)
JArray = JsonConverter(JstArray, ValueError)
print(JArray[1]["drawData"])
#JArray1 = JsonConverter(JArray, TypeError)
# print(JArray[2])
