import csv, json, math

#Optional: Decode transformed stupidity / courage values
def un_transform(data):
	num = (float)(data)
	return round((math.atan(num)+(math.pi/2))*(100/math.pi))

#open csv as a file object, create csvreader
with open('kerbals.csv', newline='') as kerbalscsv:
	kerbonauts = csv.reader(kerbalscsv)
	
	#load headers, instantiate kerbal roster
	headers = next(kerbonauts)
	roster = []
	
	for kerbal_data in kerbonauts:
		new_kerbal = {}
		for i in range(len(headers)):
			#translate courage and stupidity to human-friendly values (percentage)
			if(headers[i] == "Courage" or headers[i] == "Stupidity"):
				new_kerbal[headers[i]] = un_transform(kerbal_data[i])
			else:
				new_kerbal[headers[i]] = kerbal_data[i]
		roster.append(new_kerbal)

	#convert to json array
	jsn = json.dumps(roster)
	print(jsn)