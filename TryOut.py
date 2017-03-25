import csv
import json 

#imports the library and the next one is the path that can be changed

#I would rather use a path how do i do that?
#path = '~/Desktop/ResearchAnna/DrawData.csv'


#opens and closes the file

drawF = open('DrawData.csv')
ReadDF = csv.reader(drawF)

#This array has access to all the json strings in the csv document. 
JsonStArray = []
for row in ReadDF:
	JsonStArray.append(row[11])

#Remeber that in order to simplify things we are indexing from 1. We don't want to waste time one the index
#print(len(JsonStArray))

#for i in range(len(JsonStArray)):
#data = json.dumps(JsonStArray[1])
# print(JsonStArray[2])
print(len(JsonStArray))
print(type(json.loads(JsonStArray[34])))
# I don't know what happen while exporting or putting it in a csv but some of the lines won't load as a json string. 
data = json.loads(JsonStArray[2])
#check 34,35,39

data1 = json.loads(data["drawData"])

#print(data1['canvas']['objects'])
data2 = data1['canvas']['objects']
#print(data2)

NumObInDraw = len(data2)
Wheelcounter = 0
Carbodycounter = 0
Ballooncounter = 0
Rubberbandcounter = 0

print(len(data2))
for i in range(len(data2)):
	try:
		src = data2[i]['src']
		if src == 'http://wise.berkeley.edu/curriculum/15590/assets/Wheel.png':
			Wheelcounter = Wheelcounter + 1
		if src == 'http://wise.berkeley.edu/curriculum/15590/assets/carbody_short.png':
			Carbodycounter = Carbodycounter + 1
		if src == 'http://wise.berkeley.edu/curriculum/15590/assets/Balloon.png':
			Ballooncounter = Ballooncounter + 1
		if src == 'http://wise.berkeley.edu/curriculum/15590/assets/rubberband.png':
			Rubberbandcounter = Rubberbandcounter+ 1
	except KeyError:
		print("meow")

print(Wheelcounter)
print(Ballooncounter)
print(Carbodycounter)
print(Rubberbandcounter)
# pngs 
# http://wise.berkeley.edu/curriculum/15590/assets/Wheel.png
# http://wise.berkeley.edu/curriculum/15590/assets/carbody_short.png
# http://wise.berkeley.edu/curriculum/15590/assets/rubberband.png
# http://wise.berkeley.edu/curriculum/15590/assets/Balloon.png


#data2 = json.parse(data["drawData"])
#print(data["drawData"])
#data.close()
#data2 = json.loads(data["drawData"])

#data3["canvas"]["objects"]
#data4 = json.loads(data3["object"])
#print(data3["canvas"]["objects"])
#writer = csv.writer(open("Workbook1.csv", 'w'))
#for x in range(10):
#	writer.writerow(x)


#for i in range(len(JsonStArray)):
	#do whatever you have to. probably will be couting how many wheels. 


drawF.close()
