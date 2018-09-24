#library to handle XML documents
from lxml import etree
xmlDocument = etree.parse("pfSense.xml")
root = xmlDocument.getroot()

#find "alias" tag and show its content
txtAlias = open("aliases.txt", "w")
for alias in root.iter("alias"):
	aliasName = str(alias.find("name").text)
	aliasType = str(alias.find("type").text)
	aliasAddress = str(alias.find("address").text )
	aliasDescr = str(alias.find("descr").text)
	aliasDetail = str(alias.find("detail").text)
####Format to .txtAlias
	txtAlias.write(aliasName+"|")
	txtAlias.write(aliasType+"|")
	txtAlias.write(aliasAddress+"|")
	txtAlias.write(aliasDescr+"|")
	string = str(aliasDetail.replace(" ||", " ")+"|"+"\n")
	txtAlias.write(string.replace("||", "|"))
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

# find "SQUIDGUARDDEST" tags and its content
txtSquidguarddest = open("squidguarddest.txt", "w")
installedpackages = root.find("installedpackages")
squidguarddest = installedpackages.find("squidguarddest")
for config in squidguarddest:
	configName = str(config.find("name").text)
	configDomains = str(config.find("domains").text)
	configUrls = str(config.find("urls").text)
	configExpressions = str(config.find("expressions").text)
	configRedirect_mode = str(config.find("redirect_mode").text)
	configRedirect = str(config.find("redirect").text)
	configDescription = str(config.find("description").text)
	configEnablelog = str(config.find("enablelog").text)
#####format and write on txt
	txtSquidguarddest.write(configName + "|")
	txtSquidguarddest.write(configDomains + "|")
	txtSquidguarddest.write(configUrls)
	txtSquidguarddest.write(configExpressions)
	txtSquidguarddest.write(configRedirect_mode + "|")
	txtSquidguarddest.write(configRedirect + "|")
	txtSquidguarddest.write(configDescription + "|")
	txtSquidguarddest.write(configEnablelog + "|")
	txtSquidguarddest.write("\n")
txtSquidguarddest.close()

#"SQUIDGUARDACL"
txtSquidguardacl = open("squidguardacl.txt", "w")
squidguardacl = installedpackages.find("squidguardacl")
for config in squidguardacl:
	configDisable = str(config.find("disabled").text)
	configName = str(config.find("name").text)
	configSource = str(config.find("source").text)
	configTime = str(config.find("time").text)
	configDest = str(config.find("dest").text)
	configNotallowingip = str(config.find("notallowingip").text)
	configRedirect_mode = str(config.find("redirect_mode").text)
	configRedirect = str(config.find("redirect").text)
	configSafesearch = str(config.find("safesearch").text)
	configRewrite = str(config.find("rewrite").text)
	configOverrewrite = str(config.find("overrewrite").text)
	configDescription = str(config.find("description").text)
	configEnablelog = str(config.find("enablelog").text)
####Format and write on txt
	txtSquidguardacl.write(configDisable + "|")
	txtSquidguardacl.write(configName + "|")
	txtSquidguardacl.write(configSource + "|")
	txtSquidguardacl.write(configTime + "|")
	txtSquidguardacl.write(configDest + "|")
	txtSquidguardacl.write(configNotallowingip + "|")
	txtSquidguardacl.write(configRedirect_mode + "|")
	txtSquidguardacl.write(configRedirect + "|")
	txtSquidguardacl.write(configSafesearch + "|")
	txtSquidguardacl.write(configRewrite + "|")
	txtSquidguardacl.write(configOverrewrite + "|")
	txtSquidguardacl.write(configDescription + "|")
	txtSquidguardacl.write(configEnablelog + "|")
	txtSquidguardacl.write("\n")
txtSquidguardacl.close()

