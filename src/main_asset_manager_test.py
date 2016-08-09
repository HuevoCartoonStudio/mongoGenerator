import sys

from DaoMaster import DaoMaster
from DaoSession import DaoSession
from Items import Items
from ItemsDao import ItemsDao

if __name__ == "__main__":
	dao_master = DaoMaster()
	dao_session = dao_master.getSession()
	items_dao = dao_session.getItemsDao()

	# for i in range(3):
	# 	item = Items()
	# 	item.setId(i)
	# 	item.setName('Name_' + str(i))
	# 	item.setPath('Path_' + str(i))
	# 	item.setAssetSubscription('AssetSubscription_' + str(i))
	# 	item.setSuperAssetSubscription('SuperAssetSubscription_' + str(i))
	# 	item.setDigitalMediaSubscription('DigitalMediaSubscription_' + str(i))
	# 	item.setArtSubscription('ArtSubscription_' + str(i))
	# 	item.setUserSubscription('UserSubscription_' + str(i))
	# 	item.setType('Type_' + str(i))
	# 	item.setFormat('Format_' + str(i))
	# 	item.setStatus(i)
	# 	item.setVersion(float(i))
	# 	items_dao.create(item)

	sadf = items_dao.readOneByPropertie(items_dao.Properties.Status, 2)
	print(sadf.getId())

	# item = items_dao.readAll()
	# print(items_dao.deleteCollection(item))

	#print ('Count ' + str(items_dao.count()))

	#items_dao.deleteAll()

	#print (items_dao.readFirst().getId())

	#test_all = items_dao.readAll()
	#print(len(test_all))

	#test_all = items_dao.readByQuery({'_id': {'$lt': 50000}})
	#test_all = items_dao.readByQuery({'Name':'Name_19132'})
	#print(test_all[0].getField('Name'))
	#print(len(test_all))

	#print('Number fields' + str(users_dao.getFieldCount()))

	#a = ''
	#if (a is ''):
		#print ('is empty')

	# test_all = items_dao.readAll()
	#
	# for i in range(len(test_all)):
	# 	test_all[i].setName('Namesito_' + str(i))
	# 	items_dao.update(test_all[i])