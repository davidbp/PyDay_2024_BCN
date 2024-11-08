import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
#from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier

X = pd.read_csv("data/x.csv", index_col=[0])
y = pd.read_csv("data/y.csv", index_col=[0])

(X_train, X_test, y_train, y_test) = train_test_split(
    X,
    y, 
    test_size=0.3, 
    random_state=1,
    train_size=100,
)

params = {
    "criterion": "entropy", 
    "min_samples_split": 4,
    "min_impurity_decrease": 0.02
}

decission_tree_model = DecisionTreeClassifier(**params)
decission_tree_model = decission_tree_model.fit(X_train, y_train)
prediction = decission_tree_model.predict(X_test)

print(decission_tree_model.score(X_test, y_test))

# Define parameters
params = {
    "n_estimators": 10,
    "criterion": "gini",
    "max_depth": None,
    "min_samples_split": 2,
    "min_samples_leaf": 1,
}

# Instantiate the RandomForestClassifier model with parameters
random_forest_model = RandomForestClassifier(**params)

# Train the model
random_forest_model.fit(X_train, y_train)

# Predict
predictions = random_forest_model.predict(X_test)

# Evaluate your model
score_train = random_forest_model.score(X_train, y_train.values.ravel())   # .values will give the values in a numpy array (shape: (n,1))
                                                                           # .ravel will convert that array shape to (n, ) (i.e. flatten it)
print(score_train)