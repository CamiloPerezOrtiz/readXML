#library to handle XML documents
from lxml import etree
xmlDocument = etree.parse("pfSense.xml")
root = xmlDocument.getroot()
#open txts needed
txtAlias = open("aliases.txt", "w")
txtInterfaces = open("interfaces.txt", "w")

#find "alias" tag and show its content
for alias in root.iter("alias"):
	aliasName = alias.find("name").text
	aliasType = alias.find("type").text
	aliasAddress = alias.find("address").text 
	aliasDescr = alias.find("descr").text
	aliasDetail = alias.find("detail").text
#Format to .txtAlias
	txtAlias.write(aliasName+"|")
	txtAlias.write(aliasType+"|")
	txtAlias.write(aliasAddress+"|")
	txtAlias.write(aliasDescr+"|")
	txtAlias.write(aliasDetail.replace(" ||", " ")+"|"+"\n")

#"interfaces"
interfacesTag = root.find("interfaces")
for element in interfacesTag:
	txtInterfaces.write(element.tag+"|")
	for tag in element:
		txtInterfaces.write(tag.tag)
		txtInterfaces.write(":")
		txtInterfaces.write(str(tag.text))
		txtInterfaces.write("|")
	txtInterfaces.write("\n")
