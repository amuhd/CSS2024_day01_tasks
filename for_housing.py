import pandas

file = pandas.read_csv("housing_data.csv")

print(file)

print(file.info())

df = pandas.read_csv("housing_data.csv")

print(df.describe())