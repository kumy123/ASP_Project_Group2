import pandas as pd
import numpy as np



#region = asia
#era = 2008-2017


#load data from excel
project_data = pd.read_excel('Project_File.xlsx')
print(project_data)
project = pd.DataFrame(project_data)
print(project)
print(project.columns)


#filter out by region selected
project = project.drop(project.loc[:,' United Kingdom ':' Africa '].columns, axis=1)
print(project)



print(project)

print(project)
print(project.columns)


print(project.isnull().sum())

print(project)
#remove Na values from dataframe itself
project = project.replace(' na ', np.nan)
project = project.rename(columns={'   ':'Date'})
project = project.dropna()
print(project)



project.info()
#filter the dataframe by era
project['Date'] = project['Date'].astype(str)
print(type(project['Date']))
print(project)
project['Date'] = project['Date'].str.strip()
project.info()
print(project.columns)

project['Date'] = pd.to_datetime(project['Date'], errors='coerce')
print(project['Date'])
print(project)
#project['Date'] = project.loc[project['Date'].dt.year < 2007-12-01]


#10 presentation(fuck that)