import os
import glob
import streamlit as st
import pandas as pd


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


def display_file_with_url(folder_path: str, output_files: [], extension: str):
    for output_file in output_files:
        output_file_link = get_links(output_file, folder_path)

        if output_file_link:
            if extension == 'csv':
                with st.chat_message("AI"):
                    url = os.getcwd() + output_file_link + '.' + extension
                    df = pd.read_csv(url, sep=';', header=0)
                    st.dataframe(df)
            else:
                with st.chat_message("AI"):
                    url = os.getcwd() + output_file_link + '.' + extension
                    html_file = read_md_file(url)
                    st.markdown(html_file)
