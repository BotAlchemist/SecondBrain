# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 08:30:04 2022

@author: Sumit
"""

import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, timedelta

def set_reminder():
    df_reminder= pd.read_csv('files/reminders.csv')  
    
    today = date.today()
    
    #with st.form("Set reminder", clear_on_submit=True):
    i_reminder= st.selectbox('Reminder',df_reminder['Reminder'].unique() )
    i_recharge_date= st.date_input("Recharge date", today)
    i_period= st.number_input("Remind after (days)", value= 30, step=1,min_value= 0,  max_value= 365)
    
    
    next_recharge_date= i_recharge_date + timedelta(days=i_period)
    i_next_recharge_date= st.date_input("Next recharge date", next_recharge_date)
    
    reminder_submit = st.button("Set reminder")
        
  
    if reminder_submit:
        df_reminder.loc[df_reminder["Reminder"] == i_reminder, "Last recharged date"] = i_recharge_date
        df_reminder.loc[df_reminder["Reminder"] == i_reminder, "Recharge period"] = i_period
        df_reminder.loc[df_reminder["Reminder"] == i_reminder, "Next Recharge date"] = i_next_recharge_date
        df_reminder.to_csv('files/reminders.csv', index=False)
        st.success("Reminder set successfully")
        
           
   
    
    
def show_reminder():
    today = pd.to_datetime('today').normalize()
    df_reminder= pd.read_csv('files/reminders.csv', dayfirst=True, parse_dates=[1, 3]) 
    df_reminder["Last recharged date"] = pd.to_datetime(df_reminder["Last recharged date"])#.dt.date
    df_reminder["Next Recharge date"] = pd.to_datetime(df_reminder["Next Recharge date"])#.dt.date
    #df_reminder= df_reminder[df_reminder["Next Recharge date"] >= today]
    df_reminder['Today']= today#- df_reminder["Next Recharge date"]
    df_reminder['Remind in (days)'] = (df_reminder['Next Recharge date'] - df_reminder['Today']) / np.timedelta64(1, 'D')
    
    
    df_reminder= df_reminder.sort_values(by='Next Recharge date')

    
    
    df_reminder["Last recharged date"] = pd.to_datetime(df_reminder["Last recharged date"]).dt.strftime('%d-%B-%Y')
    df_reminder["Next Recharge date"] = pd.to_datetime(df_reminder["Next Recharge date"]).dt.strftime('%d-%B-%Y')
    df_reminder['Remind in (days)'] = df_reminder['Remind in (days)'].astype(int)
    df_reminder= df_reminder.drop(['Today', 'Recharge period'], axis=1)
    
    def color_reminder(val):
        color = 'red' if val<=3 else 'green' 
        return f'background-color: {color}'
    st.table(df_reminder.style.applymap(color_reminder, subset=['Remind in (days)']))
    #st.dataframe(df_reminder)
    
    