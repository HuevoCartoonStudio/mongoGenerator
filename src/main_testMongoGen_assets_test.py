import sys

from testMongoGen_DaoMaster import DaoMaster
from testMongoGen_DaoSession import DaoSession
from Items import Items
from CatalogItemType import CatalogItemType
from CatalogFormatType import CatalogFormatType
from ItemsDao import ItemsDao

from random import randint
import datetime
import time

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
	number_assets = 1000

	for j in range(number_assets):
		time.sleep(.001)
		item_item = Items()
		# item_item.setId(i)
		item_item.setClass(1)
		item_item.setName('Asset_' + str(j))
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

	for j in range(number_assets):
		numbersito = randint(1, 11)
		# numbersito = 1
		list_id_subscript_itemes = []
		list_subscript_itemes = []

		for i in range(numbersito):
			list_id_subscript_itemes.append(randint(0, number_items))

		for k in list_id_subscript_itemes:
			itemp_temp = items_dao.readOneByProperty(items_dao.Properties.Name, 'Item_' + str(k))
			if itemp_temp is not None:
				list_subscript_itemes.append(itemp_temp)
			# print (item_temp.getId())

		for l in list_subscript_itemes:
			list_items[j].addItemSubscription(l.getId())
			l.addAssetSubscription(list_items[j].getId())
			items_dao.update(l)
			# print('hello' + str(l))

	items_dao.updateCollection(list_items)