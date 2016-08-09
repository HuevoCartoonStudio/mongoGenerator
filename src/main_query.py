import sys

from testMongoGen_DaoMaster import DaoMaster
from testMongoGen_DaoSession import DaoSession
from Items import Items
from CatalogItemType import CatalogItemType
from CatalogFormatType import CatalogFormatType
from ItemsDao import ItemsDao

from random import randint

if __name__ == "__main__":
	dao_master = DaoMaster()
	dao_session = dao_master.getSession()
	items_dao = dao_session.getItemsDao()
	catalog_item_type_dao = dao_session.getCatalogItemTypeDao()
	catalog_format_type_dao = dao_session.getCatalogFormatTypeDao()
	catalog_status_type_dao = dao_session.getCatalogStatusTypeDao()
	users_dao = dao_session.getUsersDao()

	super_asset = items_dao.readOneByProperty(items_dao.Properties.Name, 'SuperAsset_333')
	print(super_asset.getAssetSubscriptions())
	list_assets = items_dao.readByPropertyValues(items_dao.Properties.Id, super_asset.getAssetSubscriptions())
	for la in list_assets:
		print (la.getName())
		list_items = items_dao.readByPropertyValues(items_dao.Properties.Id, la.getItemSubscriptions())
		for li in list_items:
			print ('\t' + li.getName())
