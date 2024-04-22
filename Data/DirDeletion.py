import shutil

# directory path to delete
directory_path = 'kaggledatasets/Dataset'

# Check if the directory exists
if os.path.exists(directory_path):
    shutil.rmtree(directory_path)
    print("Directory deleted successfully.")
else:
    print("Directory does not exist.")
