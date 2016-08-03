from schema import Schema

class SessionGenerator:
	def __init__(self, schema, directory):
		self.__schema = schema
		self.__directory = directory
	
	def setSchema(self):
		return self.__schema

	def generate(self):
		self._generateSession()
		
	def _generateSession(self):
		model_file = open(self.__directory + "/DaoSession.py", "wb")
			
		self._generateSessionHeader(model_file)
		self._generateSessionMethods(model_file)

		model_file.close()
	
	def _generateSessionHeader(self, model_file):
		model_file.write('from pymongo import MongoClient\n\n')
		
		for e in self.__schema.getEntities():
			model_file.write('from ' + e.getName() + 'Dao import ' + e.getName() + 'Dao\n')
		
		model_file.write('\nclass DaoSession:')
		model_file.write('\n\tdef __init__(self, db):')
		model_file.write('\n\t\tself.__db = db')
		
	def _generateSessionMethods(self, model_file):
		for s in self.__schema.getEntities():
			model_file.write('\n\n\tdef get' + s.getName() + 'Dao(self):\n\t\treturn ' + s.getName() + 'Dao(self.__db.' + s.getName() + ')')
			#model_file.write('\n\n\tdef set' + p + '(self, ' + p + '):\n\t\tself.__data[\'' + p + '\'] = ' + p)
			
		#for p in self.__entity.getFloatProperties():
			#model_file.write('\n\n\tdef get' + p + '(self):\n\t\treturn self.__data[\'' + p + '\']')
			#model_file.write('\n\n\tdef set' + p + '(self, ' + p + '):\n\t\tself.__data[\'' + p + '\'] = ' + p)
			
		#for p in self.__entity.getStringProperties():
			#model_file.write('\n\n\tdef get' + p + '(self):\n\t\treturn self.__data[\'' + p + '\']')
			#model_file.write('\n\n\tdef set' + p + '(self, ' + p + '):\n\t\tself.__data[\'' + p + '\'] = ' + p)