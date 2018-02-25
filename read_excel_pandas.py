# -*- coding: utf-8 -*-

import os
import sys

import pandas as pd
from pandas import DataFrame

def main(dirName):
	for root, dirs, files in os.walk(dirName):
		for fileName in files:
			filePath = os.path.join(root, fileName)

			read_excel(filePath, fileName)

def read_excel(filePath, fileName):
	print(fileName)
	fileNameTemp1 = fileName.split(".")
	fileNameTemp2 = fileNameTemp1[0].split("_")

	yearMonth = fileNameTemp2[1]
	print("YearMonth: " + yearMonth)
	
	data = pd.read_excel(filePath, names=['stnCd', 'stnNm', 'startTm', 'endTm', 'isNew', 'isMoving', 'obsStartTm', 'lat', 'lon'])
	data['yearMonth'] = yearMonth
	data = DataFrame(data, columns = ['yearMonth', 'stnCd', 'lat', 'lon'])
	data.to_csv('stn_list_by_yearmonth.csv', sep=',', header=False, index=False, mode='a')


if __name__ == "__main__":
	if (len(sys.argv) < 2):
		print("Usage: python3 read_excel_pandas.py dir")
		sys.exit()

	main(sys.argv[1])
