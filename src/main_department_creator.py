from testMongoGen_DaoMaster import DaoMaster
from CatalogDepartment import CatalogDepartment

if __name__ == "__main__":
    dao_master = DaoMaster()
    dao_session = dao_master.getSession()
    catalog_department_dao = dao_session.getCatalogDepartmentDao()

    depto1 = CatalogDepartment()
    depto1.setName('ID')
    depto2 = CatalogDepartment()
    depto2.setName('ART')
    depto3 = CatalogDepartment()
    depto3.setName('ILLUSTRATION')
    depto4 = CatalogDepartment()
    depto4.setName('MODELING')
    depto5 = CatalogDepartment()
    depto5.setName('RIGGING')
    depto6 = CatalogDepartment()
    depto6.setName('ANIMATION')
    depto7 = CatalogDepartment()
    depto7.setName('RENDER')

    list_dptos = [depto1, depto2, depto3, depto4, depto5, depto6, depto7]

    catalog_department_dao.createCollection(list_dptos)
