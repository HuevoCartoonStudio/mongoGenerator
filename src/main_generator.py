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
		schema = Schema('mongodbtest3')
		
		memTemplate = schema.addEntity('Users')
		#memTemplate.addIdProperty(is_auto = True)
		memTemplate.addStringProperty('Name')
		#memTemplate.addBoolProperty('IsValid')
		
		#try:
		daoGenerator = DaoGenerator()
		daoGenerator.generateAll(schema, self.PROJECT_DIR + '/test/model')
		#except:
			#print(sys.exc_info()[0])
			#raise

        #memInfGen = schema.addEntity('MemorandumInformationGeneral')
        #memInfGen.addIdProperty().autoincrement().primaryKey()
        #memInfGen.addLongProperty('idMemo')
        #memInfGen.addStringProperty('title')
        #memInfGen.addStringProperty('company')
        #memInfGen.addStringProperty('place')
        #memInfGen.addStringProperty('objective')

        #memInfPar = schema.addEntity('MemorandumInformationParticipants')
        #memInfPar.addIdProperty().autoincrement().primaryKey()
        #memInfPar.addLongProperty('idMemo')
        #memInfPar.addStringProperty('participant')
        #memInfPar.addStringProperty('participantMail')

        #memInfTkp = schema.addEntity('MemorandumInformationTalkingpoints')
        #memInfTkp.addIdProperty().autoincrement().primaryKey()
        #memInfTkp.addLongProperty('idMemo')
        #memInfTkp.addStringProperty('talkingPoint')

        #memInfAgr = schema.addEntity('MemorandumInformationAgreements')
        #memInfAgr.addIdProperty().autoincrement().primaryKey()
        #memInfAgr.addLongProperty('idMemo')
        #memInfAgr.addStringProperty('agreements')

        #memInfPen = schema.addEntity('MemorandumInformationPendings')
        #memInfPen.addIdProperty().autoincrement().primaryKey()
        #memInfPen.addLongProperty('idMemo')
        #memInfPen.addStringProperty('pendings')
        
        


if __name__ == "__main__":
	ModelGenerator().generateEntities()





	
