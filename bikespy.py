import pandas as pd
import matplotlib.pyplot as plt

plt.style.use('ggplot')  # Красивые графики
plt.rcParams['figure.figsize'] = (15, 5)  # Размер картинок

fixed_df = pd.read_csv('MyNpPdExercises/nba.csv')
df = pd.DataFrame(fixed_df)

# print(df['Age'])
# df = pd.read_csv('bikes1.csv',
#                  sep=';',
#                  skiprows = [0, 306])
#
# # Print the Dataframe
# print(df)
# df['Age'].plot()
# plt.show()
df['Age'].value_counts().plot(kind='bar')
plt.show()

# # initializing the data
# plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
# plt.axis([0, 6, 0, 20])
# plt.show()