# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 13:45:39 2022

@author: Sumit
"""
import streamlit as st
import pandas as pd


def get_list():
    
    listcol1, listcol2, listcol3= st.columns(3)
    
    df_list= pd.read_csv('files/groceries_list.csv')  

    checklist_done=[]

    if listcol2.button("Reset All"):
        df_list['Check']= ''
        df_list.to_csv('files/groceries_list.csv', index=False)
        
    


    list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11= st.tabs(['Food grains', 'Oil', 'Masala', 'Beverages', 'Beauty & hygiene', 
                                                       'Bakery, Dairy & Eggs', 'Dry fruits', 'Breakfast & Snacks', 'Cleaning & household',
                                                      'Pooja needs', 'Others' ])
    
    all_tabs= [list1, list2, list3, list4, list5, list6, list7, list8, list9, list10, list11]
    all_categories= ['Food grains', 'Oil', 'Masala', 'Beverages', 'Beauty & hygiene', 
                                                       'Bakery, Dairy & Eggs', 'Dry fruits', 'Breakfast & Snacks', 'Cleaning & household',
                                                      'Pooja needs', 'Others' ]
    tab_dict = dict(zip(all_tabs, all_categories))  # this will map all tabs with groceries categories, so that it can be run on loop
    for i_tab in all_tabs:
        with i_tab:
            df_list_cat= df_list[df_list['Category']== tab_dict[i_tab]]
            for index, row in df_list_cat.iterrows():
                if row['Check'] == 'X':
                    is_checked = True
                else:
                    is_checked = False
                item_check= st.checkbox(row['Item'], value= is_checked)
                if item_check:
                    checklist_done.append(row['Item'])
      
    
  
    
    
    check_mark=[]   
    for index, row in df_list.iterrows():
        if row['Item'] in checklist_done:
            check_mark.append("X")
        else:
            check_mark.append("")
           
    df_list['Check']= check_mark        
    
    
    
    if listcol1.button("Save list"):
        df_list.to_csv('files/groceries_list.csv', index=False)
   
    
    
    
    
    
   