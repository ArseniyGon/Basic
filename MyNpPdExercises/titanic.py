import pandas as pd


INDEX_COL = 0
NAME_COL = "Name"
SEX_COL = "Sex"
PCLASS_COL = "PClass"
AGE_COL = "Age"
SURVIVED_COL = "Survived"

AGE_GROUP_COL = "AgeGroup"

HEAD_ROWS_TO_SHOW = 15

# df = pd.read_csv("test.csv", index_col=INDEX_COL)
train_df = pd.read_csv('train.csv')
test_df = pd.read_csv('test.csv')
combine = [train_df, test_df]
# print(combine)

print(train_df[['Pclass', 'Survived']].groupby(['Pclass']).mean())
# print(train_df[['Pclass', 'Survived']].groupby(['Pclass']).count())
print(train_df[['Sex', 'Survived']].groupby(['Sex']).mean())
print(train_df[['Sex', 'Pclass', 'Survived']].groupby(['Sex', 'Pclass']).mean())



# print(df[:HEAD_ROWS_TO_SHOW])
#
# print("----")
#
# print(df.dtypes)
# print("----")
# print(df.shape)
# print(df[SEX_COL][:HEAD_ROWS_TO_SHOW])
# print(df.loc[10:15])
# print(df[['Survived', 'Age']])
# print(df[SEX_COL].value_counts())
# print(df['Class'].value_counts())




