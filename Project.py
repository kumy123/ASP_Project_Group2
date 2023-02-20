import pandas as pd
import numpy as np


project_data = pd.read_excel('Project_File.xlsx')
print(project_data)
project = pd.DataFrame(project_data)
project.to_numpy()
print(project)

Column = ["Saudi Arabia","Kuwait","UAE","United Kingdom","Germany","France","Italy","Netherlands","Greece","Belgium & Luxembourg","Switzerland","Austria","Scandinavia","CIS & Eastern Europe","USA","Canada","Australia","New Zealand","Africa"]
project.drop(["Africa "],inplace=True,axis=0)
project = project.drop(project.loc[:,' Saudi Arabia ':' Africa '].columns, axis=1)
print(project)


print(project)
print(project.columns)


project.replace('na', 0)

print(project.isnull().sum())

print(project)

project = project.replace(' na ', np.nan)

project = project.rename(columns={'   ':'Date'})


project = project.dropna()

