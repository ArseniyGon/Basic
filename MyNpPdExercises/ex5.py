import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import seaborn as sns
from scipy.stats import mannwhitneyu

# Create a sample DataFrame
# data = {'Name': ['Alex', 'Bob', 'Charlie', 'David', 'Eve'],
#         'Age': [25, 32, 45, 27, 35],
#         'City': ['New York', 'San Francisco', 'Los Angeles', 'New York', 'San Francisco']}
# df = pd.DataFrame(data)

# Group the DataFrame by the 'City' column
# grouped_df = df.groupby('City')['Age'].sum()

# Print the groups
# print(grouped_df.groups)
# for x, y in grouped_df:
#     print(x)
#     print(y)
# print(grouped_df)

# Print the mean of each group
# print(grouped_df.mean())
# fig, axes = plt.subplots(nrows=2, ncols=2)
# df.groupby('City').count().plot(ax=axes[0,0]).pie(y='Age', autopct='%1.0f%%', subplots=True)
# df.groupby('Age').count().plot(ax=axes[0,1]).pie(y='Name', autopct='%1.0f%%', subplots=True)
# plt.show()
#
# N = 5
# menMeans = (20, 35, 30, 35, -27)
# womenMeans = (25, 32, 34, 20, -25)
# menStd = (2, 3, 4, 1, 2)
# womenStd = (3, 5, 2, 3, 3)
# ind = np.arange(N)    # the x locations for the groups
# width = 0.35       # the width of the bars: can also be len(x) sequence
# # Stacked bar plot with error bars
#
# fig, ax = plt.subplots()
#
# p1 = ax.bar(ind, menMeans, width, yerr=menStd, label='Men')
# p2 = ax.bar(ind, womenMeans, width,
#             bottom=menMeans, yerr=womenStd, label='Women')
#
# ax.axhline(0, color='grey', linewidth=0.8)
# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.set_xticks(ind, labels=['G1', 'G2', 'G3', 'G4', 'G5'])
# ax.legend()
#
# # Label with label_type 'center' instead of the default 'edge'
# ax.bar_label(p1, label_type='center')
# ax.bar_label(p2, label_type='center')
# ax.bar_label(p2)
#
# plt.show()

df = pd.DataFrame({'Name': ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5', 'Cat6', 'Cat7', 'Cat8', 'Cat9'],
                   'Color': ['Red', 'Black', 'Grey', 'Red', 'Black', 'Grey', 'Red', 'Black', 'Grey'],
                   'Size': ['Large', 'Medium', 'Medium', 'Large', 'Large', 'Small', 'Large', 'Medium', 'Small']})

# print(df.groupby('Size').count())
x = df.groupby('Size').count()
# print(x)

# df.groupby('Size')['Color'].count().plot.bar(color=df['Color'])
# x.plot(kind='scatter', x='Color', y='Size')
# plt.show()



# Create a random dataset
# np.random.seed(0)
# data = np.random.normal(size=(20, 3))
#
# # Create a DataFrame from the data
# df = pd.DataFrame(data, columns=["X1", "X2", "X3"])
#
# # Use Seaborn to create a scatter plot matrix
# sns.pairplot(df)
# plt.show()
# # Use SciPy to perform a statistical test on the data
# results = stats.ttest_ind(df["X1"], df["X2"])

# Create some example data
# data = {'treatment': ['A', 'A', 'B', 'B'],
#         'response': [10, 8, 12, 14]}
# df = pd.DataFrame(data)
#
# # Perform the Mann-Whitney U test
# u, p_value = mannwhitneyu(df[df['treatment'] == 'A']['response'],
#                            df[df['treatment'] == 'B']['response'])
# print('U-statistic:', u)
# print('p-value:', p_value)

