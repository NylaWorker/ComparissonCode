import csv
import json 
import simplejson
import urllib2
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
print(len(JsonStArray))

#writer = csv.writer(open("Workbook1.csv", 'w'))
#for x in range(10):
#	writer.writerow(x)


#for i in range(len(JsonStArray)):
	#do whatever you have to. probably will be couting how many wheels. 


drawF.close()
