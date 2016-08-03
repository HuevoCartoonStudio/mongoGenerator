import os

from schema import Schema
from entity import Entity
from entity_generator import EntityGenerator
from entity_dao_generator import EntityDaoGenerator
from master_generator import MasterGenerator
from session_generator import SessionGenerator
#from dao_master_generator import daoMasterGenerator

class DaoGenerator:
	def generateAll(self, schema, directory):
		#print ('hello')
		
		print (directory + '/' + schema.getName())
		
		if not os.path.exists(directory + '/' + schema.getName()):
			os.makedirs(directory + '/' + schema.getName())
		
		for i in schema.getEntities():
			entity_gen = EntityGenerator(i, directory + '/' + schema.getName())
			entity_gen.generate()
			
			entity_dao_gen = EntityDaoGenerator(i, directory + '/' + schema.getName())
			entity_dao_gen.generate()
		
		master_gen = MasterGenerator(schema, directory + '/' + schema.getName())
		master_gen.generate()
		
		session_gen = SessionGenerator(schema, directory + '/' + schema.getName())
		session_gen.generate()
