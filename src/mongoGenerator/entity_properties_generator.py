from entity import Entity


class EntityPropertiesGenerator:
    def __init__(self, entity, directory):
        self.__entity = entity
        self.__directory = directory

    def setEntity(self):
        return self.__entity

    def generate(self):
        self._generateModel()

    def _generateModel(self):
        model_file = open(self.__directory + "/" + self.__entity.getName() + "Properties.py", "wb")

        self._generateModelHeader(model_file)
        self._generateModelData(model_file)

        model_file.close()

    def _generateModelHeader(self, model_file):
        # model_file.write('from collections import Counter\n\n')
        model_file.write('class ' + self.__entity.getName() + 'Properties:\n')
        model_file.write('\tdef __init__(self):\n')

    def _generateModelData(self, model_file):
        # if (self.__entity.getIsPrimaryKey()):
        # model_file.write('\"_id\" : 0, ')

        for p in self.__entity.getIntProperties():
            model_file.write('\t\tself.' + p + ' = \'' + p + '\'\n')

        for p in self.__entity.getFloatProperties():
            model_file.write('\t\tself.' + p + ' = \'' + p + '\'\n')

        for p in self.__entity.getStringProperties():
            model_file.write('\t\tself.' + p + ' = \'' + p + '\'\n')

        for p in self.__entity.getBoolProperties():
            model_file.write('\t\tself.' + p + ' = \'' + p + '\'\n')

        for p in self.__entity.getListProperties():
            model_file.write('\t\tself.' + p + ' = \'' + p + '\'\n')

