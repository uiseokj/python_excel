import sys

import pandas as pd
from pandas import DataFrame

def main(filePath, fileName):
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
	if (len(sys.argv) < 3):
		print("Usage: python3 read_excel_pandas.py filepath filename")
		sys.exit()

	main(sys.argv[1], sys.argv[2])
