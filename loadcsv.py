#! /usr/bin/python3
import csv

with open('marketing-data.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		print(row)

