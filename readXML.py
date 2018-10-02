#library to handle XML documents
from lxml import etree


xmlDocument = etree.parse("pfSense.xml") #your xml goes here
root = xmlDocument.getroot()

#find "alias" tag and show its content
txtAlias = open("aliases.txt", "w")
for alias in root.find("aliases"):
	for element in alias:
		txtAlias.write(str(element.text) + ":")
	txtAlias.write("\n")
txtAlias.close()

#find and format "interfaces" tag and its content
txtInterfaces = open("interfaces.txt", "w")
interfacesTag = root.find("interfaces")
for element in interfacesTag:
	txtInterfaces.write(element.tag+"|")
	for tag in element:
		txtInterfaces.write(str(tag.tag))
		txtInterfaces.write(":")
		txtInterfaces.write(str(tag.text))
		txtInterfaces.write("|")
	txtInterfaces.write("\n")
txtInterfaces.close()

# find "SQUIDGUARDDEST" tag and its content
txtSquidguarddest = open("squidguarddest.txt", "w")
installedpackages = root.find("installedpackages")
squidguarddest = installedpackages.find("squidguarddest")
for config in squidguarddest:
	for element in config:
		txtSquidguarddest.write(str(element.text) + ":")
	txtSquidguarddest.write("\n")
txtSquidguarddest.close()

#find "SQUIDGUARDACL tag and its content"
txtSquidguardacl = open("squidguardacl.txt", "w")
squidguardacl = installedpackages.find("squidguardacl")
for config in squidguardacl:
	for element in config:
		txtSquidguardacl.write(str(element.text) + "|")
	txtSquidguardacl.write("\n")
txtSquidguardacl.close()

#find "filter" TAG and its content
txtFilter = open("filter.txt", "w")
filterTag = root.find("filter")
for rule in filterTag:
	txtFilter.write(str(rule.tag) + "|")
	for element in rule:
		if element.tag == "source" or element.tag == "created" or element.tag == "updated" or element.tag == "destination":
			for field in element:
				txtFilter.write(str(element.tag) + "_" + str(field.tag) + ":" + str(field.text) + "|")
		else:
			txtFilter.write(str(element.tag) + ":" + str(element.text) + "|")
	txtFilter.write("\n")
txtFilter.close()

#Nat tag
txtNat = open("nat.txt", "w")
natTag = root.find("nat")
for rule in natTag:
	if rule.tag == "outbound" or rule.tag == "separator":
		for outbound in rule:
			txtNat.write(str(rule.tag) + "_" + str(outbound.tag) + "|" )
			for element in outbound:
				if element.tag == "source" or element.tag == "created" or element.tag == "updated" or element.tag == "destination":
					for field in element:
						txtNat.write(str(element.tag) + "_" + str(field.tag) + ":" + str(field.text) + "|")
				else:
					txtNat.write(str(element.tag) + ":" + str(element.text) + "|")
			txtNat.write("\n")
	else:
		txtNat.write(str(rule.tag) + "|")
		for element in rule:
			if element.tag == "source" or element.tag == "created" or element.tag == "updated" or element.tag == "destination":
				for field in element:
					txtNat.write(str(element.tag) + "_" + str(field.tag) + ":" + str(field.text) + "|")
			else:
				txtNat.write(str(element.tag) + ":" + str(element.text) + "|")
	if rule.tag == "outbound":
		pass
	else:
		txtNat.write("\n")
txtNat.close()