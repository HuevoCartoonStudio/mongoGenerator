import sys

sys.path.insert(0, './mongoGenerator/')

from dao_generator import DaoGenerator
from entity import Entity
from schema import Schema

import os

class ModelGenerator:
	
	def __init__(self):
		self.PROJECT_DIR = os.getcwd()
	
	def generateEntities(self):
		schema = Schema('assetmanagerdb')
		
		memTemplate = schema.addEntity('Items')
		#memTemplate.addIdProperty(is_auto = True)
		memTemplate.addStringProperty('Name')
		memTemplate.addStringProperty('Path')
		memTemplate.addStringProperty('AssetSubscription')
		memTemplate.addStringProperty('SuperAssetSubscription')
		memTemplate.addStringProperty('DigitalMediaSubscription')
		memTemplate.addStringProperty('ArtSubscription')
		memTemplate.addStringProperty('UserSubscription')
		memTemplate.addStringProperty('Type')
		memTemplate.addStringProperty('Format')
		memTemplate.addIntProperty('Status')
		memTemplate.addFloatProperty('Version')
		
		memTemplate = schema.addEntity('Assets')
		#memTemplate.addIdProperty(is_auto = True)
		memTemplate.addStringProperty('Name')
		memTemplate.addStringProperty('Path')
		memTemplate.addStringProperty('ItemSubscription')
		memTemplate.addStringProperty('ProyectSubscription')
		memTemplate.addStringProperty('SuperAssetSubscription')
		memTemplate.addStringProperty('ShotSubscription')
		memTemplate.addStringProperty('SequenceSubscription')
		memTemplate.addStringProperty('DigitalMediaSubscription')
		memTemplate.addStringProperty('TaskSubscription')
		memTemplate.addStringProperty('UserSubscription')
		memTemplate.addStringProperty('Type')
		memTemplate.addStringProperty('Format')
		memTemplate.addIntProperty('Status')
		
		memTemplate = schema.addEntity('SuperAssets')
		#memTemplate.addIdProperty(is_auto = True)
		memTemplate.addStringProperty('Name')
		memTemplate.addStringProperty('Path')
		memTemplate.addStringProperty('ItemSubscription')
		memTemplate.addStringProperty('AssetSubscription')
		memTemplate.addStringProperty('DigitalMediaSubscription')
		memTemplate.addStringProperty('ShotSubscription')
		memTemplate.addStringProperty('SequenceSubscription')
		memTemplate.addStringProperty('ProyectSubscription')
		memTemplate.addStringProperty('TaskSubscription')
		memTemplate.addStringProperty('UserSubscription')
		memTemplate.addStringProperty('Type')
		memTemplate.addStringProperty('Format')
		memTemplate.addIntProperty('Status')
		
		daoGenerator = DaoGenerator()
		daoGenerator.generateAll(schema, self.PROJECT_DIR + '/test/model')


if __name__ == "__main__":
	ModelGenerator().generateEntities()





	
