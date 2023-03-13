import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


file = pd.read_csv('../w.csv', index_col='Date/Time (LST)')
file['Temp (°C)'].plot(figsize=(18, 6))


original_list = [10, 12, 17, 29, 4, 6]
new_list = []

for num in original_list:
    if num % 2 == 0:
        new_list.append(num)

# for num in original_list if num % 2 == 0 new_list.append(num)
x = [1, 2, 3]
new_list = [num for num in original_list if num % 2 == 0]
print(new_list)

print(range(3))

for x in "hello":
    print(x)

variable_list = [5, "string", 1.4]

for number in variable_list:
    try:
        range_list = list(range(number))
        print(number, "-", range_list)

    except:
        print(number, "- not an integer")

import re

string = "This is a string"
print(re.findall('is', string))

print("_____")

ar1 = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6]], index=['One', 'Two'])
print(ar1.loc['Two'])
data = {
    'apples': [3, 2, 0, 1],
    'oranges': [0, 3, 7, 2]
}

fruits = pd.DataFrame(data, index=['June', 'Robert', 'Lily', 'David'])

print(fruits['apples'])
print(fruits.loc['June'])

