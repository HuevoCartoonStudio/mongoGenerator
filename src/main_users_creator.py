from testMongoGen_DaoMaster import DaoMaster
from Users import Users

if __name__ == "__main__":
    dao_master = DaoMaster()
    dao_session = dao_master.getSession()
    users_dao = dao_session.getUsersDao()

    # user = Users()
    # user.setName('Raul')
    # user.setDepartment('ID')
    # users_dao.create(user)
    # user = Users()
    # user.setName('Fidel')
    # user.setDepartment('ID')
    # users_dao.create(user)
    # user = Users()
    # user.setName('Alberto')
    # user.setDepartment('ID')
    # users_dao.create(user)
    # user = Users()
    # user.setName('Juan')
    # user.setDepartment('Arte')
    # users_dao.create(user)

    # user = users_dao.readOneByProperty(users_dao.Properties.Name, 'Juan')
    # users_dao.delete(user)

    user1 = Users()
    user1.setName('Raul')
    user1.setDepartment(0)
    user1.setEmail('asdf@asdf')
    user1.setIsActive(True)
    user2 = Users()
    user2.setName('Fidel')
    user2.setDepartment(0)
    user2.setEmail('asdf@asdf')
    user2.setIsActive(True)
    user3 = Users()
    user3.setName('Alberto')
    user3.setDepartment(0)
    user3.setEmail('asdf@asdf')
    user3.setIsActive(True)
    user4 = Users()
    user4.setName('Juan')
    user4.setDepartment(1)
    user4.setEmail('asdf@asdf')
    user4.setIsActive(True)

    list_users = [user1, user2, user3, user4]

    users_dao.createCollection(list_users)



