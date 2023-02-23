import pandas as pd
import numpy as np



#region = asia
#era = 2008-2017


#load data from excel
project_data = pd.read_excel('Project_File.xlsx')
print(project_data)
project = pd.DataFrame(project_data)
print(project)


#filter out by region selected
project = project.drop(project.loc[:,' United Kingdom ':' Africa '].columns, axis=1)
print(project)


#rename col to date
project = project.rename(columns={'   ':'Date'})

#removing whitespace for filtering year
project['Date'] = project['Date'].astype(str)
project['Date'] = project['Date'].str.strip()
project['Date'] = project['Date'].str.split(' ',2).str[0]
project['Date'] = project['Date'].astype(int)

#filter df by years
project = project.loc[(project['Date'] > 2007)]
project = project.reset_index(drop=True)
print(project)

#Q6
asia = [' Brunei Darussalam ', ' Indonesia ', ' Malaysia ',
       ' Philippines ', ' Thailand ', ' Viet Nam ', ' Myanmar ', ' Japan ',
       ' Hong Kong ', ' China ', ' Taiwan ', ' Korea, Republic Of ', ' India ',
       ' Pakistan ', ' Sri Lanka ', ' Saudi Arabia ', ' Kuwait ', ' UAE ']
sum_col= project[asia].sum(axis=0)
print(sum_col)
sum_dict = sum_col.to_dict()
print(sum_dict)
#sum_col= pd.DataFrame(project[asia].sum(axis=0), columns=['total']).reset_index()
#sum_col = sum_col.rename(columns={'index':'Countries'})
countries = list(sum_dict.keys())
total = list(sum_dict.values())
import matplotlib.pyplot as plt
plt.figure(facecolor='white',figsize=(10,10))
plt.bar(x = countries, height = total, color = 'orange' )
plt.ticklabel_format(axis='y',style='plain')
plt.xticks(rotation = 45)
plt.xlabel('Countries')
plt.ylabel('total no. of visitors')
plt.show()


#Q7
sorted_col = sum_col.sort_values(ascending=False)
print(sorted_col)
top3_val = sorted_col.head(3)
print(top3_val)


#sorted_value =
#top3_region
#sort value and then sort it by top 3 values of countries in the region selected


#Q8
#do the unittest, make sure to import unittest
import unittest

class TestMyProgram(unittest.TestCase):

       def __int__(self):
              self.file = file


       def test_load_data(self):
              load_data = pd.read_excel(self.file)
              return load_data


if __name__ == '__main__':
       unittest.main()




#09 presentation(fuck that)