
class Entity:
	def __init__(self, name):
		self.__name = name
		self.__is_primary_key = False
		self.__int_properties = []
		self.__float_properties = []
		self.__string_properties = []
		self.__bool_properties = []
		self.__list_properties = []
	
	def getName(self):
		return self.__name

	def addIdProperty(self, is_auto = False):
		self.__is_primary_key = True
		self.__is_auto = is_auto
		
	def addIntProperty(self, name):
		self.__int_properties.append(name)
		
	def addFloatProperty(self, name):
		self.__float_properties.append(name)
		
	def addStringProperty(self, name):
		self.__string_properties.append(name)
		
	def addBoolProperty(self, name):
		self.__bool_properties.append(name)
		
	def addListProperty(self, name):
		self.__list_properties.append(name)
		
	def getIsPrimaryKey(self):
		return self.__is_primary_key
	
	def getIsAuto(self):
		return self.__is_auto
	
	def getIntProperties(self):
		return self.__int_properties
	
	def getFloatProperties(self):
		return self.__float_properties
	
	def getStringProperties(self):
		return self.__string_properties
	
	def getBoolProperties(self):
		return self.__bool_properties
	
	def getListProperties(self):
		return self.__list_properties