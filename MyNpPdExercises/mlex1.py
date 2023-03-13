import pandas as pd
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

data = {'Name': ['John', 'Maggie', 'Mike', 'Sarah', 'David', 'Tom'],
        'Age': [32, 28, 45, 33, 27, 35],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Male'],
        'Salary': [45000, 52000, 60000, 65000, 38000, 70000]}

df = pd.DataFrame(data)
print(df)
X = df[['Age', 'Salary']]
y = df['Gender']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a decision tree classifier
clf = DecisionTreeClassifier()

# Create a bagging classifier using the decision tree classifier as the base estimator
bag_clf = BaggingClassifier(estimator=clf, n_estimators=10, random_state=42)

# Fit the bagging classifier on the training data
bag_clf.fit(X_train, y_train)

# Evaluate the accuracy of the bagging classifier on the test data
accuracy = bag_clf.score(X_test, y_test)
print('Accuracy:', accuracy)


# Calculate the mean salary of the entire dataset
mean_salary = np.mean(df['Salary'])
print('Mean Salary:', mean_salary)

# Perform bootstrapping by resampling the dataset with replacement and calculating the mean salary
n_bootstraps = 1000
bootstrapped_means = []

for i in range(n_bootstraps):
    bootstrap_sample = np.random.choice(df['Salary'], size=len(df), replace=True)
    boot