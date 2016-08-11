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
		model_dao_file.write('from pymongo import MongoClient\n')
		model_dao_file.write('from itertools import izip\n\n')
		model_dao_file.write('from '  + self.__entity.getName() +  ' import ' + self.__entity.getName() + '\n\n')
		model_dao_file.write('from '  + self.__entity.getName() +  'Properties import ' + self.__entity.getName() + 'Properties\n\n')
		model_dao_file.write('class ' + self.__entity.getName() + 'Dao:\n')
		model_dao_file.write('\tdef __init__(self, table):\n')
		model_dao_file.write('\t\tself.__table = table\n')
		model_dao_file.write('\t\tself.Properties = ' + self.__entity.getName() + 'Properties()\n\n')
		
	def _generateModelDaoMethods(self, model_dao_file):
		#Methods Create
		model_dao_file.write('\tdef create(self, entity):\n')
		if self.__entity.getIsPrimaryKey() and self.__entity.getIsAuto():
			model_dao_file.write('\t\tself._incrementInstanceId(entity)\n')
			model_dao_file.write('\t\treturn self.__table.insert(entity.getComposedData())\n\n')
		elif self.__entity.getIsPrimaryKey() and not self.__entity.getIsAuto():
			#model_dao_file.write('\t\t))\n')
			model_dao_file.write('\t\treturn self.__table.insert(entity.getComposedData())\n\n')
		else:
			model_dao_file.write('\t\tentity.setId(self.__table.insert(entity.getData()))\n')
			model_dao_file.write('\t\treturn entity.getId()\n\n')
			#model_dao_file.write('\t\treturn self.__table.insert(entity.getData())')

		model_dao_file.write('\tdef createCollection(self, collection):\n')
		if self.__entity.getIsPrimaryKey() and self.__entity.getIsAuto():
			model_dao_file.write('\t\tdata_list = []\n')
			model_dao_file.write('\t\tself._incrementCollectionId(collection)\n')
			model_dao_file.write('\t\tfor c in collection:\n')
			model_dao_file.write('\t\t\tdata_list.append(c.getComposedData())\n')
			model_dao_file.write('\t\tself.__table.insert_many(data_list)\n\n')
		elif self.__entity.getIsPrimaryKey() and not self.__entity.getIsAuto():
			# model_dao_file.write('\t\tfor c in collection:\n')
			# model_dao_file.write('\t\t\tself.create(c)\n\n')
			model_dao_file.write('\t\tdata_list = []\n')
			model_dao_file.write('\t\tfor c in collection:\n')
			model_dao_file.write('\t\t\tdata_list.append(c.getComposedData())\n')
			model_dao_file.write('\t\tself.__table.insert_many(data_list)\n\n')
		else:
			model_dao_file.write('\t\tdata_list = []\n')
			model_dao_file.write('\t\tfor c in collection:\n')
			model_dao_file.write('\t\t\tdata_list.append(c.getData())\n')
			model_dao_file.write('\t\tresult = self.__table.insert_many(data_list)\n')
			model_dao_file.write('\t\tfor i in range(len(result.inserted_ids)):\n')
			model_dao_file.write('\t\t\tcollection[i].setId(result.inserted_ids[i])\n\n')

		#Methods Read
		model_dao_file.write('\tdef readCollection(self, query):\n')
		model_dao_file.write('\t\treturn self._cursorToList(self.__table.find(query))\n\n')

		model_dao_file.write('\tdef readOne(self, query):\n')
		model_dao_file.write('\t\ttemp = self.__table.find_one(query)\n')
		model_dao_file.write('\t\ttemp_instance = ' + self.__entity.getName() + '()\n')
		model_dao_file.write('\t\tself._mapJSONToInstance(temp, temp_instance)\n')
		model_dao_file.write('\t\treturn temp_instance\n\n')

		model_dao_file.write('\tdef readOneByProperty(self, propertie, value):\n')
		model_dao_file.write('\t\treturn self.readOne({propertie:value})\n\n')

		model_dao_file.write('\tdef readOneByProperties(self, *args):\n')
		model_dao_file.write('\t\ti = iter(args)\n')
		model_dao_file.write('\t\treturn self.readOne(dict(izip(i, i)))\n\n')

		model_dao_file.write('\tdef readCollectionByProperty(self, property, value):\n')
		model_dao_file.write('\t\treturn self.readCollection({property: value})\n\n')

		model_dao_file.write('\tdef readByPropertyInValues(self, property, values):\n')
		model_dao_file.write('\t\treturn self.readCollection({property: {\'$in\': values}})\n\n')

		model_dao_file.write('\tdef readByPropertyNinValues(self, property, values):\n')
		model_dao_file.write('\t\treturn self.readCollection({property: {\'$nin\': values}})\n\n')

		model_dao_file.write('\tdef readByPropertyGtValue(self, property, value):\n')
		model_dao_file.write('\t\treturn self.readCollection({property: {\'$gt\': value}})\n\n')

		model_dao_file.write('\tdef readByPropertyGteValue(self, property, value):\n')
		model_dao_file.write('\t\treturn self.readCollection({property: {\'$gte\': value}})\n\n')

		model_dao_file.write('\tdef readByPropertyLteValue(self, property, value):\n')
		model_dao_file.write('\t\treturn self.readCollection({property: {\'$lte\': value}})\n\n')

		model_dao_file.write('\tdef readByPropertyLtValue(self, property, value):\n')
		model_dao_file.write('\t\treturn self.readCollection({property: {\'$lt\': value}})\n\n')

		model_dao_file.write('\tdef readByPropertyNeValue(self, property, value):\n')
		model_dao_file.write('\t\treturn self.readCollection({property: {\'$ne\': value}})\n\n')

		model_dao_file.write('\tdef readByPropertyGtValueLtValue(self, property, value1, value2):\n')
		model_dao_file.write('\t\treturn self.readCollection({property: {\'$gt\': value1, \'$lt\': value2}})\n\n')

		model_dao_file.write('\tdef readRandom(self):\n')
		model_dao_file.write('\t\ttemp = self.__table.find_one()\n')
		model_dao_file.write('\t\ttemp_instance = ' + self.__entity.getName() + '()\n')
		model_dao_file.write('\t\tself._mapJSONToInstance(temp, temp_instance)\n')
		model_dao_file.write('\t\treturn temp_instance\n\n')

		model_dao_file.write('\tdef readAll(self):\n')
		model_dao_file.write('\t\treturn self._cursorToList(self.__table.find())\n\n')

		model_dao_file.write('\tdef readByQuery(self, query):\n')
		model_dao_file.write('\t\treturn self._cursorToList(self.__table.find(query))\n\n')
		
		#Methods Update
		model_dao_file.write('\tdef update(self, entity):\n')
		#model_dao_file.write('\t\treturn self.__table.update(entity.getData())\n\n')
		model_dao_file.write('\t\treturn self.__table.update(entity.getIdData(), {\'$set\':entity.getData()})\n\n')

		model_dao_file.write('\tdef updateCollection(self, collection):\n')
		model_dao_file.write('\t\tfor c in collection:\n')
		model_dao_file.write('\t\t\tself.update(c)\n\n')

		#Methods Delete
		model_dao_file.write('\tdef deleteAll(self):\n')
		model_dao_file.write('\t\tresult = self.__table.remove({})\n\n')

		model_dao_file.write('\tdef delete(self, entity):\n')
		model_dao_file.write('\t\tresult = self.__table.remove(entity.getIdData())\n\n')

		model_dao_file.write('\tdef deleteCollection(self, collection):\n')
		model_dao_file.write('\t\tfor c in collection:\n')
		model_dao_file.write('\t\t\tself.delete(c)\n\n')

		#Methods Misc
		model_dao_file.write('\tdef count(self):\n')
		model_dao_file.write('\t\treturn self.__table.count()\n\n')

		model_dao_file.write('\tdef getFieldCount(self):\n')
		model_dao_file.write('\t\treturn ' + str(len(self.__entity.getBoolProperties()) + len(self.__entity.getIntProperties()) + len(self.__entity.getFloatProperties()) + len(self.__entity.getStringProperties())) + '\n\n') 
	
	def _generateModelDaoInternalMethods(self, model_dao_file):
		#_mapJSONToInstance
		model_dao_file.write('\tdef _mapJSONToInstance(self, json_doc, instance):\n')
		# model_dao_file.write('\t\tinstance.setId(json_doc.get(\'_id\'))\n')
		model_dao_file.write('\t\tif json_doc is not None:\n')
		
		for p in self.__entity.getIntProperties():
			model_dao_file.write('\t\t\tinstance.set' + p + '(json_doc.get(\'' + p + '\'))\n')
		for p in self.__entity.getFloatProperties():
			model_dao_file.write('\t\t\tinstance.set' + p + '(json_doc.get(\'' + p + '\'))\n')
		for p in self.__entity.getStringProperties():
			model_dao_file.write('\t\t\tinstance.set' + p + '(json_doc.get(\'' + p + '\'))\n')
		for p in self.__entity.getBoolProperties():
			model_dao_file.write('\t\t\tinstance.set' + p + '(json_doc.get(\'' + p + '\'))\n')
		for p in self.__entity.getListProperties():
			#model_dao_file.write('\t\tinstance.set' + p + '(json_doc.get(\'' + p + '\'))\n')
			model_dao_file.write('\t\t\tfor i in json_doc.get(\'' + p + '\'):\n')
			model_dao_file.write('\t\t\t\tinstance.add' + p + '(i)\n')

		model_dao_file.write('\t\t\tif len(json_doc) > self.getFieldCount():\n')
		model_dao_file.write('\t\t\t\tli = list(set(json_doc.keys()) - set(instance.getData().keys()))\n')
		model_dao_file.write('\t\t\t\tfor i in li:\n')
		model_dao_file.write('\t\t\t\t\tinstance.setField(i, json_doc.get(i))\n')
		model_dao_file.write('\t\t\tinstance.setId(json_doc.get(\'_id\'))\n')
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

		#get setLast + 1 id method
		if self.__entity.getIsPrimaryKey() and self.__entity.getIsAuto():
			model_dao_file.write('\tdef _incrementInstanceId(self, entity):\n')
			model_dao_file.write('\t\tif self.count() is not 0:\n')
			# model_dao_file.write('\t\t\tcursor = self.__table.find().sort([(\"_id\", pymongo.ASCENDING)])\n')
			model_dao_file.write('\t\t\tentity.setId(self._readLastId() + 1)\n')
			model_dao_file.write('\t\telse:\n')
			model_dao_file.write('\t\t\tentity.setId(0)\n\n')

			model_dao_file.write('\tdef _incrementCollectionId(self, collection):\n')
			model_dao_file.write('\t\tif self.count() is not 0:\n')
			model_dao_file.write('\t\t\tbegin = self._readLastId() + 1\n')
			model_dao_file.write('\t\telse:\n')
			model_dao_file.write('\t\t\tbegin = 0\n')
			model_dao_file.write('\t\tfor i in collection:\n')
			model_dao_file.write('\t\t\ti.setId(begin)\n')
			model_dao_file.write('\t\t\tbegin += 1\n\n')

		#get list from cursor
		model_dao_file.write('\tdef _cursorToList(self, cursor):\n')
		model_dao_file.write('\t\tresult = []\n')
		model_dao_file.write('\t\tfor c in cursor:\n')
		model_dao_file.write('\t\t\tresult.append(self._mapJSONToNewInstance(c))\n') 
		model_dao_file.write('\t\treturn result\n\n') 