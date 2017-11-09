import csv 
import sys
import os
from parserApp.models import Customer

def writeInModels():
	f = os.path.abspath(os.curdir)
	ifile = open(f+ '/parserApp/data/customerdata.txt', 'rt')
	reader = csv.reader(ifile)
	 
	rownum = 0
	colnum = 0
	for row in reader:
	# Save header row.
		if rownum ==0:
			header = row
		else:
			colnum = 0
			cust = Customer(date = row[0],
				phone = int(row[1]),
				name = row[2],
				amount = int(row[3])
				)
			cust.save()
		rownum  = 1 + rownum
	 
	ifile.close()