import random, csv
import numpy as np

with open('stops.csv', newline='') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	count = 0
	stops = []
	veto_list_miguelito = ["Hermannplatz", "Rathaus Neukölln", "Sonnenallee"]
	veto_list_ethanito = ["Kleistpark", "Julius-Leber-Brücke"]
	for row in reader:
		if "(Berlin)" in str(row):
			if row[2] not in stops and not np.any([veto in row[2] for veto in veto_list_miguelito]):
				count += 1
				stops.append(row[2])
	print(random.choice(stops))
	print("COUNT is " + str(count))