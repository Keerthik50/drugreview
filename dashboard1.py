import pandas as pd
import plotly.express as px
import streamlit as st
df =pd.read_csv('webmd.csv')
st.set_page_config(layout='wide')
st.header('Drug Review Analysis')

st.image('images.jpg')
page=st.sidebar.selectbox('select page',['Condition','Age','Date','Drug','DrugId','EaseofUse','Effectiveness','Reviews','Satisfaction','Sex','Sides','UsefulCount'])
if page == 'Condition':
    uni_list=df['Condition'].unique()
    col1,col2=st.columns(2)
    condition = st.sidebar.selectbox('Select a Condition',uni_list)
    fig=px.line(df[df['Condition']==condition],x='Drug',y='UsefulCount')
    col1.plotly_chart(fig)
    col2.plotly_chart(fig,use_container_width=True)
elif page == 'Age' :
    uni_list=df['Age'].unique()
    col1,col2=st.columns(2)
    age=st.sidebar.selectbox('Select a Age',uni_list)
    fig=px.line(df[df['Age']==age],x='Drug',y='UsefulCount')
    col1.plotly_chart(fig)
    col2.plotly_chart(fig,use_container_width=True)
elif page == 'Date' :
    uni_list=df['Date'].unique()
    col1,col2=st.columns(2)
    date=st.sidebar.selectbox('Select a Date',uni_list)
    fig=px.line(df[df['Date']==date],x='Drug',y='Condition')
    col1.plotly_chart(fig)
    col2.plotly_chart(fig,use_container_width=True)
elif page == 'Drug' :
    uni_list=df['Drug'].unique()
    col1,col2=st.columns(2)
    drug=st.sidebar.selectbox('Select a Drug',uni_list)
    fig=px.line(df[df['Drug']==drug],x='Age',y='Condition')
    col1.plotly_chart(fig)
    col2.plotly_chart(fig,use_container_width=True)
elif page == 'DrugId' :
    uni_list=df['DrugId'].unique()
    col1,col2=st.columns(2)
    drugId=st.sidebar.selectbox('Select a DrugId',uni_list)
    fig=px.line(df[df['DrugId']==drugId],x='Drug',y='Condition')
    col1.plotly_chart(fig)
    col2.plotly_chart(fig,use_container_width=True)
elif page == 'EaseofUse' :
    uni_list=df['EaseofUse'].unique()
    col1,col2=st.columns(2)
    easeofUse=st.sidebar.selectbox('Select a EaseofUse',uni_list)
    fig=px.line(df[df['EaseofUse']==easeofUse],x='Drug',y='Condition')
    col1.plotly_chart(fig)
    col2.plotly_chart(fig,use_container_width=True)
elif page == 'Effectiveness' :
    uni_list=df['Effectiveness'].unique()
    col1,col2=st.columns(2)
    effectiveness=st.sidebar.selectbox('Select a Effectiveness',uni_list)
    fig=px.line(df[df['Effectiveness']==effectiveness],x='Drug',y='Condition')
    col1.plotly_chart(fig)
    col2.plotly_chart(fig,use_container_width=True)
elif page == 'Reviews' :
    uni_list=df['Reviews'].unique()
    col1,col2=st.columns(2)
    reviews=st.sidebar.selectbox('Select a Reviews',uni_list)
    fig=px.line(df[df['Reviews']==reviews],x='Drug',y='Condition')
    col1.plotly_chart(fig)
    col2.plotly_chart(fig,use_container_width=True)
elif page == 'Satisfaction' :
    uni_list=df['Satisfaction'].unique()
    col1,col2=st.columns(2)
    satisfaction=st.sidebar.selectbox('Select a Satisfaction',uni_list)
    fig=px.line(df[df['Satisfaction']==satisfaction],x='Drug',y='Condition')
    col1.plotly_chart(fig)
    col2.plotly_chart(fig,use_container_width=True)
elif page == 'Sex' :
    uni_list=df['Sex'].unique()
    col1,col2=st.columns(2)
    sex=st.sidebar.selectbox('Select a Sex',uni_list)
    fig=px.line(df[df['Sex']==sex],x='Drug',y='Condition')
    col1.plotly_chart(fig)
    col2.plotly_chart(fig,use_container_width=True)
elif page == 'Sides' :
    uni_list=df['Sides'].unique()
    col1,col2=st.columns(2)
    sides=st.sidebar.selectbox('Select a Sides',uni_list)
    fig=px.line(df[df['Sides']==sides],x='Drug',y='Condition')
    col1.plotly_chart(fig)
    col2.plotly_chart(fig,use_container_width=True)
else:
    uni_list=df['UsefulCount'].unique()
    col1,col2=st.columns(2)
    usefulCount=st.sidebar.selectbox('Select a UsefulCount',uni_list)
    fig=px.line(df[df['UsefulCount']==usefulCount],x='Drug',y='Condition')
    col1.plotly_chart(fig)
    col2.plotly_chart(fig,use_container_width=True)





