import sys
import datetime
import time

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

	list_it_types = catalog_item_type_dao.readAll()
	format_type = catalog_format_type_dao.readRandom()
	list_catalog_status_type = catalog_status_type_dao.readAll()
	list_users = users_dao.readAll()

	list_items = []

	number_items = 10000

	for j in range(number_items):
		time.sleep(0.001)
		item_item = Items()
		# item_item.setId(i)
		item_item.setClass(0)
		item_item.setName('Item_' + str(j))
		item_item.setPath('Path_' + str(j))
		item_item.setDateTime(datetime.datetime.now())
		item_item.setType(list_it_types[randint(0, len(list_it_types) - 1)].getId())
		item_item.setFormat(randint(0, len(format_type.getField(list_it_types[item_item.getType()].getItemType())) - 1))
		item_item.setStatus(list_catalog_status_type[randint(0, len(list_catalog_status_type) - 1)].getId())
		item_item.setVersion(0.1)
		item_item.setPrevVersion('')
		item_item.setNextVersion('')
		for i in range(0, randint(0, len(list_users) - 1)):
			item_item.addUserSubscription(randint(0, len(list_users) - 1))

		list_items.append(item_item)

	items_dao.createCollection(list_items)
