import pandas

file = pandas.read_csv("iris.csv")

print(file)

print(file.info())

df = pandas.read_csv("iris.csv")

print(df.describe)