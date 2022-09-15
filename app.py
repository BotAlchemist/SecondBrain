# -*- coding: utf-8 -*-
"""
Created on Thu Sep  8 16:37:28 2022

@author: Sumit
"""

import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import date

import BrainiacExpenses, BrainiacList, BrainiacExercise, BrainiacBook, BrainiacReminder


st.set_page_config(layout='wide',page_title="Second Brain")
st.set_option('deprecation.showPyplotGlobalUse', False)

with st.sidebar:
    i_page= option_menu('Brainiac', ['Expenses', 'Groceries List', 'Reminder', 'Idea', 'Workout', 'Book Summary'],
                        default_index=0, icons=['wallet-fill', 'list-check','alarm-fill', 'lightbulb-fill' , 'activity', 'book'], menu_icon= 'cast')
    
if i_page == 'Expenses':
    tab1, tab2, tab3, tab4= st.tabs(['Add income', 'Add expenses', 'Show graph', 'Download sheet'])
    
    with tab1:
        BrainiacExpenses.add_income()
    
    with tab2:
        BrainiacExpenses.add_expenses()
        
    with tab3:
        BrainiacExpenses.display_graph_expense()
        
    with tab4:
        BrainiacExpenses.download_sheet()
        
        
if i_page == 'Groceries List':
    BrainiacList.get_list()


if i_page== 'Reminder':
    remindtab1, remindtab2= st.tabs(['Show reminder', 'Set reminder'])
    with remindtab1:
        BrainiacReminder.show_reminder()
    with remindtab2:
        BrainiacReminder.set_reminder()
    



    
if i_page == 'Workout':
    BrainiacExercise.add_workout()
    
if i_page== 'Book Summary':
    booktab1, booktab2, booktab3= st.tabs(['Add book','Add summary', 'View Summary'])
    
    with booktab1:
        BrainiacBook.add_book()
        
    
    with booktab2:
        BrainiacBook.add_summary()
        
    with booktab3:
        BrainiacBook.get_summary()
        
    
    
    
       
            
    
        
    
    