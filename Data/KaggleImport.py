import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

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
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError reading file '{file_name}': {e}")
        continue
    except pd.errors.EmptyDataError as e:
        print(f"EmptyDataError reading file '{file_name}': {e}")
        continue
    except IsADirectoryError as e:
        print(f"Error reading file '{file_name}': {e}")
        continue

print("amount of dataframes imported:")
print(len(dataset_dfs))

ARRAY_SIZE = 200

for key, df in dataset_dfs.items():
    for column in df.columns:
        if not df[column].apply(lambda x: isinstance(x, (int, float))).all() or len(df[column].values) < ARRAY_SIZE:
            df.drop(column, axis=1, inplace=True)
            
    dataset_dfs[key] = df.dropna().head(ARRAY_SIZE)

import pickle

# Save the dictionary to a file
with open('dataset_dfs.pkl', 'wb') as f:
    pickle.dump(dataset_dfs, f)
