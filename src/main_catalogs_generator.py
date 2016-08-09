
from dao_generator import DaoGenerator
from entity import Entity
from schema import Schema

import os


class ModelGenerator:
    def __init__(self):
        self.PROJECT_DIR = os.getcwd()

    def generate_entities(self):
        schema = Schema('testMongoGen')

        asset_template = schema.addEntity('CatalogItemType')
        asset_template.addIdProperty(is_auto = False)
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

        asset_template = schema.addEntity('Items')
        asset_template.addIdProperty(is_auto=False)
        asset_template.addStringProperty('Name')
        asset_template.addStringProperty('Path')
        asset_template.addStringProperty('DateTime')
        asset_template.addStringProperty('AssetSubscription')
        asset_template.addStringProperty('ReferenceSubscription')
        asset_template.addStringProperty('TaskSubscription')
        asset_template.addStringProperty('UserSubscription')
        asset_template.addStringProperty('Type')
        asset_template.addStringProperty('Format')
        asset_template.addStringProperty('Status')
        asset_template.addFloatProperty('Version')
        asset_template.addBoolProperty('Archive')
        asset_template.addStringProperty('Complejidad')

        asset_template = schema.addEntity('Assets')
        asset_template.addIdProperty(is_auto=False)
        asset_template.addStringProperty('Name')
        asset_template.addStringProperty('Path')
        asset_template.addStringProperty('DateTime')
        asset_template.addStringProperty('ItemSubscription')
        asset_template.addStringProperty('SuperAssetSubscription')
        asset_template.addStringProperty('ShotSubscription')
        asset_template.addStringProperty('SequenceSubscription')
        asset_template.addStringProperty('TaskSubscription')
        asset_template.addStringProperty('UserSubscription')
        asset_template.addStringProperty('Type')
        asset_template.addStringProperty('Format')
        asset_template.addStringProperty('Status')
        asset_template.addFloatProperty('Version')
        asset_template.addBoolProperty('Archive')
        asset_template.addStringProperty('Complejidad')

        asset_template = schema.addEntity('SuperAssets')
        asset_template.addIdProperty(is_auto=False)
        asset_template.addStringProperty('Name')
        asset_template.addStringProperty('Path')
        asset_template.addStringProperty('DateTime')
        asset_template.addStringProperty('AssetSubscription')
        asset_template.addStringProperty('ShotSubscription')
        asset_template.addStringProperty('SequenceSubscription')
        asset_template.addStringProperty('ProyectSubscription')
        asset_template.addStringProperty('TaskSubscription')
        asset_template.addStringProperty('UserSubscription')
        asset_template.addStringProperty('Type')
        asset_template.addStringProperty('Format')
        asset_template.addStringProperty('Status')
        asset_template.addFloatProperty('Version')
        asset_template.addBoolProperty('Archive')
        asset_template.addStringProperty('Complejidad')

        daoGenerator = DaoGenerator()
        daoGenerator.generateAll(schema, self.PROJECT_DIR + '/documents', '192.168.0.189:20017')


if __name__ == "__main__":
    ModelGenerator().generate_entities()
