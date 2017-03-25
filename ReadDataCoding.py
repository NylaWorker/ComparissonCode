import csv
import math 

def csvReader(File, rowWanted):
	dataFile = open(File)
	readData = csv.reader(dataFile)
	DataArray= []
	for row in readData:
		DataArray.append(row[rowWanted])
	dataFile.close()
	return DataArray

def csvPrinter(Matrix, nameFile):
	writer = csv.writer(open(nameFile, 'w'), delimiter = ',')
	for x in range(len(Matrix)):
		try:
			writer.writerow(Matrix[x])
		except IndexError:
			print('Oh No')



A = [[1,2,3],[2,3,4],[1,3,3]]
csvPrinter(A, 'gno.csv')