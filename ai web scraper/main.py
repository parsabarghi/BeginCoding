import streamlit as st
from scrape import (
    scrape_website, 
    split_dom_content, 
    clean_body_content, 
    extract_body_content)
# from parse import parse_with_ollama


st.title("Ai Web Scraper")
url = st.text_input("Enter your url:")

if st.button("scrape site"):
    st.write("scraping the website")
    result = scrape_website(url)

    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    

    st.session_state.dom_content = cleaned_content

    with st.expander("view dom content"):
        st.text_area("dom content", cleaned_content, height=300)

if "dom_content" in st.session_state:
    parse_description = st.text_area("what you want?")

    if st.button("parse content"):
        if parse_description:
            st.write("parsing the data")

            dom_chunk = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunk, parse_description)
            st.write(parsed_result)