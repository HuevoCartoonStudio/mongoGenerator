from testMongoGen_DaoMaster import DaoMaster
from CatalogStatusType import CatalogStatusType

if __name__ == "__main__":
    dao_master = DaoMaster()
    dao_session = dao_master.getSession()
    catalog_item_type_dao = dao_session.getCatalogStatusTypeDao()

    catalog_item_type = CatalogStatusType()
    catalog_item_type.setId(0)
    catalog_item_type.setStatusType('rejected')
    catalog_item_type_dao.create(catalog_item_type)
    catalog_item_type.setId(1)
    catalog_item_type.setStatusType('deprecated')
    catalog_item_type_dao.create(catalog_item_type)
    catalog_item_type.setId(2)
    catalog_item_type.setStatusType('outdated')
    catalog_item_type_dao.create(catalog_item_type)
    catalog_item_type.setId(3)
    catalog_item_type.setStatusType('variation')
    catalog_item_type_dao.create(catalog_item_type)
    catalog_item_type.setId(4)
    catalog_item_type.setStatusType('current')
    catalog_item_type_dao.create(catalog_item_type)
