from pandas import read_csv
data = read_csv("/home/gempak/Krishnapatnam.csv",index_col=0)
print(data.head())