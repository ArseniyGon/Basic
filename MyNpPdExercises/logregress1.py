import numpy
from sklearn import linear_model
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, \
    roc_auc_score, roc_curve
import matplotlib.pyplot as plt


#Reshaped for Logistic function.
X = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1, 1)
# print(X)
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

logr = linear_model.LogisticRegression()
logr.fit(X, y)


#predict if tumor is cancerous where the size is 3.46mm:
predicted = logr.predict(X)
print(predicted)

# процент объектов которые были  классифицированны правильно
# (Точность классификации определяется соотношением)
accuracy = accuracy_score(y, predicted)
print(accuracy)

# доля правильно классифицированных объектов относительно всех объектов которые были предсказанны как положительные
# (из всех прогнозирующих положительных классов, сколько мы предсказали правильно. Точность должна быть высокой)
precision = precision_score(y, predicted)
print(precision)

# доля правильно классифицированных объектов положительного класса
# ( из всех положительных классов, сколько мы предсказали правильно. Отзыв должен быть высоким.)
recall = recall_score(y, predicted)
print(recall)

#  гармонический баланс между точностью и полнотой
#  (Сложно сравнивать две модели с разными Precision и Recall.
#  Поэтому, чтобы сделать их сопоставимыми, мы используем F-Score.
#  Это Гармоническое Средство Точности и Вспомнить. По сравнению с арифметическим средним,
#  гармоническое среднее наказывает более экстремальные значения. F-оценка должна быть высокой.)
f1 = f1_score(y, predicted)
print(f1)

print(classification_report(y, predicted))
y_pred_prob = logr.predict_proba(X)   # значение вероятности для каждого объекта (на сколько вероятен каждый объект)

aucroc = roc_auc_score(y, y_pred_prob[:, 1])
print(aucroc)
fpr, tpr, thresholds = roc_curve(y, y_pred_prob[:, 1])
plt.plot(fpr, tpr)
plt.plot([0, 1], [0, 1])
plt.show()


# print(y_pred_prob)

