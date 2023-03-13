import numpy as np
from sklearn import linear_model
import seaborn as sns
from sklearn.metrics import accuracy_score, confusion_matrix, roc_auc_score, roc_curve, precision_score, recall_score, \
    f1_score
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

X = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])
y_true = y
logr = linear_model.LogisticRegression()
logr.fit(X, y)

# predict if tumor is cancerous where the size is 3.46mm:
predicted = logr.predict(np.array([3.46]).reshape(-1, 1))

print(predicted)

y_pred = logr.predict_proba(X)[:, 1]
print(y_pred)

y_predict = logr.predict(X)
AUC_ROC = roc_auc_score(y, y_pred)
print(AUC_ROC)

xs = np.linspace(0, 6, 100)
pred_prob = logr.predict_proba(xs[:, None])
plt.scatter(X, y, c=y_predict)
plt.plot(xs, pred_prob[:, 1], label="sklearn probability", c="#006156", zorder=-1)
plt.show()
# fpr, tpr, treshold = roc_curve(y, y_pred)
# roc_auc = auc(fpr, tpr)
# plt.plot(fpr, tpr, color='darkorange')
# plt.show()

accuracy = accuracy_score(y, y_predict)
print(accuracy)
cm = confusion_matrix(y, y_predict)
print(cm)
# precision = precision_score(y, y_pred)
# recall = recall_score(y, y_pred)
# f1_score = f1_score(y, y_pred)