class Stamps:
	#Creates a class that defines an element
	def __init__(self, name, coordinates, width, height,order):
		self.name = name
		self.coordinates = coordinates
		self.order = order
		self.width = width
		self.height = height
	def getWidth(self):
		return(self.width)
	def getHeight(self):
		return(self.height)
	def getCoordinates(self):
		return(self.coordinates)
	def getName(self):
		return(self.name)
	def getOrder(self):
		return(self.order)
	def getAll(self):
		return([self.name,self.coordinates,self.width,self.height,self.order])

