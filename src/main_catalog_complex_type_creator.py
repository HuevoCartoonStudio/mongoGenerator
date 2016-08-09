from testMongoGen_DaoMaster import DaoMaster
from CatalogComplexType import CatalogComplexType

if __name__ == "__main__":
    dao_master = DaoMaster()
    dao_session = dao_master.getSession()
    catalog_item_type_dao = dao_session.getCatalogComplexTypeDao()

    catalog_item_type = CatalogComplexType()
    catalog_item_type.setId(0)
    catalog_item_type.setComplexType('low')
    catalog_item_type_dao.create(catalog_item_type)
    catalog_item_type.setId(1)
    catalog_item_type.setComplexType('medium')
    catalog_item_type_dao.create(catalog_item_type)
    catalog_item_type.setId(2)
    catalog_item_type.setComplexType('high')
    catalog_item_type_dao.create(catalog_item_type)
