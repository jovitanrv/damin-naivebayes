# import numpy as np
import pandas as pd

def readcsv():
	data = pd.read_csv("data_latih.csv",delimiter=',')
	return data

a = readcsv()
print(a)

# def readData_uji():
# 	