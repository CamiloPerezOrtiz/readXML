#library to handle XML documents
from lxml import etree


xmlDocument = etree.parse("pfSense.xml") #your xml goes here
root = xmlDocument.getroot()

check = 1

def eachTag_eachValue(rootTag):
	for tag in rootTag:

		if tag.text == '\n\t\t\t' :
			txtNat.write("\n")
			txtNat.write(str(tag.tag) + "|")
		elif tag.text == '\n\t\t\t\t':
			txtNat.write(str(tag.tag)) 
		else:
			txtNat.write(":" + str(tag.text) + ":" + str(tag.text) + "|")		
		eachTag_eachValue(tag)
		







#"nat" tag
txtNat = open("nat.txt", "w")
natTag = root.find("nat")




eachTag_eachValue(natTag)

txtNat.close()
