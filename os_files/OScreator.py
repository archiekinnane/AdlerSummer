from os_files import asset_creator
from os_files import speck_creator


  
#initialize with name of table and desired file name with NO extension. e.g. test will create test.speck and test.asset
def createFiles(Table, file_name, GUI_name = 'default', GUI_path = 'default', source = 'default'):
	asset_creator.makeAsset(file_name, GUI_name, GUI_path)
	speck_creator.makeSpeck(Table, file_name, source)
	
	



def printArgs():
    print("createFiles(Table, file_name, GUI_name = 'default', GUI_path = 'default', source = 'default')")