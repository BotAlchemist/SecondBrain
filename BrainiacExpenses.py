# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 16:49:56 2022

@author: Sumit
"""

import streamlit as st
import pandas as pd
from datetime import date

def add_expenses():
    df_expense= pd.read_csv('files/expenses.csv')    
    today = date.today()
    i_category_list=[ 'Car' ,'Food' ,'Shopping' ,'Bill' ,'Enternainment', 'Travel' ,'Pet' ,'Gift' ,'Unknown','Others' ]
    i_sub_category_list= ['Maintenance', 'Gift' ,'Swiggy','Zomato', 'Amazon','Electricity' ,'Mobile', 'D2H' ,'Credit Card','Uni card', 'OTT' ,
                          'Dunzo', 'Big Basket' ,'Movies' ,'Country Delight', 'Car loan', 'Medical', 'Ola', 'Uber' ,'Rent' , 'Stall' ,'Driver',
                          'Fasttag', 'Wifi' ,'Pet food', 'Petrol', 'Others' 'Unknown']
    
    with st.form("expenses_form"):
        i_date= st.text_input("Date", today)
        i_amount= st.number_input("Amount")
        i_type= st.selectbox("Type", ['Mandatory', 'Optional'])
        i_category= st.selectbox("Category", i_category_list)
        i_subcategory= st.selectbox("Sub-Category", i_sub_category_list)
        i_comment= st.text_input("Comments")
        
        new_expense= {
                    "Date": i_date,
                    "Amount": i_amount,
                    "Type": i_type,
                    "Category": i_category,
                    "Sub-Category": i_subcategory,
                    "Comments": i_comment
            }
        
        
        
        expense_submit = st.form_submit_button("Save")
        
    if expense_submit:
        df_expense=df_expense.append(new_expense, ignore_index=True)
        df_expense.to_csv('files/expenses.csv', index=False)
        
    st.write(df_expense.tail(5))


def display_graph(today):
    st.write(today)