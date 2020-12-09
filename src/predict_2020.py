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
from sklearn.tree import export_graphviz

sc = StandardScaler()

# All rounds, manually updated one at a time
CSV_round1 = "all_data_combined_r1.csv"
CSV_round2 = "all_data_combined_r2.csv"
CSV_round3 = "all_data_combined_r3.csv"
CSV_round4 = "all_data_combined_r4.csv"
CSV_round5 = "all_data_combined_r5.csv"
CSV_round6 = "all_data_combined_r6.csv"

# Load classifier
classifier = None
with open("top_classifier.pck", 'rb') as p:
    classifier = pck.load(p)

# Load round data from CSV
mm_features = pd.read_csv(CSV_round6)
mm_features = mm_features.drop("WINNINGTEAM",axis=1)
mm_features = mm_features.drop("TEAM1SCORE",axis=1)
mm_features = mm_features.drop("TEAM2SCORE",axis=1)
mm_features = mm_features.drop("TEAM1",axis=1)
mm_features = mm_features.drop("TEAM2",axis=1)
mm_features = mm_features.drop("YEAR",axis=1)
columns = list(mm_features.columns)

# Predict using the classifier
mm_features = pd.get_dummies(mm_features)
mm_x = sc.fit_transform(mm_features)
mm_y_pred = classifier.predict(mm_x)
for i in range(0,len(mm_y_pred) - 1, 2):
    print(mm_y_pred[i], mm_y_pred[i+1])

# Create png file of a decision tree in the RF
# estimator = classifier.estimators_[0]
# export_graphviz(estimator, 
#                 out_file='tree.dot', 
#                 feature_names = columns,
#                 class_names = ["0","1"],
#                 rounded = True, proportion = False, 
#                 precision = 2, filled = True)
# call(['dot', '-Tpng', 'tree.dot', '-o', 'tree.png', '-Gdpi=600'])