import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#region = asia
#era = 2008-2017

class project_data:

       def __init__(self, file):
              self.file = file


       def load_data(self):
              load_xlsx = pd.read_excel(self.file)
              return load_xlsx

       def parsed_data(self):
              loaded_data = project_data.load_data(self)
              filtered_region = loaded_data.drop(loaded_data.loc[:,' United Kingdom ':' Africa '].columns, axis=1)
              filtered_region = filtered_region.rename(columns={'   ':'Date'})
              filtered_region['Date'] = filtered_region['Date'].str.strip().str.split(' ',2).str[0].astype(int)
              filtered_year = filtered_region.loc[(filtered_region['Date'] > 2007)]
              return filtered_year




x = project_data('Project_File.xlsx')
df = project_data.load_data(x)
print(df)

project = project_data.parsed_data(x)
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
countries = list(sum_dict.keys())
total = list(sum_dict.values())
import matplotlib.pyplot as plt
fig1, ax = plt.subplots(figsize=(12, 10))
bar_container = ax.bar(x = countries, height = total, color = 'orange' )
ax.bar_label(bar_container, labels=total, fmt='{:,.0f}')
plt.ticklabel_format(axis='y',style='plain')
plt.xticks(rotation = 90)
plt.xlabel('Countries')
plt.ylabel('total no. of visitors')
plt.show()


#Q7 Sort values and show the top 3 in a region
sorted_col = sum_col.sort_values(ascending=False)
print(sorted_col)
top3_val = sorted_col.head(3)
print('the top 3 countries in the region are')
print(top3_val)



#sorted_value =
#top3_region
#sort value and then sort it by top 3 values of countries in the region selected


#Q8
#do the unittest, make sure to import unittest





