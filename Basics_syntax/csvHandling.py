import csv
with open("csvData.csv") as csvf:
	fileData = csv.reader(csvf,delimiter=',')

	names=[]
	ages = []
	favs = []

	for row in fileData:
		name = row[0]
		age = row[1]
		fav = row[2]
		names.append(name)
		ages.append(age)
		favs.append(fav)
	print(names)
	print(ages)
	print(favs)
	print(names[0])
try:
	inPut = raw_input('Enter the persons name for getting his details:')

	indexOf = names.index(inPut)
	#print(indexOf)
	print('Age:'+str(ages[indexOf])+' OS:'+str(favs[indexOf]))

except Exception as e:
	print(e)

