import sys

from dao_generator import DaoGenerator
from entity import Entity
from schema import Schema

import os


class ModelGenerator:
    def __init__(self):
        self.PROJECT_DIR = os.getcwd()

    def generateEntities(self):
        schema = Schema('testMongoAppend')

        # query = {'Field': {'$gt': 0, '$lt': 2}}
        # db.Items.find({"Status": {$gt:0, $lt:2, $ne:0}}).pretty()

        memTemplate = schema.addEntity('ItemsTest')
        memTemplate.addIdProperty(is_auto=False)
        memTemplate.addStringProperty('Name')
        memTemplate.addStringProperty('Path')

        daoGenerator = DaoGenerator()
        daoGenerator.generateAll(schema, self.PROJECT_DIR + '/test/model', '192.168.0.189:20017')


if __name__ == "__main__":
    ModelGenerator().generateEntities()






