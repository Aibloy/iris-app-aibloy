# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 20:38:55 2020

@author: Willi
"""
# Run en linea de comandos:  !streamlit run IRIS_APP.py


import streamlit as st

# EDA 
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
from PIL import Image,ImageEnhance, ImageFilter
#-------------------------------------------------------------
#Title
st.title("IRIS EDA ")
st.header("Streamlit App")
#-------------------------------------------------------------
# Dataframe

path = "iris.csv"
#-------------------------------------------------------------
@st.cache
def load_data(path):
    data = pd.read_csv(path)
    return data 
data = load_data(path)
#-------------------------------------------------------------

if st.sidebar.checkbox("Preview Dataset"):
    if st.button("Head"):
        st.write(data.head())
    if st.button("Tail"):
        st.write(data.tail())

#-------------------------------------------------------------        
if st.sidebar.checkbox("Show ALL dataset"):
    st.write(data)
#-------------------------------------------------------------    
# Column Names
if st.sidebar.checkbox("Show Column Names"):
    st.write(data.columns)
#-------------------------------------------------------------
#Summary
if st.sidebar.checkbox("Show summary"):
    st.write(data.describe())
        
    
#-------------------------------------------------------------
d = ["Rows","Columns","ALL"]
data_dim = st.sidebar.radio("Select Dimensions to see:",tuple(d))

for i in d:
    if data_dim == i:
        # st.text(f"Showing {i}")
        
        if i == "ALL":
            st.header(f"Shape {i} : {data.shape}")
        else:
            st.header(f"Shape {i} : {data.shape[d.index(i)]}")
    
    
if st.sidebar.checkbox("Show Correlations "):
    corr = data.corr()
    cmap = plt.cm.RdBu
    plt.title('Correlación Pearson', size=15)
    st.write(sns.heatmap(corr, cmap=cmap,  annot=True, linewidths=1))
    st.pyplot()


#-------------------------------------------------------------
if st.sidebar.checkbox("Show columns"):
    # Select Column:
    columnas = data.columns
    col = st.sidebar.selectbox("Select Column",tuple(columnas))
    st.write(data[col])
    
    #-------------------------------------------------------------
    if st.sidebar.checkbox("Show Histogram: "):
        st.write(data[col].plot(kind="hist"))
        st.pyplot()
    
#-------------------------------------------------------------
@st.cache
def load_image(path):
    imagen = Image.open(path)
    return imagen
    

tipos = data["Species"].unique()
species_type = st.sidebar.radio("Select type: ", tuple(tipos))
st.title(f"Showing {species_type}")
st.image(load_image(f"{species_type}.jpg"))
    

     
        


    
    

    

    
    



