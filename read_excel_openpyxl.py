import sys

import openpyxl
import pandas as pd
from pandas import DataFrame

def main(filePath, fileName):
	print(fileName)
	fileNameTemp1 = fileName.split(".")
	fileNameTemp2 = fileNameTemp1[0].split("_")

	yearMonth = fileNameTemp2[1]
	print("YearMonth: " + yearMonth)
	
	wb = openpyxl.load_workbook(filePath)
	print(wb.sheetnames)


if __name__ == "__main__":
	if (len(sys.argv) < 3):
		print("Usage: python3 read_excel_openpyxl.py filepath filename")
		sys.exit()

	main(sys.argv[1], sys.argv[2])
