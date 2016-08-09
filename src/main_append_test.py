import sys

from testMongoAppend_DaoMaster import DaoMaster
from testMongoAppend_DaoSession import DaoSession
from ItemsTest import ItemsTest
from ItemsTestDao import ItemsTestDao

if __name__ == "__main__":
    dao_master = DaoMaster()
    dao_session = dao_master.getSession()
    items_dao = dao_session.getItemsTestDao()

    # item = ItemsTest()
    # item.setId(0)
    # item.setName('Raul')
    # item.setPath('/home/root')
    # items_dao.create(item)

    item = items_dao.readRandom()
    print (item.getField('Status'))
    # item.setField('Status', 'go')
    item.appendData('Version', 2)
    items_dao.update(item)