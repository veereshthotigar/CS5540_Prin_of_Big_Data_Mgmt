import re
textTemp = ""
# Open/Create a file to append data
textFile = open('spacex.txt', 'a+')

with open('spacex.csv','Ur') as file:
    for line in file:
	textTemp = ""
	extractedData = re.findall(r'[#@][^\s#@]+', line) 
	extractedData += re.findall("(?P<url>https?://[^\s]+)",line)
	print extractedData
	for data in extractedData:
	    textTemp += " "+data
        textFile.write(textTemp)

#close file
textFile.close()

