import os
import zipfile
import shutil

def traverse_directories(directory):
    # Walk through each directory in the given directory
    num = 0;
    for dirfile in os.listdir(directory):
        # Print the current directory's path
        # print(f"now folders: {root}")
        # Optionally, print subdirectories and files
        # print("Subdirectories:", dirs)
        # print("Files:", files)
        now_path = os.path.join(directory,dirfile)
        if now_path.endswith('.zip'):
            with zipfile.ZipFile(now_path, 'r') as zip_ref:
                zip_ref.extractall(directory)
                print(f"{now_path} extracted successfully")
# Call the function with the current working directory
traverse_directories(os.getcwd())
