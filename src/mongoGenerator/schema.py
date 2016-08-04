from entity import Entity

class Schema:
	def __init__(self, name):
		self.__name = name
		self.__entities = []

	def getName(self):
		return self.__name

	def setName(self, name):
		self.__name = name

	def addEntity(self, name):
		self.__entities.append(Entity(name))
		return self.__entities[len(self.__entities) - 1]

	def getEntities(self):
		return self.__entities