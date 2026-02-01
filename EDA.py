import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
st.sidebar.title("Welcome to EDA ")
st.header("Smart EDA")
st.image("imgeEDA.jpg",use_container_width=True)
upload_file=st.file_uploader("Upload your csv here ",type=["csv"])
if(upload_file):
    df=pd.read_csv(upload_file)
    st.dataframe(df.head())
    st.success(f"Data Load successfully")
    x=st.selectbox("Select X axis",options=df.columns)
    y=st.selectbox("select y axis",options=df.columns)
    z=st.selectbox("which graph u want to plot",options=["scatterplot","lineplot","histplot","barplot"])
    if(z=="scatterplot"):
        plt.figure(figsize=(10,6))
        sns.scatterplot(data=df,x=x,y=y)
        st.pyplot(plt)
    elif(z=="lineplot"):
        plt.figure(figsize=(10,6))
        sns.lineplot(data=df,x=x,y=y)
        st.pyplot(plt)
    elif(z=="histplot"):
        plt.figure(figsize=(10,6))
        sns.histplot(data=df,x=x)
        st.pyplot(plt)
    elif(z=="barplot"):
        plt.figure(figsize=(10,6))
        sns.barplot(data=df,x=x,y=y)
        st.pyplot(plt)
