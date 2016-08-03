from entity import Entity


class EntityGenerator:
	def __init__(self, entity, directory):
		self.__entity = entity
		self.__directory = directory
	
	def setEntity(self):
		return self.__entity

	def generate(self):
		self._generateModel()
		
	def _generateModel(self):
		model_file = open(self.__directory + "/" + self.__entity.getName() + ".py", "wb")
			
		self._generateModelHeader(model_file)
		self._generateModelData(model_file)
		self._generateModelMethods(model_file)
			
		model_file.close()
	
	def _generateModelHeader(self, model_file):
		model_file.write('from collections import Counter\n\n')
		model_file.write('class ' + self.__entity.getName() + ':\n')
		model_file.write('\tdef __init__(self):\n')
		model_file.write('\t\tself.__id = Counter({\"_id\" : 0})\n')
		model_file.write('\t\tself.__data = Counter({')
		
	def _generateModelData(self, model_file):
		#if (self.__entity.getIsPrimaryKey()):
			#model_file.write('\"_id\" : 0, ')

		for p in self.__entity.getIntProperties():
			model_file.write('\"' + p + '\" : 0,')
			
		for p in self.__entity.getFloatProperties():
			model_file.write('\"' + p + '\" : 0.0, ')
			
		for p in self.__entity.getStringProperties():
			model_file.write('\"' + p + '\" : \"\", ')
			
		for p in self.__entity.getBoolProperties():
			model_file.write('\"' + p + '\" : False, ')
			
		model_file.write('})\n\n')
		
	def _generateModelMethods(self, model_file):
		
		model_file.write('\tdef getIdData(self):\n')
		model_file.write('\t\treturn self.__id\n\n')
		
		model_file.write('\tdef getData(self):\n')
		model_file.write('\t\treturn self.__data\n\n')
		
		model_file.write('\tdef getComposedData(self):\n')
		model_file.write('\t\treturn self.__id + self.__data\n\n')
		
		model_file.write('\tdef getField(self, token):\n')
		model_file.write('\t\treturn self.__data[token]\n\n')
		
		model_file.write('\tdef setField(self, token, value):\n')
		model_file.write('\t\tself.__data[token] = value\n\n')
		
		#if (self.__entity.getIsPrimaryKey() and self.__entity.getIsAuto()):
			#model_file.write('\n\n\tdef getId(self):\n\t\treturn self.__data[\'_id\']')
		#elif (self.__entity.getIsPrimaryKey() and not self.__entity.getIsAuto()):
		model_file.write('\tdef getId(self):\n')
		model_file.write('\t\treturn self.__id[\'_id\']\n\n')
		model_file.write('\tdef setId(self, id):\n')
		model_file.write('\t\tself.__id[\'_id\'] = id\n\n')
		#else:
			#model_file.write('\n\n\tdef getId(self):\n\t\treturn self.__data[\'_id\']')
		
		for p in self.__entity.getIntProperties():
			model_file.write('\tdef get' + p + '(self):\n')
			model_file.write('\t\treturn self.__data[\'' + p + '\']\n\n')
			model_file.write('\tdef set' + p + '(self, ' + p + '):\n')
			model_file.write('\t\tself.__data[\'' + p + '\'] = ' + p + '\n\n')
			
		for p in self.__entity.getFloatProperties():
			model_file.write('\tdef get' + p + '(self):\n')
			model_file.write('\t\treturn self.__data[\'' + p + '\']\n\n')
			model_file.write('\tdef set' + p + '(self, ' + p + '):\n')
			model_file.write('\t\tself.__data[\'' + p + '\'] = ' + p + '\n\n')
			
		for p in self.__entity.getStringProperties():
			model_file.write('\tdef get' + p + '(self):\n')
			model_file.write('\t\treturn self.__data[\'' + p + '\']\n\n')
			model_file.write('\tdef set' + p + '(self, ' + p + '):\n')
			model_file.write('\t\tself.__data[\'' + p + '\'] = ' + p + '\n\n')
			
		for p in self.__entity.getBoolProperties():
			model_file.write('\tdef get' + p + '(self):\n')
			model_file.write('\t\treturn self.__data[\'' + p + '\']\n\n')
			model_file.write('\tdef set' + p + '(self, ' + p + '):\n')
			model_file.write('\t\tself.__data[\'' + p + '\'] = ' + p + '\n\n')
	