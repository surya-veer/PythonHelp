import csv
with open('data.csv') as csvfile:
	readcsv = csv.reader(csvfile, delimiter = ',')
	for row in readcsv:
		print(row)
