import os

folder_path = r"C:\Users\thoma\Desktop\test_folder"

for filename in os.listdir(folder_path):
    full_path = os.path.join(folder_path, filename) 
    if os.path.isfile(full_path) and not filename.startswith("renamed_"):
        new_filename = "renamed_" + filename
        new_full_path = os.path.join(folder_path, new_filename)
        os.rename(full_path, new_full_path)
        print(new_filename)