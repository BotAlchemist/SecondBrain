# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:07:22 2022

@author: Sumit
"""

import streamlit as st
import pandas as pd

def add_book():
    df_book_meta= pd.read_csv('files/book_metadata.csv')
    
    with st.form("Add book details"):
        i_book_name= st.text_input("Book Name").upper()
        i_book_author= st.text_input("Author").upper()
        i_book_category= st.selectbox("Category", ['Sprituality', 'Finance', 'Motovation/Inspiration', 'Others'])

        book_submit = st.form_submit_button("Add book")
        
        if book_submit:
            if len(i_book_name) != 0:
                add_book_row= [i_book_name, i_book_author, i_book_category]
                df_add_book= pd.DataFrame([add_book_row], columns= ['Name', 'Author', 'Category'])
                st.write(df_book_meta)
                
                df_book_meta= df_book_meta.append(df_add_book)
                df_book_meta= df_book_meta.drop_duplicates()
                df_book_meta.to_csv('files/book_metadata.csv', index=False)
                st.success("Book added")
            else:
                st.warning("Add book name!")
    
def add_summary():
    df_book_meta= pd.read_csv('files/book_metadata.csv')
    df_book_summary= pd.read_csv('files/book_summary.csv')
    with st.form("Add summary", clear_on_submit=True):
        i_book_name= st.selectbox("Select Book Name", df_book_meta['Name'].unique()  )
        i_book_header= st.text_input("Header/Chapter").upper()
        i_book_summary= st.text_area("Summary", height= 200)
        
        summary_submit = st.form_submit_button("Add summary")
        
        if summary_submit:
            if len(i_book_summary)!=0:
                add_summary_row= [i_book_name,i_book_header, i_book_summary ]  
                df_add_summary= pd.DataFrame([add_summary_row], columns= ['Name','Header', 'Summary'])
                df_book_summary= df_book_summary.append(df_add_summary)
                df_book_summary= df_book_summary.drop_duplicates()
                df_book_summary.to_csv('files/book_summary.csv', index=False)
                st.success("Summary added")
                i_book_summary= ""
            else:
                st.warning("Add summary!")
                
                
def get_summary():
    df_book_summary= pd.read_csv('files/book_summary.csv')
    
    df_book_summary= df_book_summary.fillna("Unknown")
    i_book_name= st.selectbox("Select Book Name", df_book_summary['Name'].unique()  )
    df_one_book= df_book_summary[df_book_summary['Name']==i_book_name]
    i_book_header= st.selectbox('Chapter/Header', df_one_book['Header'].unique())
    df_one_book= df_one_book[df_one_book['Header']== i_book_header]
    
    
    #st.write(df_one_book)
    st.subheader(i_book_header)
    for index, row in df_one_book.iterrows():
        st.text_area("", row['Summary'])
    
    # with st.container():
    #     st.caption("This is inside the container 1")
    #     st.caption("This is inside the container 2")

                
            
            
            
            
            
            
            
            
            
            
            
            
        