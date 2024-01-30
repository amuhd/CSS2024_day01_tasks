import pandas

file = pandas.read_csv("diab_data.csv")

print(file)

print(file.info())

df = pandas.read_csv("diab_data.csv")

print(df.describe())