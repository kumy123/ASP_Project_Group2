import pandas as pd
import numpy as np

missing_values = ["na"]
project_df = pd.read_csv('Project_File.csv', na_values=missing_values)
print(project_df)
project_df.replace('na', np.NaN)

print(project_df.isnull())
