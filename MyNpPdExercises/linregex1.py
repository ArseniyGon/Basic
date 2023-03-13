import pandas as pd
from scipy. stats import ttest_ind

#create pandas DataFrame
df = pd.DataFrame({'method': ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A',
 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B'],
 'score': [71, 72, 72, 75, 78, 81, 82, 83, 89, 91, 91, 92, 92, 95, 98, 81, 82, 83, 89, 91]})

#view first five rows of DataFrame
print(df.head(20))

#define samples
group1 = df[df['method']=='A']
group2 = df[df['method']=='B']

#perform independent two sample t-test
print(ttest_ind(group1['score'], group2['score']))
