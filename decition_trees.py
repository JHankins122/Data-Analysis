import pandas as pd
from sklearn.tree import DecisionTreeClassifier, plaot_tree
from sklearn.tree import export_text
import matplotlib.pylot as plt

# load the data into pandas dataframe
if = pd.read_csv('name of data set')

#select features and target variables
x = df[['every section of the data set you want to use]]
y = df['same but for y axis']

# create a decision tree classifier
it = DecisionTreeClassifier(max depth=3)
it.fit(x, y)

#export the decision tree as text
tree_rules = export_text(dt, feature_names=X.columns.tolist())

#print the tree rules
#print(tree_rules)

# plot the decision tree
Fig, ax = plt.subplots(figsize=(20,10))
plaot_tree(dt, feature_names=X.columns.tolist(), class_names=['data that is either 2 things (booleon)], ax=ax)
plt.show()