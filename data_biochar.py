import xlrd
from collections import Counter
import numpy as np

def removeDashes(arr):
	'''
	Some 0 values appear as '--' in excel
	Return:
	- list with '--' replaced by 0.0
	'''
	for idx, item in enumerate(arr):
		if item == '--':
			arr[idx] = 0.0

	return arr

def containsNegative(arr):
	'''Preprocessing data step
	Check if features contain a negative number.
	Return:
	- True if the features do
	_ False otherwise
	'''
	for idx, item in enumerate(arr):
		if item < 0:
			return True

	return False


def getFeaturesAndY(worksheet, i:int):
	'''
	Extract features and y labels form the excel files
	return
	- X: list of features values
	- y
	'''
	features = [
			worksheet.cell(i, 1).value,
			worksheet.cell(i, 2).value,
			worksheet.cell(i, 3).value,

			worksheet.cell(i, 4).value,
			worksheet.cell(i, 5).value,
			worksheet.cell(i, 6).value,
			worksheet.cell(i, 7).value,

			worksheet.cell(i, 8).value,

			worksheet.cell(i, 9).value,
			worksheet.cell(i, 10).value,
			worksheet.cell(i, 11).value,
	]

	'''
	For uncertain values in excel sheet, average value is used for analysis
	'''
	for idx, item in enumerate(features):
		if isinstance(features[idx], str):
			features[idx] = item.split('-')
			features[idx] = [float(i) for i in features[idx]]
			features[idx] = sum(features[idx]) / float(len(features[idx]))

	y = [
		worksheet.cell(i, 12).value
	]
	return features, y

def getBioCharYieldData():
	'''
	Extract biochar yield data
	Return:
	- trainX: training set features
	- trainY: training set catgories
	- testX: test set features
	- testY: test set categories
	'''
	workbook = xlrd.open_workbook('biochar/data.xlsx', on_demand = True)
	worksheet = workbook.sheet_by_name('biochar yield')
	trainX = []
	trainY = []
	testX = []
	testY = []
	n_start = 2
	n_div = int((worksheet.nrows - n_start)/ 10)
	for i in range(n_start, worksheet.nrows):
		features, y = getFeaturesAndY(worksheet, i)
		if i % n_div == 0:
			testX.append(features)
			testY.append(y)
		else:
			trainX.append(features)
			trainY.append(y)

	return np.array(trainX), np.array(trainY), np.array(testX), np.array(testY)

def getBioCharSAData():
	'''
	Extract biochar 
	Return:
	- trainX: training set features
	- trainY: training set catgories
	- testX: test set features
	- testY: test set categories
	'''
	workbook = xlrd.open_workbook('biochar/data.xlsx', on_demand = True)
	worksheet = workbook.sheet_by_name('surface area')
	trainX = []
	trainY = []
	testX = []
	testY = []
	n_start = 2
	n_div = int((worksheet.nrows - n_start)/ 10)
	for i in range(n_start, worksheet.nrows):
		features, y = getFeaturesAndY(worksheet, i)
		if i % n_div == 0:
			testX.append(features)
			testY.append(y)
		else:
			trainX.append(features)
			trainY.append(y)

	return np.array(trainX), np.array(trainY), np.array(testX), np.array(testY)

# trainX, trainY, testX, testY = getBioCharData()

