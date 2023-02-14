import pandas as pd
import numpy as np

<<<<<<< HEAD
project_data = pd.read_excel('Project_File.xlsx')
print(project_data)
project = pd.DataFrame(project_data)
print(project)

Column = ["Saudi Arabia","Kuwait","UAE","United Kingdom","Germany","France","Italy","Netherlands","Greece","Belgium & Luxembourg","Switzerland","Austria","Scandinavia","CIS & Eastern Europe","USA","Canada","Australia","New Zealand","Africa"]
project.drop(["Africa "],inplace=True,axis=1)
=======
missing_values = ["na"]
project_df = pd.read_csv('Project_File.csv', na_values=missing_values)
print(project_df)
project_df.replace('na', np.NaN)

print(project_df.isnull())
>>>>>>> b6f4a8da3b08674feffd15919d5981971ccc0b03
