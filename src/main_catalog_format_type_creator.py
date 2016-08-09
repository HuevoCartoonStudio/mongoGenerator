from testMongoGen_DaoMaster import DaoMaster
from CatalogFormatType import CatalogFormatType

if __name__ == "__main__":
    dao_master = DaoMaster()
    dao_session = dao_master.getSession()
    catalog_item_type_dao = dao_session.getCatalogFormatTypeDao()

    catalog_format_type = CatalogFormatType()
    catalog_format_type.setId(0)
    catalog_format_type.addSRC('.py')
    catalog_format_type.addSRC('.ui')
    catalog_format_type.addSRC('.sh')
    catalog_format_type.addSRC('.cpp')
    catalog_format_type.addSRC('.h')

    catalog_format_type.addPRO('.ma')

    catalog_format_type.addENV('.ma')

    catalog_format_type.addCHR('.ma')

    catalog_format_type.addRIG('.ma')

    catalog_format_type.addFXS('.ma')
    catalog_format_type.addFXS('.hips')

    catalog_format_type.addTEM('.ma')
    catalog_format_type.addTEM('.hip')
    catalog_format_type.addTEM('.nk')
    catalog_format_type.addTEM('.mr')

    catalog_format_type.addGEO('.ma')
    catalog_format_type.addGEO('.mb')
    catalog_format_type.addGEO('.abc')
    catalog_format_type.addGEO('.bgeo')
    catalog_format_type.addGEO('.fbx')

    catalog_format_type.addART('.tif')
    catalog_format_type.addART('.jpg')
    catalog_format_type.addART('.png')
    catalog_format_type.addART('.tx')

    catalog_format_type.addSHD('.ma')

    catalog_format_type.addTEX('.tif')
    catalog_format_type.addTEX('.tx')

    catalog_format_type.addCCH('.abc')
    catalog_format_type.addCCH('.bgeo')
    catalog_format_type.addCCH('.sim')

    catalog_format_type.addSQI('.tif')
    catalog_format_type.addSQI('.exr')

    catalog_format_type.addDCC('.ma')
    catalog_format_type.addDCC('.mb')
    catalog_format_type.addDCC('.hip')
    catalog_format_type.addDCC('.mri')
    catalog_format_type.addDCC('.nk')

    catalog_format_type.addNON('default')
    catalog_item_type_dao.create(catalog_format_type)
