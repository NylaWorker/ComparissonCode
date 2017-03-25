class Stamps:
	#Creates a class that defines an element
	def __init__(self, name, coordinates, Area,order):
		self.name = name
		self.coordinates = coordinates
		self.order = order
		self.Area =Area
	def getArea(self):
		return(self.Area)
	def getCoordinates(self):
		return(self.coordinates)
	def getName(self):
		return(self.name)
	def getOrder(self):
		return(self.order)
	def getAll(self):
		return([self.name,self.coordinates,self.Area,self.order])

