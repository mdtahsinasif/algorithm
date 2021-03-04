import os
import pandas as pd
import seaborn as sns

path = 'C:\\Users\\Algorithmica\\Downloads'
titanic_train = pd.read_csv(os.path.join(path, 'titanic_train.csv'))
print(titanic_train.shape)
print(titanic_train.info())

#explore bivariate relationships: categorical vs categorical 
sns.factorplot(x="Sex", hue="Survived", data=titanic_train, kind="count", size=6)
sns.factorplot(x="Pclass", hue="Survived", data=titanic_train, kind="count", size=6)
sns.factorplot(x="Embarked", hue="Survived", data=titanic_train, kind="count", size=6)

#explore bivariate relationships: continuous  vs categorical
sns.FacetGrid(titanic_train, hue="Survived",size=8).map(sns.kdeplot, "Fare").add_legend()
sns.FacetGrid(titanic_train, row="Survived",size=8).map(sns.distplot, "Fare").add_legend()
sns.FacetGrid(titanic_train, hue="Survived",size=8).map(sns.boxplot, "Age").add_legend()

#explore bivariate relationships: continuous vs continuous 
sns.jointplot(x="Age", y="Fare", data=titanic_train)
