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

import BrainiacExpenses, BrainiacList, BrainiacExercise


st.set_page_config(layout='wide',page_title="Second Brain")
st.set_option('deprecation.showPyplotGlobalUse', False)

with st.sidebar:
    i_page= option_menu('Brainiac', ['Expenses', 'Groceries List', 'Reminder', 'Idea', 'Workout'],
                        default_index=0, icons=['wallet-fill', 'list-check','alarm-fill', 'lightbulb-fill' , 'activity'], menu_icon= 'cast')
    
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
    
if i_page == 'Workout':
    BrainiacExercise.add_workout()
    
    
    
       
            
    
        
    
    