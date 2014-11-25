import csv
with open('data/911truth.csv') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		print(row['title'])