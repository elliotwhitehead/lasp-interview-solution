import csv, json

#open csv as a file object, create csvreader
with open('kerbals.csv', newline='') as kerbalscsv:
	kerbonauts = csv.reader(kerbalscsv)
	
	#load headers, instantiate kerbal roster
	headers = next(kerbonauts)
	roster = []
	
	for kerbal_data in kerbonauts:
		new_kerbal = {}
		for i in range(len(headers)):
			new_kerbal[headers[i]] = kerbal_data[i]
		roster.append(new_kerbal)

	#convert to json array
	jsn = json.dumps(roster)
	print(jsn)