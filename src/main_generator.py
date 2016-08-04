from dao_generator import DaoGenerator
from entity import Entity
from schema import Schema

import os


class ModelGenerator:
    def __init__(self):
        self.PROJECT_DIR = os.getcwd()

    def generate_entities(self):
        schema = Schema('mongodbtest6')

        doc_template = schema.addEntity('Users')
        doc_template.addIdProperty(is_auto=False)
        doc_template.addStringProperty('Name')
        doc_template.addListProperty('Subs')
        # memTemplate.addBoolProperty('IsValid')

        # try:
        dao_generator = DaoGenerator()
        dao_generator.generateAll(schema, self.PROJECT_DIR + '/test/model')


if __name__ == "__main__":
    ModelGenerator().generate_entities()
