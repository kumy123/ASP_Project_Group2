import pandas as pd
import numpy as np

project = pd.read_excel('Project_File.xlsx')
print(project_data)
project = pd.DataFrame(project_data)
print(project)

Column = ["Saudi Arabia","Kuwait","UAE","United Kingdom","Germany","France","Italy","Netherlands","Greece","Belgium & Luxembourg","Switzerland","Austria","Scandinavia","CIS & Eastern Europe","USA","Canada","Australia","New Zealand","Africa"]
project.drop(["Africa "],inplace=True,axis=1)