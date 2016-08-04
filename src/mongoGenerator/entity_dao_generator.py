from entity import Entity

class EntityDaoGenerator:
	def __init__(self, entity, directory):
		self.__entity = entity
		self.__directory = directory
	
	def setEntity(self):
		return self.__entity

	def generate(self):
		self._generateModelDao()
		
	def _generateModelDao(self):
		model_dao_file = open(self.__directory + "/" + self.__entity.getName() + "Dao.py", "wb")
			
		self._generateModelDaoHeader(model_dao_file)
		self._generateModelDaoMethods(model_dao_file)
		self._generateModelDaoInternalMethods(model_dao_file)
			
		model_dao_file.close()
	
	def _generateModelDaoHeader(self, model_dao_file):
		model_dao_file.write('import pymongo\n')
		model_dao_file.write('from pymongo import MongoClient\n\n')
		model_dao_file.write('from '  + self.__entity.getName() +  ' import ' + self.__entity.getName() + '\n\n')
		model_dao_file.write('class ' + self.__entity.getName() + 'Dao:\n')
		model_dao_file.write('\tdef __init__(self, table):\n')
		model_dao_file.write('\t\tself.__table = table\n\n')
		
	def _generateModelDaoMethods(self, model_dao_file):
		#Method Count
		model_dao_file.write('\tdef count(self):\n')
		model_dao_file.write('\t\treturn self.__table.count()\n\n')
		
		#Method Insert
		model_dao_file.write('\tdef create(self, entity):\n')
		if (self.__entity.getIsPrimaryKey() and self.__entity.getIsAuto()):
			model_dao_file.write('\t\tif (self.count() is not 0):\n')
			model_dao_file.write('\t\t\tcursor = self.__table.find().sort([(\"_id\", pymongo.ASCENDING)])\n')
			model_dao_file.write('\t\t\tentity.setId(self._readLastId() + 1)\n')
			model_dao_file.write('\t\telse:\n')
			model_dao_file.write('\t\t\tentity.setId(0)\n')
			model_dao_file.write('\t\treturn self.__table.insert(entity.getComposedData())\n\n')
		elif(not self.__entity.getIsAuto()):
			#model_dao_file.write('\t\t))\n')
			model_dao_file.write('\t\treturn self.__table.insert(entity.getComposedData())\n\n')
		else:
			model_dao_file.write('\t\tentity.setId(self.__table.insert(entity.getData()))\n')
			model_dao_file.write('\t\treturn entity.getId()\n\n')
			#model_dao_file.write('\t\treturn self.__table.insert(entity.getData())')
		
		#Method Update
		model_dao_file.write('\tdef update(self, entity):\n')
		#model_dao_file.write('\t\treturn self.__table.update(entity.getData())\n\n')
		model_dao_file.write('\t\treturn self.__table.update(entity.getIdData(), {\'$set\':entity.getData()})\n\n')
		
		#Method GetFirst
		model_dao_file.write('\tdef readFirst(self):\n')
		model_dao_file.write('\t\ttemp = self.__table.find_one()\n')
		model_dao_file.write('\t\ttemp_instance = ' + self.__entity.getName() + '()\n')
		model_dao_file.write('\t\tself._mapJSONToInstance(temp, temp_instance)\n')
		model_dao_file.write('\t\treturn temp_instance\n\n')
		
		#Method getAll
		model_dao_file.write('\tdef readAll(self):\n') 
		model_dao_file.write('\t\treturn self._cursorToList(self.__table.find())\n\n')
		
		#Method removeAll
		model_dao_file.write('\tdef deleteAll(self):\n')
		model_dao_file.write('\t\tresult = self.__table.remove({})\n\n')
		
		#Method getByQuery
		model_dao_file.write('\tdef readByQuery(self, query):\n')
		model_dao_file.write('\t\treturn self._cursorToList(self.__table.find(query))\n\n')
		
		model_dao_file.write('\tdef getFieldCount(self):\n')
		model_dao_file.write('\t\treturn ' + str(len(self.__entity.getBoolProperties()) + len(self.__entity.getIntProperties()) + len(self.__entity.getFloatProperties()) + len(self.__entity.getStringProperties())) + '\n\n') 
	
	def _generateModelDaoInternalMethods(self, model_dao_file):
		#_mapJSONToInstance
		model_dao_file.write('\tdef _mapJSONToInstance(self, json_doc, instance):\n')
		model_dao_file.write('\t\tinstance.setId(json_doc.get(\'_id\'))\n')
		
		for p in self.__entity.getIntProperties():
			model_dao_file.write('\t\tinstance.set' + p + '(json_doc.get(\'' + p + '\'))\n')
		for p in self.__entity.getFloatProperties():
			model_dao_file.write('\t\tinstance.set' + p + '(json_doc.get(\'' + p + '\'))\n')
		for p in self.__entity.getStringProperties():
			model_dao_file.write('\t\tinstance.set' + p + '(json_doc.get(\'' + p + '\'))\n')
		for p in self.__entity.getBoolProperties():
			model_dao_file.write('\t\tinstance.set' + p + '(json_doc.get(\'' + p + '\'))\n')
		for p in self.__entity.getListProperties():
			#model_dao_file.write('\t\tinstance.set' + p + '(json_doc.get(\'' + p + '\'))\n')
			model_dao_file.write('\t\tfor i in json_doc.get(\'' + p + '\'):\n')
			model_dao_file.write('\t\t\tinstance.add' + p + '(i)\n')
			
			
		model_dao_file.write('\n')
		
		#_mapJSONToNewInstance
		model_dao_file.write('\tdef _mapJSONToNewInstance(self, json_doc):\n')
		model_dao_file.write('\t\tinstance = ' + self.__entity.getName() + '()\n')
		model_dao_file.write('\t\tself._mapJSONToInstance(json_doc, instance)\n')
		model_dao_file.write('\t\treturn instance\n\n')
			
		#get last id number
		model_dao_file.write('\tdef _readLastId(self):\n')
		model_dao_file.write('\t\tcursor = self.__table.find().sort([(\"_id\", pymongo.ASCENDING)])\n')
		model_dao_file.write('\t\treturn cursor[cursor.count() - 1].get(\'_id\')\n\n')
		
		#get list from cursor
		model_dao_file.write('\tdef _cursorToList(self, cursor):\n')
		model_dao_file.write('\t\tresult = []\n')
		model_dao_file.write('\t\tfor c in cursor:\n')
		model_dao_file.write('\t\t\tresult.append(self._mapJSONToNewInstance(c))\n') 
		model_dao_file.write('\t\treturn result\n\n') 