import os
import pandas as pd
import numpy as np

os.getcwd()

dataset_directory = './kaggledatasets'
dataset_dfs = {}

# import files in the directory
for file_name in os.listdir(dataset_directory):
    try:
        dataset_name = os.path.splitext(file_name)[0]
        dataset_dfs[dataset_name] = pd.read_csv(os.path.join(dataset_directory, file_name))
    except pd.errors.ParserError as e:
        print(f"Error reading file '{file_name}': {e}")
        continue

print("amount of dataframes imported:")
print(len(dataset_dfs))

for key, df in dataset_dfs.items():
    for column in df.columns:
        if not df[column].apply(lambda x: isinstance(x, (int, float))).all():
            df.drop(column, axis=1, inplace=True)
            
    dataset_dfs[key] = df.dropna().head(30)
