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
        schema = Schema('testMongoGen')

        # query = {'Field': {'$gt': 0, '$lt': 2}}
        # db.Items.find({"Status": {$gt:0, $lt:2, $ne:0}}).pretty()

        memTemplate = schema.addEntity('Items')
        # memTemplate.addIdProperty(is_auto=False)
        memTemplate.addStringProperty('Class')
        memTemplate.addStringProperty('Name')
        memTemplate.addStringProperty('Path')
        memTemplate.addStringProperty('DateTime')
        memTemplate.addIntProperty('Type')
        memTemplate.addIntProperty('Format')
        memTemplate.addIntProperty('Status')
        memTemplate.addFloatProperty('Version')
        memTemplate.addStringProperty('PrevVersion')
        memTemplate.addStringProperty('NextVersion')
        memTemplate.addListProperty('UserSubscription')
        memTemplate.addListProperty('TaskSubscription')

        memTemplate.addListProperty('ProyectSubscription')
        memTemplate.addListProperty('SequenceSubscription')
        memTemplate.addListProperty('ShotSubscription')
        memTemplate.addListProperty('ItemSubscription')
        memTemplate.addListProperty('AssetSubscription')
        memTemplate.addListProperty('SuperAssetSubscription')
        memTemplate.addListProperty('DigitalMediaSubscription')

        memTemplate = schema.addEntity('CatalogDepartment')
        memTemplate.addIdProperty(is_auto=True)
        memTemplate.addStringProperty('Name')

        memTemplate = schema.addEntity('Users')
        memTemplate.addIdProperty(is_auto=True)
        memTemplate.addStringProperty('Name')
        memTemplate.addStringProperty('Department')
        memTemplate.addStringProperty('Email')
        memTemplate.addBoolProperty('IsActive')

        #######################################################################################

        asset_template = schema.addEntity('CatalogClassType')
        asset_template.addIdProperty(is_auto=False)
        asset_template.addStringProperty('ClassType')
        # asset_template.addIntProperty('Code')

        asset_template = schema.addEntity('CatalogItemType')
        asset_template.addIdProperty(is_auto=False)
        asset_template.addStringProperty('ItemType')
        # asset_template.addIntProperty('Code')

        asset_template = schema.addEntity('CatalogComplexType')
        asset_template.addIdProperty(is_auto=False)
        asset_template.addStringProperty('ComplexType')
        # asset_template.addIntProperty('Code')

        asset_template = schema.addEntity('CatalogStatusType')
        asset_template.addIdProperty(is_auto=False)
        asset_template.addStringProperty('StatusType')
        # asset_template.addIntProperty('Code')

        asset_template = schema.addEntity('CatalogStatusType')
        asset_template.addIdProperty(is_auto=False)
        asset_template.addStringProperty('StatusType')
        # asset_template.addIntProperty('Code')

        asset_template = schema.addEntity('CatalogFormatType')
        asset_template.addIdProperty(is_auto=False)
        asset_template.addListProperty('SRC')
        asset_template.addListProperty('PRO')
        asset_template.addListProperty('ENV')
        asset_template.addListProperty('CHR')
        asset_template.addListProperty('RIG')
        asset_template.addListProperty('FXS')
        asset_template.addListProperty('TEM')
        asset_template.addListProperty('GEO')
        asset_template.addListProperty('ART')
        asset_template.addListProperty('SHD')
        asset_template.addListProperty('TEX')
        asset_template.addListProperty('CCH')
        asset_template.addListProperty('SQI')
        asset_template.addListProperty('DCC')
        asset_template.addListProperty('NON')

        daoGenerator = DaoGenerator()
        daoGenerator.generateAll(schema, self.PROJECT_DIR + '/test/model', '192.168.0.189:20017')


if __name__ == "__main__":
    ModelGenerator().generateEntities()






