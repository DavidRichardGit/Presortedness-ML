import os
#os.environ['KAGGLE_USERNAME'] = '...'
#os.environ['KAGGLE_KEY'] = '...'
import kaggle
import pandas as pd
os.getcwd()
dataset_directory = './kaggledatasets'

# creating a df that contains datasets
datasets_list_csv = []

for page_num in range(400, 420):
    datasets_page = kaggle.api.datasets_list(page=page_num, max_size=100000, filetype='csv')
    datasets_list_csv.extend(datasets_page)

datasets_list_df = pd.DataFrame(datasets_list_csv)
public_datasets = datasets_list_df[datasets_list_df['isPrivate'] == False]


print(public_datasets)

# downloading the datasets into path = './datasets'
for index, row in public_datasets.iterrows():
    owner_slug = row['ownerNameNullable'].replace(" ", "-").lower()
    dataset_slug = row['titleNullable'].replace(" ", "-").lower()
    dataset_name = f"{owner_slug}/{dataset_slug}"
    print(f"Downloading dataset: {dataset_name}")
    try:
        kaggle.api.dataset_download_files(dataset_name, path=dataset_directory, unzip=True)
    except Exception as e:
        print(f"Error downloading dataset {dataset_name}: {e}")
