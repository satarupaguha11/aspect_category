import re,string,sys
from collections import defaultdict
import xml.dom.minidom

modelName = sys.argv[1]
inputPath = '../data/prediction_'+modelName
outputPath = '../data/prediction_'+modelName+'.xml'
XMLPath = '../data/Restaurants_Test_Data_phaseB.xml'

input_file = open(inputPath,'r')
output_file = open(outputPath, 'w')
dictionary = defaultdict(set)

for num,line in enumerate(input_file):
	cats = line.strip().split('\t')[1:]
	print line
	for cat in cats:
		dictionary[line.strip().split('\t')[0]].add(cat)
# dictionary[sentence] will tell the category of that sentence


tree = open(XMLPath, "r")
reviewlines = tree.readlines()
exclude = set(string.punctuation) - set('-')
ourCategories = []
for line in reviewlines:

	if "<text>" in line:
		sentence = re.sub("(<text>)|(</text>)", "", line).strip()
		#sentence = ''.join(ch for ch in sentence if ch not in exclude)
		ourCategories = dictionary[sentence]
		print sentence, ourCategories
		output_file.write(line)

	elif "</sentence>" in line.strip():
		# First write the Categories
		output_file.write("<aspectCategories>\n")
		
		for oc in ourCategories:
			
			if "miscellaneous" == oc:
				oc = "anecdotes/miscellaneous"
			
			output_file.write("<aspectCategory category=\""+oc+"\"/>\n")
		output_file.write("</aspectCategories>\n")
		# Then clean ourCategories
		ourCategories = []
		# And then write </sentence>
		output_file.write(line)
	elif "Categories" in line or "aspectCategory" in line:
		pass
	else:
		# keep writing the line
		output_file.write(line)
	
output_file.close()

#Formatting the XML file properly
output_file = open(outputPath)
xmlvar = xml.dom.minidom.parse(output_file) # or xml.dom.minidom.parseString(xml_string)
prettyXML = xmlvar.toprettyxml()
output_file = open(outputPath, 'w') # I'm writing it again in proper formatted - tabbed XML style
for line in prettyXML.split('\n'):
	if(len(line.strip())>0):
		output_file.write(line+"\n")
output_file.close()