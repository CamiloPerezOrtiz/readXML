#library to handle XML documents
from lxml import etree


xmlDocument = etree.parse("pfSense.xml") #your xml goes here
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

#Filter TAG
txtFilter = open("filter.txt", "w")
filterTag = root.find("filter")
for rule in filterTag:
	txtFilter.write(str(rule.tag) + "|")
	#***********************************
	if str(rule.tag) != "rule":  #this is for separator Tag
		for field in rule:
			txtFilter.write(str(field.tag) + ":" + str(field.text) + "|") 
	#***********************************  this all is for rule Tag
	if rule.find("id") is not None:
		txtFilter.write(str(rule.find("id").tag) + ":" + str(rule.find("id").text) + "|")
		txtFilter.write(str(rule.find("tracker").tag) + ":" + str(rule.find("tracker").text) + "|")
		txtFilter.write(str(rule.find("type").tag) + ":" + str(rule.find("type").text) + "|")
		txtFilter.write(str(rule.find("interface").tag) + ":" + str(rule.find("interface").text) + "|")
		txtFilter.write(str(rule.find("ipprotocol").tag) + ":" + str(rule.find("ipprotocol").text) + "|")
		txtFilter.write(str(rule.find("tag").tag) + ":" + str(rule.find("tag").text) + "|")
		txtFilter.write(str(rule.find("tagged").tag) + ":" + str(rule.find("tagged").text) + "|")
		txtFilter.write(str(rule.find("max").tag) + ":" + str(rule.find("max").text) + "|")
		txtFilter.write(str(rule.find("max-src-nodes").tag) + ":" + str(rule.find("max-src-nodes").text) + "|")
		txtFilter.write(str(rule.find("max-src-conn").tag) + ":" + str(rule.find("max-src-conn").text) + "|")
		txtFilter.write(str(rule.find("max-src-states").tag) + ":" + str(rule.find("max-src-states").text) + "|")
		txtFilter.write(str(rule.find("statetimeout").tag) + ":" + str(rule.find("statetimeout").text) + "|")
		txtFilter.write(str(rule.find("statetype").tag) + ":" + str(rule.find("statetype").text) + "|")
		txtFilter.write(str(rule.find("os").tag) + ":" + str(rule.find("os").text) + "|")
		#txtFilter.write(str(rule.find("source").tag) + ":" + str(rule.find("source").text) + "|")  ***Etiqueta pendiente
		#txtFilter.write(str(rule.find("destination").tag) + ":" + str(rule.find("destination").text) + "|")  ***Etiqueta pendiente
		txtFilter.write(str(rule.find("descr").tag) + ":" + str(rule.find("descr").text) + "|")
		for fields in rule.find("created"): 
			txtFilter.write("created_"+str(fields.tag) + ":" + str(fields.text) + "|")
		for fields in rule.find("updated"): 
			txtFilter.write("updated_"+str(fields.tag) + ":" + str(fields.text) + "|")
	#***********************************
	elif rule.find("type") is not None:
		for fields in rule:
			if str(fields.tag) == "source":
				for field in fields:
					txtFilter.write("source" + str(field.tag) + ":" + str(field.text) + "|")
			elif str(fields.tag) == "destination":
				for field in fields:
					txtFilter.write("destination_" + str(field.tag) + ":" + str(field.text) + "|")
			else:
				txtFilter.write(str(fields.tag) + ":" + str(fields.text) + "|")
	#***********************************
	elif rule.find("associated-rule-id") is not None:
		for fields in rule:
			if str(fields.tag) == "source":
				 for field in fields:
					txtFilter.write("source_" + str(field.tag) + ":" + str(field.text) + "|")
			elif str(fields.tag) == "destination":
				for field in fields:
					txtFilter.write("destination_" + str(field.tag) + ":" + str(field.text) + "|")
			elif str(fields.tag) == "created":
				for field in fields:
					txtFilter.write("created_" + str(field.tag) + ":" + str(field.text) + "|") 
			elif str(fields.tag) == "updated":
				for field in fields:
					txtFilter.write("updated_" + str(field.tag) + ":" + str(field.text) + "|")
			else:
				txtFilter.write(str(fields.tag) + ":" + str(fields.text) + "|")
	else:
		pass
	txtFilter.write("\n")
txtFilter.close()

#Nat tag
txtNat = open("nat.txt", "w")
natTag = root.find("nat")
for rule in natTag:
	#***********************************
	if str(rule.tag) == "outbound":
		for outbound in rule:
			txtNat.write(str(rule.tag) +"_rule" + "|")
			for fields in outbound:
				if fields.tag == "source":
					for field in fields:
						txtNat.write("source_" + str(field.tag) + ":" + str(field.text) + "|")
				elif fields.tag == "destination":
					for field in fields:
						txtNat.write("destination_" + str(field.tag) + ":" + str(field.text) + "|")
				elif fields.tag == "created":
					for field in fields:
						txtNat.write("created_" + str(field.tag) + ":" + str(field.text) + "|")
				elif fields.tag == "updated":
					for field in fields:
						txtNat.write("updeted_" + str(field.tag) + ":" + str(field.text) + "|")
				else:
					txtNat.write(str(fields.tag) + ":" + str(fields.text) + "|")
			txtNat.write("\n")
	
	#***********************************
	elif str(rule.tag) == "separator":
		

		for separator in rule:
			txtNat.write("separator_" + str(separator.tag) + "|")
			
			for fields in separator:
	

				txtNat.write(str(fields.tag) + ":" + str(fields.text) + "|")
			txtNat.write("\n")			

	else:
		txtNat.write(str(rule.tag) + "|")

	if str(rule.tag) == "rule":
		for fields in rule:
			if fields.tag == "source":
				for field in fields:
					txtNat.write("source_" + str(field.tag) + ":" + str(field.text) + "|")
			elif fields.tag == "destination":
				for field in fields:
					txtNat.write("destination_" + str(field.tag) + ":" + str(field.text) + "|")
			elif fields.tag == "created":
				for field in fields:
					txtNat.write("created_" + str(field.tag) + ":" + str(field.text) + "|")
			elif fields.tag == "updated":
				for field in fields:
					txtNat.write("updeted_" + str(field.tag) + ":" + str(field.text) + "|")
			else:
				txtNat.write(str(fields.tag) + ":" + str(fields.text) + "|")
	#***********************************
	elif str(rule.tag) == "onetoone":
		for fields in rule:
			if fields.tag == "source":
				for field in fields:
					txtNat.write("source_" + str(field.tag) + ":" + str(field.text) + "|")
			elif fields.tag == "destination":
				for field in fields:
					txtNat.write("destination_" + str(field.tag) + ":" + str(field.text) + "|")
			else:
				txtNat.write(str(fields.tag) + ":" + str(fields.text) + "|")
	#***********************************
	elif rule.tag == "separator":
		pass



	if str(rule.tag) == "outbound":
		pass
	else:
		txtNat.write("\n")
txtNat.close()