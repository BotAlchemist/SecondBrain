# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 07:12:06 2022

@author: Sumit
"""

import streamlit as st
import pandas as pd
from datetime import date

def add_workout():
    
    tab1, tab2, tab3= st.tabs(['Daily workout', 'Help', 'Download sheet'])
    
    
    with tab1: # Daily workout
        
        today = date.today()
        i_date= st.date_input("Date", today)
        i_equipment= st.selectbox("Equipment", ['5kg dumbell', '3kg dumbell'])
        exercise_name_list= ['Biceps curl', 'Squat', 'One Arm row', 'Two arm bicep curl','Push up', 'Lateral raise', 'Overhead press', 'French press', 'Crunch', 'Leg raise']
        
        
        with st.form("workout_form"):
            work1, work2, work3= st.columns(3)
            row=[]
            for i_name in exercise_name_list:
                work1.text_input("Exercise name", i_name)
                no_reps= work2.number_input('Reps', value= 0, step=5,min_value= 0,  max_value= 20, key= i_name)
                no_sets= work3.number_input('Sets', value= 0, step=1,min_value= 0,  max_value= 5, key= i_name+ 'set')
                row.append([i_date, i_name,i_equipment,  no_reps, no_sets])                
            
            workout_submit = work1.form_submit_button("Done")
            if workout_submit:
                
                df_today_workput= pd.DataFrame(row, columns=['Date', 'Name', 'Equipment', 'Reps', 'Set'])
                df_today_workput['Volume']= df_today_workput['Reps'] * df_today_workput['Set']
                
                total_volume= df_today_workput['Volume'].sum()
                
                df_workout= pd.read_csv('files/workout_planner.csv')
                df_workout= df_workout.dropna()
                df_workout= df_workout.append(df_today_workput, ignore_index=True)
                df_workout.to_csv('files/workout_planner.csv', index=False)
                
                st.success("Congratulations! You completed your workout.")
                st.subheader('Total volume: ' + str(total_volume))
                
                
        
    with tab2: # help
        link='https://www.youtube.com/watch?v=AXZlb-3MMYE'
        st.success(link)
        
    with tab3: # download sheet
        df_workout= pd.read_csv('files/workout_planner.csv') 
        def convert_df(df):
           return df.to_csv().encode('utf-8')
        
        
        csv = convert_df(df_workout)
        
        st.download_button(
           "Press to Download",
           csv,
           "expenses.csv",
           "text/csv",
           key='download-csv'
        )
        
    
            