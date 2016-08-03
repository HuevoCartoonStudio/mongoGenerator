from schema import Schema


class MasterGenerator:
	def __init__(self, schema, directory):
		self.__schema = schema
		self.__directory = directory
	
	def setSchema(self):
		return self.__schema

	def generate(self):
		self._generateMaster()
		
	def _generateMaster(self):
		model_file = open(self.__directory + "/DaoMaster.py", "wb")
			
		self._generateMasterHeader(model_file)
		self._generateMasterSession(model_file)

		model_file.close()
	
	def _generateMasterHeader(self, model_file):
		model_file.write('from pymongo import MongoClient')
		model_file.write('\n\nfrom DaoSession import DaoSession')
		model_file.write('\n\nclass DaoMaster:')
		model_file.write('\n\tdef __init__(self):')
		model_file.write('\n\t\tself.__client = MongoClient(\'localhost:27017\')')
		model_file.write('\n\t\tself.__db = self.__client.' + self.__schema.getName())
		
	def _generateMasterSession(self, model_file):
		model_file.write('\n\n\tdef getSession(self):')
		model_file.write('\n\t\t return DaoSession(self.__db)')
	