'''
to run the app:-
1. open termintal ctrl+j
2. type 'streamlit run app.py'
'''


from tkinter.ttk import Style
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
import seaborn as sns
import streamlit as st

@st.cache
def load_data():
    df = pd.read_csv('Gender Pay Gap.csv')
    return df
df = load_data()
st.title('Gender Pay Gap')
st.image('https://miro.medium.com/max/540/1*J_EXEmUkOcg-rgzJudUhZQ.png')
st.header('This is an analysis with the Graphs')
st.sidebar.header('Menu')
ops=['Intro','Analysis Job Title','Analysis (IT, Graphic Designer, Data Scientist)','Histogram:Base pay and Job Title','Box Plot between all Fields','Histogram between Marketing Associate and Graphic Designer', 'Bar chart on bases of Education ']
choice=st.sidebar.selectbox('Select an option',ops)
if choice==ops[0]:
    st.write('In this analysis we can understand that, which field effects salary. This analysis gives infromation about Male and Female salary difference whth respect of different fields.  ')
    st.write('Summary :-1 It shows the Basepay of people in different field, 2 In this analysis we get that in the Data scientis , Female get highest pay in compariosn to Male. Male get approx equal salary in IT and data scientist, 3 we check on the condition in IT where age is less than 25, we see that male have much salary then female , 4 we find that software engineer get maximum pay, 5 Male Manager get max pay, 6 we see that there are more males in Graphic Designer field and females in Marketing Associate field , whose salary is less 40K and exp greater than 2 yrs, 7 Phd holder get higher salary in comparison to others')
elif choice==ops[1]:
    ops2=['Pie','Histogram']
    choice2=st.selectbox('Select an option',ops2)
    if choice2==ops2[0]:
        st.subheader('Here in this figure we can see that, how many people are in a particular field.')
        fig1 =px.pie(df,names='JobTitle')
        st.plotly_chart(fig1)
        btn = st.button('Show result')
        if btn:
            st.subheader('It shows the Basepay of people in different field')
    if choice2==ops2[1]:
        st.subheader('Here in this figure we can see the difference between basepay.')
        fig1 =px.histogram(df,x='JobTitle',color='Gender')
        st.plotly_chart(fig1)
        btn = st.button('Show result')
        if btn:
            st.subheader('In this analysis we get that in the Data scientis , Female get highest pay in compariosn to Male. Male get approx equal salary in IT and data scientist')
    

elif choice==ops[2]:
    ops2=['Histogram','Box']
    choice2=st.selectbox('Select an option',ops2)
    if choice2==ops2[0]:
        st.subheader('It shows the gender pay gap for the fields')

        f1  = df['JobTitle'] == 'IT' # boolean filter
        f2  = df['JobTitle'] == 'Graphic Designer' # boolean filter
        f3  = df['JobTitle'] == 'Data Scientist' # boolean filter
        df2=df[f1 | f2 | f3]

        sns.set(style="dark")
        fig2=plt.figure(facecolor='grey',figsize=(15,5))
        sns.barplot(x="JobTitle", y = "BasePay", data=df2, hue='Gender')
        plt.xticks(rotation=90)
        st.pyplot(fig2)
    if choice2==ops2[1]:
        st.subheader(' With the help of this fig. we can see the max, median , min, q1 and q2 values of some specific fields like(Graphiac Designer, IT, Data Scientist)')

        f1  = df['JobTitle'] == 'IT' # boolean filter
        f2  = df['JobTitle'] == 'Graphic Designer' # boolean filter
        f3  = df['JobTitle'] == 'Data Scientist' # boolean filter
        df2=df[f1 | f2 | f3]
        fig5 = px.box(df2,x="JobTitle", y = "BasePay", color='Gender', color_discrete_sequence=['Yellow','Orange'])
        st.plotly_chart(fig5)
        btn = st.button('Show Result')
        if btn:
            st.subheader('In this analysis we get that in the Data scientis , Female get highest pay in compariosn to Male')

    st.subheader('Here In this figure we used condition that is Jobtitle IT and Age >25')
    g1 = df['JobTitle'] =='IT'
    g2 = df['Age'] >=25
    df3=df[g1 & g2]
    sns.set(style="white")
    fig3=plt.figure(facecolor='grey')
    sns.barplot(x="JobTitle", y = "BasePay", data=df3, hue='Gender',palette='copper_r')
    plt.xticks(rotation=90)
    st.pyplot(fig3)

    btn = st.button('Show result')
    if btn:
        st.subheader('we check on the condition in IT where age is less than 25, we see that male have much salary then female')

elif choice==ops[3]:
    st.subheader('Here we can see the histogram with respect of jobtitles and basepay')
    
    fig4 = px.histogram(df,x='JobTitle',y='BasePay', color='JobTitle')
    st.plotly_chart(fig4)
    btn = st.button('Show Result')
    if btn:
        st.subheader('we find that software engineer get maximum pay')
    

elif choice==ops[4]:
    st.subheader('With the help of this fig. we can see the max, median , min, q1 and q2 values of all the fields of JobTitle.')
    
    fig6 = px.box(df,x="JobTitle", y = "BasePay", color='Gender', color_discrete_sequence=['Yellow','Orange'])
    st.plotly_chart(fig6)
    btn = st.button('Show Results')
    if btn:
        st.subheader('Male Manager get max pay')

elif choice==ops[5]:
    st.subheader('Histogram with condition aplly in seniorty{experience},BasePay')
     
    c1 = df['BasePay'] <= 40000 
    c2 = df['Seniority'] >= 2
    df4 = df[c1 & c2]  
    fig7 = px.histogram(df4,x="JobTitle", y = "BasePay", color='Gender', color_discrete_sequence=['LightGreen','Pink'], height=500, width=1000)
    st.plotly_chart(fig7)
    btn = st.button('Show Result')
    if btn:
        st.subheader('we see that there are more males in Graphic Designer field and females in Marketing Associate field , whose salary is less 40K and exp greater than 2 yrs.')

elif choice==ops[6]:
    st.subheader('Bar chart between education and basepay')
      
    fig8=plt.figure()
    sns.barplot(x="Education", y="BasePay", data=df)
    st.pyplot(fig8)
    btn = st.button('Show Result')
    if btn:
        st.subheader('Phd holder get higher salary in comparison to others')
