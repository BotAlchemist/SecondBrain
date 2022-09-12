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
    i_category_list=[ 'Car' ,'Food' , 'Groceries' ,'Shopping' ,'Bill' ,'Enternainment','Health/Fitness' ,'Travel' ,'Pet' ,'Gift' ,'Unknown','Others' ]
    
    i_sub_category_list= ['Maintenance', 'Gift' ,'Swiggy','Zomato', 'Amazon','Electricity' ,'Mobile', 'D2H' ,'Credit Card','Uni card', 'OTT' ,
                          'Dunzo', 'Big Basket' , 'Health/Fitness' , 'Movies' ,'Country Delight', 'Car loan', 'Medical', 'Ola', 'Uber' ,'Rent' , 'Mart' , 'Stall' ,'Driver',
                          'Fasttag', 'Wifi' ,'Pet food','Vet', 'Petrol', 'Others' ,'Unknown']
    
    i_category_list.sort()
    i_sub_category_list.sort()
    
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
    
    
    expensetab1, expensetab2, expensetab3= st.tabs(['Expenses split', 'Salary split', 'Raw data'])
    
    with expensetab1:
        split1, split2= st.columns(2)
        fig = px.pie(df_expense, values='Amount', names='Type')
        split1.plotly_chart(fig)
        
        fig = px.pie(df_expense, values='Amount', names='Category')
        split1.plotly_chart(fig)
        
    
        
    with expensetab2:
        split1, split2, split3= st.columns(3)
        needs_pc= split1.number_input('Needs', value= 40, step=10,min_value= 10,  max_value= 100)
        wants_pc= split2.number_input('Wants',value= 20, step=10,min_value= 10,  max_value= 100)
        investment_pc= split3.number_input('Investment', value= 40, step=10,min_value= 10,  max_value= 100)
        
        
        total_income= df_expense['Credit'].sum()
        needs_income= total_income * (needs_pc/100)
        wants_income= total_income * (wants_pc/100)
        investment_income= total_income * (investment_pc/100)
        
        needs_expense= df_expense[df_expense['Type']== 'mandatory']['Amount'].sum()
        wants_expense= df_expense[df_expense['Type']== 'optional']['Amount'].sum()
        investment_expense= df_expense[df_expense['Type']== 'mandainvestmenttory']['Amount'].sum()
        
        
        
        bucket= [needs_income,wants_income, investment_income ]
        bucket_used= [needs_expense, wants_expense, investment_expense]
        
        df_khata= pd.DataFrame( columns=['Bucket', 'Used'])
        df_khata['Bucket']= bucket
        df_khata['Used']=  bucket_used
        df_khata['Remaining']= df_khata['Bucket'] - df_khata['Used']
        
        df_khata.index= ['Needs', 'Wants', 'Investment']
        
        df_khata.loc["Total"] = df_khata.sum()
        df_khata['Used %'] = df_khata['Used']/ df_khata['Bucket'] * 100
        st.table(df_khata)
        
        
        
        
        
        
    with expensetab3:
        df_expense= df_expense.sort_values(by='Date', ascending= False)
        st.table(df_expense)
        
def download_sheet():
    df_expense= pd.read_csv('files/expenses.csv') 
    def convert_df(df):
       return df.to_csv().encode('utf-8')
    
    
    csv = convert_df(df_expense)
    
    st.download_button(
       "Press to Download",
       csv,
       "expenses.csv",
       "text/csv",
       key='download-csv'
    )
    
        
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    