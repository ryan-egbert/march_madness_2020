import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier, VotingClassifier, AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.utils import shuffle
from subprocess import call
import pickle as pck

# Name of completed data
CSV = "all_data_combined.csv"

# Read CSV into dataframe and drop necessary columns
features = pd.read_csv(CSV)
results = np.array(features['WINNINGTEAM'])
features = features.drop('WINNINGTEAM', axis=1)
features = features.drop('YEAR', axis=1)
# features = features.drop('ROUND', axis=1)
features = features.drop('TEAM1', axis=1)
features = features.drop('TEAM2', axis=1)
features = features.drop('TEAM1SCORE', axis=1)
features = features.drop('TEAM2SCORE', axis=1)
features = pd.get_dummies(features)
columns = list(features.columns)
features = np.array(features)

# Used for determining best hyperparameters
# maxAcc = 0
# bestTs = 0
# bestParams = ()
# bestClassifier = None
# ts = 0.05

# Randomly split into train and test batches
x_train, x_test, y_train, y_test = train_test_split(features, results, test_size=0.05, random_state=75)

print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

# Scale
sc = StandardScaler()

x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Train the classifier
classifier = RandomForestClassifier(n_estimators=500, random_state=75)
classifier.fit(x_train, y_train)
y_pred = classifier.predict(x_test)
print(y_pred)
print(f"============== Classifier ==============")
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred))
score = accuracy_score(y_test, y_pred)
print(f"Accuracy: {score}")
print("=========================================")

# Dump classifier into pickle file
with open("top_classifier_vc.pck", 'wb') as p:
    pck.dump(classifier, p)

# List importances of features
importances = list(classifier.feature_importances_)
feature_importances = [(feature, round(importance, 2)) for feature, importance in zip(columns, importances)]
feature_importances = sorted(feature_importances, key = lambda x: x[1], reverse = True)
[print('Variable: {:20} Importance: {}'.format(*pair)) for pair in feature_importances];


'''
This was my attempt to use a voting classifier with several
different types of classifiers.  I was never able to exceed
the accuracy that I produces with a single random forest, 
however.
'''
# rf = RandomForestClassifier(n_estimators=500, random_state=75)
# rf.fit(x_train, y_train)
# y_pred = rf.predict(x_test)

# print(f"============== RF Classifier ==============")
# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))
# print(accuracy_score(y_test, y_pred))
# print("============================================")

# ab = AdaBoostClassifier(n_estimators=500, random_state=75)
# ab.fit(x_train, y_train)
# y_pred = ab.predict(x_test)

# print(f"============== AdaBoost Classifier ==============")
# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))
# print(accuracy_score(y_test, y_pred))
# print("============================================")

# dt = RandomForestClassifier(n_estimators=500, random_state=75)
# dt.fit(x_train, y_train)
# y_pred = dt.predict(x_test)

# print(f"============== DT Classifier ==============")
# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))
# print(accuracy_score(y_test, y_pred))
# print("============================================")

# vc = VotingClassifier(estimators=[
#     ('rf', rf),
#     ('ada', ab),
#     ('dt', dt)
# ], voting="soft")

# # vc = VotingClassifier(estimators=[
# #     (str(i), c) for c, i in all_classifiers
# # ], voting="soft")

# vc.fit(x_train, y_train)
# y_pred = vc.predict(x_test)

# print("\n\n=====================\n\nAll Classifiers, Voting\n\n===================")
# print(confusion_matrix(y_test, y_pred))
# print(classification_report(y_test, y_pred))
# print(accuracy_score(y_test, y_pred))

# with open("top_classifier_vc.pck", 'wb') as v:
#     pck.dump(vc, v)

