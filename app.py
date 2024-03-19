import streamlit as st
from crew.main import write_post
from get_files import get_links, read_md_file
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
        write_post(topic)

        with st.chat_message("user"):
            st.write(topic)

        for csv_file in csv_files:
            csv_file_link = get_links(csv_file, folder_path)

            if csv_file_link:
                keyword = (lambda x: x.split('_')[1])(csv_file)

                with st.chat_message("AI"):
                    url = os.getcwd() + csv_file_link + '.csv'
                    df = pd.read_csv(url, sep=';', header=0)
                    st.dataframe(df)

        for md_file in md_files:
            md_file_link = get_links(md_file, folder_path)

            if md_file_link:
                keyword = (lambda x: x.split('_')[1])(md_file)

                with st.chat_message("AI"):
                    url = os.getcwd() + md_file_link + '.md'
                    html_file = read_md_file(url)
                    st.markdown(html_file)
