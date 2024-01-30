# Storing Data
B1 = 30
B2 = 40
B3 = 30
B4 = 49
B5 = 22
B6 = 35
B7 = 22
B8 = 46
B9 = 29
B10 = 25
B11 = 39

print(B1)
print(B2)
print(B3)
print(B4)
print(B5)
print(B6)
print(B7)
print(B8)
print(B9)
print(B10)
print(B11)

# Using List
age = [30,40,30,49,22,35,22,46,29,25,35]
print(age)

# List indexes start at 0 which has a value of 30
print(age[0])
print(age[1])
print(age[10])

# Basic Stats
age = [30,40,30,49,22,35,22,46,29,25,35]
print(min(age))
print(max(age))
print(len(age))
print(sum(age))
average = sum(age)/len(age)
print(average)

# Gender List
gender = ["M","M","F","M","F","F","F","M","M","F","M"]
print(gender[0])
print(gender[1])
print(gender[2])
print(gender[-1])

# Data Storage With Lists
my_list = [42, -2021, 6.238, "tau", "node"]
print(my_list)

my_list.append("hair")

print(my_list)

my_list.insert(1, "pi")

print(my_list)

print(len(my_list))

# View Certain Range In List: Slicing
print(my_list[0:4])


import pandas as pd

# Creating a DataFrame
data = {'age': [30,40,30,49,22,35,22,46,29,25,39],
        'gender': ["M","M","F","M","F","F","F","M","M","F","M"],
          'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
              }
#df = data frame
df = pd.DataFrame(data)

# To Display the DataFrame
print(df)

# Accessing Specific Column
print(df['age'])
print(df['gender'])

# Basic Statistics
print(df['age'].min())
print(df['age'].max())
print(df['age'].mean())

# Filtering Data
print(df[df['age'] > 30])
