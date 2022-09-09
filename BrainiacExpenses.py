# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 16:49:56 2022

@author: Sumit
"""

import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px


def add_income():
    df_expense= pd.read_csv('files/expenses.csv')    
    today = date.today()
    i_category_list= ['Salary', 'Cashback']
    i_sub_category_list= ['Salary', 'Cashback']
    
    with st.form("income_form"):
        i_date= st.date_input("Date", today)
        i_credit= st.number_input("Amount")
        i_category= st.selectbox("Category", i_category_list)
        i_subcategory= st.selectbox("Sub-Category", i_sub_category_list)
        i_comment= st.text_input("Comments")
        
        new_income= {
                    "Date": i_date,
                    "Credit": i_credit,
                    "Category": i_category,
                    "Sub-Category": i_subcategory,
                    "Comments": i_comment
            }
        income_submit = st.form_submit_button("Save")
        if income_submit:
            df_expense=df_expense.append(new_income, ignore_index=True)
            df_expense.to_csv('files/expenses.csv', index=False)
            st.success("Income added!")
        
        
        st.write(df_expense.tail(5))
        
        
    



def add_expenses():
    df_expense= pd.read_csv('files/expenses.csv')    
    today = date.today()
    i_category_list=[ 'Car' ,'Food' , 'Groceries' ,'Shopping' ,'Bill' ,'Enternainment', 'Travel' ,'Pet' ,'Gift' ,'Unknown','Others' ]
    i_sub_category_list= ['Maintenance', 'Gift' ,'Swiggy','Zomato', 'Amazon','Electricity' ,'Mobile', 'D2H' ,'Credit Card','Uni card', 'OTT' ,
                          'Dunzo', 'Big Basket' ,'Movies' ,'Country Delight', 'Car loan', 'Medical', 'Ola', 'Uber' ,'Rent' , 'Mart' , 'Stall' ,'Driver',
                          'Fasttag', 'Wifi' ,'Pet food','Vet', 'Petrol', 'Others' ,'Unknown']
    
    with st.form("expenses_form"):
        i_date= st.date_input("Date", today)
        i_amount= st.number_input("Amount")
        i_type= st.selectbox("Type", ['mandatory', 'optional', 'investment'])
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
        
        st.success("Expense added!")
        
    st.write(df_expense.tail(5))


def display_graph_expense():
    df_expense= pd.read_csv('files/expenses.csv', parse_dates=['Date'], dayfirst=True)    
    df_expense['Date'] = pd.to_datetime(df_expense['Date'])
    df_expense= df_expense.sort_values(by='Date')
    df_expense['MonthYear']= df_expense['Date'].apply(lambda x: x.strftime('%B-%Y')) 
        
    time_frame= st.multiselect("Select Period", df_expense['MonthYear'].unique(), default= df_expense['MonthYear'].unique()[-1])
    
    df_expense= df_expense[df_expense['MonthYear'].isin(time_frame)]
    
    
    expensetab1, expensetab2, expensetab3= st.tabs(['Expenses split', 'Comparative expenses over the period', 'Raw data'])
    
    with expensetab1:
        fig = px.pie(df_expense, values='Amount', names='Type')
        st.plotly_chart(fig)
        
        fig = px.pie(df_expense, values='Amount', names='Category')
        st.plotly_chart(fig)
        
        
        
    with expensetab3:
        df_expense= df_expense.sort_values(by='Date', ascending= False)
        st.write(df_expense)
        
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    