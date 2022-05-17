import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

csvs = glob.glob('states*.csv')

dfs = []
for csv in csvs:
	df = pd.read_csv(csv)
	dfs.append(df)
us_census = pd.concat(dfs)
print(us_census.columns)
print(us_census.dtypes)
print(us_census.head())
us_census.Income = us_census.Income.str.replace('[\$,]', '')
us_census.Income = pd.to_numeric(us_census.Income)
print(us_census.Income.head())
split_gend = us_census.GenderPop.str.split('_')
us_census['Men'] = split_gend.str.get(0)
us_census['Women'] = split_gend.str.get(1)
print(us_census.head())
us_census['Men'] = us_census['Men'].str[:-1]
us_census['Women'] = us_census['Women'].str[:-1]
print(us_census.head())
us_census['Men'] = pd.to_numeric(us_census.Men)
us_census['Women'] = pd.to_numeric(us_census.Women)
print(us_census.Women)
us_census = us_census.fillna(value = {"Women": us_census.TotalPop - us_census.Men})
print(us_census.Women)
print(us_census)
us_census = us_census[['State', 'TotalPop', 'Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific', 'Income', 'Men', 'Women']]
us_census = us_census.drop_duplicates()
print(us_census)
us_census = us_census.reset_index(drop = True)
print(us_census)
plt.scatter(us_census.Women, us_census.Income)
plt.show()
plt.clf()
def percentage_to_numeric(df, column):
	df[column] = df[column].str[:-1]
	df[column] = pd.to_numeric(df[column])
percentage_to_numeric(us_census, "Hispanic")
percentage_to_numeric(us_census, "White")
percentage_to_numeric(us_census, "Black")
percentage_to_numeric(us_census, "Native")
percentage_to_numeric(us_census, "Asian")
percentage_to_numeric(us_census, "Pacific")
us_census['Pacific'] = us_census['Pacific'].fillna(100 - us_census['Hispanic'] - us_census['White'] - us_census['Black'] - us_census['Native'] - us_census['Asian'])
print(us_census)
print(us_census.dtypes)
for column in ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']:
	plt.hist(us_census[column])
	plt.xlabel("Percentage")
	plt.ylabel("Frequency")
	plt.title("Percentage of {}s".format(column))
	plt.show()
	plt.clf()
