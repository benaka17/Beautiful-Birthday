import os

def list_files_in_folder(folder_path):
    # List all files in the given folder
    filenames = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            filenames.append(file)
    return filenames

# Example usage
folder_path = r'C:\Users\alexa\Desktop\All_Flowers\iCloud Fotos'
files = list_files_in_folder(folder_path)
print(files)
