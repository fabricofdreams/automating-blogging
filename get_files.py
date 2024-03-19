import os
import glob


def get_links(suffix_file, folder_path):
    # Create a list of all files in the folder ending with the suffix passed
    files_with_suffix = glob.glob(os.path.join(folder_path, suffix_file))

    # Check if there are any files in the folder
    if not files_with_suffix:
        print("No files found in the folder.")
        return ""
    else:
        # Sort the list of files by modification time and get the last one
        latest_file = max(files_with_suffix, key=os.path.getmtime)
        url = latest_file.split('.')[1]
        return url


def read_md_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        md_content = file.read()
        if md_content:
            return md_content
        else:
            return ""
