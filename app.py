import streamlit as st
from crew.main import write_post
from manage_files import display_file_with_url
import pandas as pd
import os

# suffix = ['*_websearch.csv', '*_titles.csv', '*_english.md', '*_spanish.md']

csv_files = ['*_titles.csv', '*_websearch.csv']
md_files = ['*_english.md', '*_spanish.md']
folder_path = './outputs'

st.set_page_config("Blog Post Automation")
st.title("Blog Post Automation")

topic = st.chat_input("My topic")

st.info("Write the topic and hit run.")

if topic is not None:

    with st.spinner("Processing..."):
        # write_post(topic)

        with st.chat_message("user"):
            st.write(topic)

        display_file_with_url(folder_path, csv_files, 'csv')
        display_file_with_url(folder_path, md_files, 'md')
