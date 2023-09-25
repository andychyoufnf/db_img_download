import os

def rename_files_in_folder(folder_path):
    try:
        for filename in os.listdir(folder_path):
            index = int(filename.split('_')[0])
            new_name = f"{index+1}_{filename.split('_')[1]}_1.png"
            old_path = os.path.join(folder_path, filename)
            new_path = os.path.join('./new_media/', new_name)
            
            if os.path.isfile(old_path):
                os.rename(old_path, new_path)
                print(f"File '{filename}' renamed to '{new_name}'")
    except OSError as e:
        print(f"Error renaming files: {e}")

# Example usage
folder_to_rename = "./media/"

rename_files_in_folder(folder_to_rename)