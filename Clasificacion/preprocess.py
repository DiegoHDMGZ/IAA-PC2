import csv
nameFile = 'fallecidos_sinadef.csv'
nameFileOutput = 'fallecidos_sinadef_procesado.csv'
input_file = open(nameFile, 'r')
output_file = open(nameFileOutput, 'w', newline='')
data = csv.reader(input_file, delimiter = ';')
writer = csv.writer(output_file, delimiter = ';')
specials = '\''
specials2 = '\"'

firstLine = True
for line in data:
	line = [value.replace(specials, '').replace(specials2, '') for value in line]
	row = line[:19]
	causeOfDeath = line[19:]
	isCovid = "NO"
	for word in causeOfDeath:
		if word.find("COVID") != -1:
			isCovid = "SI"
	
	if firstLine:
		row.append("MUERTE POR COVID")
		firstLine = False
	else:
		row.append(isCovid)
	
	missingAge = False
	if row[3] == "SIN REGISTRO":
		missingAge = True
	if not missingAge:
		writer.writerow(row)


