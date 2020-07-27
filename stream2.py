# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 16:22:32 2020

@author: aamir
"""
import datetime
import streamlit as st
from streamlit import caching
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from sklearn.linear_model import LinearRegression
import numpy as np
import geopandas as gpd
import seaborn as sns
import matplotlib.pyplot as plt

html = """
  <style>
    .reportview-container {
      flex-direction: row-reverse;
    }

    header > .toolbar {
      flex-direction: row-reverse;
      left: 1rem;
      right: auto;
    }

    .sidebar .sidebar-collapse-control,
    .sidebar.--collapsed .sidebar-collapse-control {
      left: auto;
      right: 0.5rem;
    }

    .sidebar .sidebar-content {
      transition: margin-right .3s, box-shadow .3s;
    }

    .sidebar.--collapsed .sidebar-content {
      margin-left: auto;
      margin-right: -21rem;
    }

    @media (max-width: 991.98px) {
      .sidebar .sidebar-content {
        margin-left: auto;
      }
    }
  </style>
"""
st.markdown(html, unsafe_allow_html=True)

@st.cache
def load_data():
    ddl=pd.read_csv('https://raw.githubusercontent.com/aamirmiy/Covid19/master/ddl.csv')
    d=pd.read_csv('https://raw.githubusercontent.com/aamirmiy/Covid19/master/d.csv')
    df=pd.read_csv('https://raw.githubusercontent.com/aamirmiy/Covid19/master/final_sentiment.csv')
    return ddl,d,df
ddl,d,df=load_data()
colors=['#636EFA','#EF553B','#00CC96','#AB63FA','#FFA15A','#19D3F3','#FF6692']
activities=['Map','Polarity and Subjectivity','Sentiments of States','Sentiment Analysis','Conclusion']
st.sidebar.markdown("**Features to explore**")
option=st.sidebar.selectbox('',activities)

st.title('Covid-19 Sentiment Analysis')

####################################################1
if option == 'Map':
    st.header("Overall change in polarity over different months.")
    
    st.write('Decreasing value of polarity shows increase in negative emotions')
    option = st.sidebar.radio('',['March','April','May','June'])
    @st.cache(suppress_st_warning=True)
    def march_map():
        f= 'https://raw.githubusercontent.com/TwiggiestOak18/data/master/march_map.csv'
        df_ms = pd.read_csv(f)
        state_wise_polairty_m = df_ms[['Place', 'Polarity', 'Month']]
        data_for_map_m = state_wise_polairty_m[state_wise_polairty_m['Month']=='March']
    
        fp = "C:/Users/aamir/Downloads/Indian_States.shp"
        map_df = gpd.read_file(fp)
        
        merged_m = map_df.set_index('st_nm').join(data_for_map_m.set_index('Place'))
        fig1, ax = plt.subplots(1, figsize=(10, 6))
        ax.axis('off')
        ax.set_title('Polarity March', fontdict={'fontsize': '25', 'fontweight' : '3'})
    
        merged_m.plot(column='Polarity', cmap='YlGnBu', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
        
        return st.write(fig1)
    if option=="March":
        march_map()
        caching.clear_cache()
        st.write('<i>The polarity in the month of March was majorly positive in most states as the pandemic did not hit the country on a large scale. It can be seen that only a few states in the south were affected and had a comparatively lower polarity . On the 21st of March, the PM, Shri Narendra Modi, announced a nationwide lockdown  in order to prevent the virus from spreading further. As social distancing was the norm during this period , it would later have the effect on the general public as it can be seen in the map portraying the polarity of emotions in the month of April.</i>',unsafe_allow_html=True)
        st.markdown("<hr></hr>",unsafe_allow_html=True)
        st.markdown("Kindly use the side bar to navigate and view the features as per your desire -->")
    @st.cache(suppress_st_warning=True)
    def april_map():
        a='https://raw.githubusercontent.com/TwiggiestOak18/data/master/april_map.csv'
        df_as= pd.read_csv(a)
        state_wise_polairty_a = df_as[['Place', 'Polarity', 'Month']]
        data_for_map_a = state_wise_polairty_a[state_wise_polairty_a['Month']=='April']
    
        fp = "C:/Users/aamir/Downloads/Indian_States.shp"
        map_df = gpd.read_file(fp)
        
        merged_a = map_df.set_index('st_nm').join(data_for_map_a.set_index('Place'))
    
        fig2, ax = plt.subplots(1, figsize=(10, 6))
        ax.axis('off')
        ax.set_title('Polarity April', fontdict={'fontsize': '25', 'fontweight' : '3'})
    
        merged_a.plot(column='Polarity', cmap='YlGnBu', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    
        return st.write(fig2)
    if option=="April":
        april_map()
        caching.clear_cache()
        st.write('<i>As people were getting accustomed to the lockdown, the polarity scale on the map shows that the people were not happy during these times. It is because of the whole ordeal which the country had to go through due to the ongoing pandemic. As the result, the polarity throughout this month was constantly low as the people tried to adjust to the quarantine lifestyle.</i>',unsafe_allow_html=True)
        st.markdown("<hr></hr>",unsafe_allow_html=True)
        st.markdown("Kindly use the side bar to navigate and view the features as per your desire -->")
    @st.cache(suppress_st_warning=True)
    def may_map():
        may='https://raw.githubusercontent.com/TwiggiestOak18/data/master/may_map.csv'
        df_mas= pd.read_csv(may)
        state_wise_polairty_may = df_mas[['Place', 'Polarity', 'Month']]
        data_for_map_may = state_wise_polairty_may[state_wise_polairty_may['Month']=='May']
    
        fp = "C:/Users/aamir/Downloads/Indian_States.shp"
        map_df = gpd.read_file(fp)
    
        merged_may = map_df.set_index('st_nm').join(data_for_map_may.set_index('Place'))
    
        fig3, ax = plt.subplots(1, figsize=(10, 6))
        ax.axis('off')
        ax.set_title('Polarity May', fontdict={'fontsize': '25', 'fontweight' : '3'})
    
        merged_may.plot(column='Polarity', cmap='YlGnBu', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    
        return st.write(fig3)
    if option=="May":
        may_map()
        caching.clear_cache()
        st.write('<i>In the month of May, things got worse as the number of cases skyrocketed and the lockdown was further extended to contain the increasing rate of positive cases per day and to control the further spread of the virus. The daily wage workers suffered massively during this time as the work came to a halt and the source of income was cut-off. When these people tried returning to their homes, they faced immense challenges as there was a huge transportation problem in the country due to restrictions on inter-district and interstate travels. So without money and a roof on their heads the poor suffered greatly during these hard times, creating a sympathetic and sad emotion in the entire country which can be seen in the map and the lowest polarity, worse than that of April.</i>',unsafe_allow_html=True)
        st.markdown("<hr></hr>",unsafe_allow_html=True)
        st.markdown("Kindly use the side bar to navigate and view the features as per your desire -->")
    @st.cache(suppress_st_warning=True)
    def june_map():
        j='https://raw.githubusercontent.com/TwiggiestOak18/data/master/june_map.csv'
        df_js=pd.read_csv(j)
        state_wise_polairty_j = df_js[['Place', 'Polarity', 'Month']]
        data_for_map_j = state_wise_polairty_j[state_wise_polairty_j['Month']=='June']
    
        fp = "C:/Users/aamir/Downloads/Indian_States.shp"
        map_df = gpd.read_file(fp)  
        
        merged_j = map_df.set_index('st_nm').join(data_for_map_j.set_index('Place'))
    
        fig4, ax = plt.subplots(1, figsize=(10, 6))
        ax.axis('off')
        ax.set_title('Polarity June', fontdict={'fontsize': '25', 'fontweight' : '3'})
    
        merged_j.plot(column='Polarity', cmap='YlGnBu', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
    
        return st.write(fig4)
    if option=="June":
        june_map()
        caching.clear_cache()
        st.write('<i>Contradictory to the trend in the past few months the situation started improving as people were now gradually accustomed to the quarantine lifestyle and many also returned to their work hence starting the economic wheel. Although at a slower pace, it wad better than the absolute halt which affected the whole country and put it in an economic turmoil .The news on the development of vaccines increased the hope of ending this pandemic sooner and thus people were in a much better mood compared to the past few months.</i>',unsafe_allow_html=True)
        st.markdown("<hr></hr>",unsafe_allow_html=True)
        st.markdown("Kindly use the side bar to navigate and view the features as per your desire -->")
#####################################################################       
elif option == 'Sentiment Analysis':
    #data = [['Sentiment Level %', 'A proxy for the intensity of a certain sentiment','count(tweets with a certain sentiment)/count(total tweets)']] 
    #df = pd.DataFrame(data, columns = ['Metric Name', 'What does it mean','How we calculate it'])
    #st.table(df)
    html = """
    <head>
    </head>
    <body>
    <table style='font-family: arial, sans-serif;border-collapse: collapse;width: 100%;'>
      <tr style='background-color: #dddddd;'>
        <th style='text-align:center;border: 3px solid #dddddd;padding: 5px;'>Metric Name</th>
        <th style='text-align:center;border: 3px solid #dddddd;padding: 5px;'>What does it mean</th>
        <th style='text-align:center;border: 3px solid #dddddd;padding: 5px;'>How we calculate it</th>
      </tr>
      <tr>
        <td style='border: 3px solid #dddddd;text-align: center;padding: 5px;'>Sentiment Level%</td>
        <td style='border: 3px solid #dddddd;text-align: center;padding: 5px;'>A proxy for the intensity of a certain sentiment</td>
        <td style='border: 3px solid #dddddd;text-align: center;padding: 5px;'>count(tweets with a certain sentiment)÷count(total tweets)</td>
      </tr>
    </table>
    </body>
    """
    st.markdown(html, unsafe_allow_html=True)
    st.markdown('<hr></hr>',unsafe_allow_html=True)
    fig = make_subplots(
        rows=4, cols=2,horizontal_spacing=0.07,vertical_spacing=0.05,x_title="Date",y_title="% Change",
        specs=[[{},{}],[{},{}],[{},{}],[{},{}]],
            
        subplot_titles=("All","Analytical","Anger","Confident","Fear","Joy","Neutral","Sadness"))
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Analytical']),line=dict(color=colors[0]),name="Analytical"
                        ),row=1,col=1)
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Anger']),line=dict(color=colors[1]),name="Anger"
                        ),row=1,col=1)
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Confident']),line=dict(color=colors[2]),name="Confident"
                    ),row=1,col=1)
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Fear']),line=dict(color=colors[3]),name="Fear"
                        ),row=1,col=1)
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Joy']),line=dict(color=colors[4]),name="Joy"
                        ),row=1,col=1)
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Neutral']),line=dict(color=colors[5]),name="Neutral"
                        ),row=1,col=1)
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Sadness']),line=dict(color=colors[6]),name="Sadness"
                        ),row=1,col=1)
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Analytical']),line=dict(color=colors[0]),name="Analytical"),
                     row=1, col=2)
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Anger']),line=dict(color=colors[1]),name="Anger"),
                     row=2, col=1)
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Confident']),line=dict(color=colors[2]),name="Confident"),
                        row=2, col=2)
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Fear']),line=dict(color=colors[3]),name="Fear"),
                        row=3, col=1)
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Joy']),line=dict(color=colors[4]),name="Joy"),
                        row=3, col=2)
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Neutral']),line=dict(color=colors[5]),name="Neutral"),
                        row=4, col=1)
    fig.add_trace(go.Scatter(x=list(ddl['Datetime']), y=list(ddl['Sadness']),line=dict(color=colors[6]),name="Sadness"),
                        row=4, col=2)
    fig.update_layout(showlegend=False, title_text="Sentiment level trend",height=1500,width=1000)
    fig.update_yaxes(ticksuffix="%")
    st.write(fig)
    #st.write("From the above graphs we can observe on how the country has reacted to the pandemic in these following months. We observe that the tweets with <b style='color:#FF6692;'>sad</b> sentiments has been linearly increasing day by day. Similar trend can be observed for <b style='color:#19D3F3;'>neutral</b> sentiment. It may look like that the country is not happy or even satisfied for that matter with the current situation regardless of the what the goverment may be doing in order to help the country bounce back on its previous economic status but given the current status of results after emotional analysis it may show the country as emotionaly downed nation but if we look at the first graph we can see that tweets with a more positive emotional status(<b style='color:#FFA15A;'>joy</b>) is way more then tweets of a negative emotional status(<b style='color:#FF6692;'>sadness</b>) and several other emotional traits like <b style='color:#AB63FA;'>fear</b>,<b style='color:#EF553B;'>anger</b>,<b style='color:#00CC96;'>confidence</b>,etc .",unsafe_allow_html=True)
    #
    html='''
    <head>
    </head>
    <body>
    <ul>
        <li><i>We can see that ever since the first case was reported,mixed sentiments arose,which indicates increasing social awareness of the public.</i></li>
        <hr></hr>
        <li><i>% of negative sentiments like <b style="color:#EF553B;">anger</b> and <b style="color:#AB63FA;">fear</b> have constantly remained low while <b style="color:#FF6692;">sadness</b> has had a linear increase throughout owing to the rise in number of deaths.</i></li>
        <hr></hr>
        <li><i>Even though this pandemic has caused a lot of damage people have stayed strong and have remained optimistic.This can be observed with steady increase of the positive sentiment <b style="color:#FFA15A;">joy</b>.</i></li>
        <hr></hr>
        <li><i><b style="color:#636EFA;">"Analytic"</b>(rationality of tweets) is volatile but it has had an overall increase.</i></li>
    </ul>
    </body>
    '''    
    st.subheader('Observations')
    st.write(html,unsafe_allow_html=True)
    st.markdown("<hr></hr>",unsafe_allow_html=True)
    st.markdown("Kindly use the side bar to navigate and view the features as per your desire -->")
######################################################2
elif option == 'Sentiments of States':
    #data = [['Analytical',"A writer's reasoning and analytical attitude about things. Higher value, more likely to be perceived as intellectual, rational, systematic, emotionless, or impersonal."],['Anger',"Likelihood of writer being perceived as angry. Low value indicates unlikely to be perceived as angry. High value indicates very likely to be perceived as angry."],['Confident',"A writer's degree of certainty. Higher value, more likely to be perceived as assured, collected, hopeful, or egotistical."],['Fear',"Likelihood of writer being perceived as scared. Low value indicates unlikely to be perceived as fearful. High value, very likely to be perceived as scared."],['Joy',"Joy or happiness has shades of enjoyment, satisfaction and pleasure. There is a sense of well-being, inner peace, love, safety and contentment."],['Sadness',"Likelihood of writer being perceived as sad. Low value, unlikely to be perceived as sad. High value very likely to be perceived as sad."],['Neutral',"Being neither negative nor positive."]] 
    #d2 = pd.DataFrame(data, columns = ['Sentiment','Description'])
    #st.table(d2)
    html = """
    <head>
    </head>
    <body>
    <table style='font-family: arial, sans-serif;border-collapse: collapse;width: 100%;'>
      <tr style='background-color: #dddddd;'>
        <th style='text-align:center;border: 1px solid #dddddd;padding: 8px;'>Emotion</th>
        <th style='text-align:center;border: 1px solid #dddddd;padding: 8px;'>Description</th>
      </tr>
      <tr>
        <td style='color:#636EFA;border: 1px solid #dddddd;text-align:center;padding: 8px;'><b>Analytical</b></td>
        <td style='border: 1px solid #dddddd;text-align:center;padding: 8px;'><i>A writer's reasoning and analytical attitude about things. Higher value, more likely to be perceived as intellectual, rational, systematic, emotionless, or impersonal.</i></td> 
      </tr>
      <tr>
        <td style='color:#EF533B;border: 1px solid #dddddd;text-align:center;padding: 8px;'><b>Anger</b></td>
        <td style='border: 1px solid #dddddd;text-align:center;padding: 8px;'><i>Likelihood of writer being perceived as angry. Low value indicates unlikely to be perceived as angry. High value indicates very likely to be perceived as angry.</i></td> 
      </tr>
      <tr>
        <td style='color:#00CC96;border: 1px solid #dddddd;text-align:center;padding: 8px;'><b>Confident</b></td>
        <td style='border: 1px solid #dddddd;text-align:center;padding: 8px;'><i>A writer's degree of certainty. Higher value, more likely to be perceived as assured, collected, hopeful, or egotistical.</i></td> 
      </tr>
      <tr>
        <td style='color:#AB63FA;border: 1px solid #dddddd;text-align: center;padding: 8px;'><b>Fear</b></td>
        <td style='border: 1px solid #dddddd;text-align:center;padding: 8px;'><i>Likelihood of writer being perceived as scared. Low value indicates unlikely to be perceived as fearful. High value, very likely to be perceived as scared.</i></td> 
      </tr>
      <tr>
        <td style='color:#FFA15A;border: 1px solid #dddddd;text-align:center;padding: 8px;'><b>Joy</b></td>
        <td style='border: 1px solid #dddddd;text-align:center;padding: 8px;'><i>Joy or happiness has shades of enjoyment, satisfaction and pleasure. There is a sense of well-being, inner peace, love, safety and contentment.</i></td> 
      </tr>
      <tr>
        <td style='color:#FF6692;border: 1px solid #dddddd;text-align:center;padding: 8px;'><b>Sadness</b></td>
        <td style='border: 1px solid #dddddd;text-align:center;padding: 8px;'><i>Likelihood of writer being perceived as sad. Low value, unlikely to be perceived as sad. High value very likely to be perceived as sad.</i></td> 
      </tr>
      <tr>
        <td style='color:#19D3F3;border: 1px solid #dddddd;text-align:center;padding: 8px;'><b>Neutral</b></td>
        <td style='border: 1px solid #dddddd;text-align:center;padding: 8px;'><i>Being neither negative nor positive.</i></td> 
      </tr>
    </table>
    </body>
    """
    st.markdown(html, unsafe_allow_html=True)
    st.write("<hr></hr>",unsafe_allow_html=True)
    st.subheader("For a clear understanding we can compare emotions of each state")
    l=list(df.columns[1:])
    selected_columns=st.multiselect("Select state",l)
    length=len(selected_columns)
    colors=['#636EFA','#EF553B','#00CC96','#AB63FA','#FFA15A','#19D3F3','#FF6692']
    if length==1:
        fig = make_subplots(
            rows=1, cols=1,
            specs=[[{"type": "bar"}]],
            x_title='Sentiments', y_title='Count',
        )
        fig.add_trace(go.Bar(
            x=list(df['Sentiment']),
            y=list(df[selected_columns[0]]),
            text=list(df[selected_columns[0]]),
            name='Emotion',
            marker=dict(color=colors, coloraxis="coloraxis"),
            showlegend=False), 
            row=1, col=1)
        fig.update_traces(texttemplate='%{text:.2s}',textposition='outside')
        fig.update_layout(height=500,width=550,title_text="Emotions with their percentages",title={
            'text': f"{selected_columns[0]}",
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'})
        st.write(fig)
    elif length==2:
        colors=['#636EFA','#EF553B','#00CC96','#AB63FA','#FFA15A','#19D3F3','#FF6692']
        fig = make_subplots(
            rows=1, cols=2,horizontal_spacing=0.03,
            specs=[[{"type": "bar"},{"type": "bar"}]],shared_yaxes=True,
            subplot_titles=(f"{selected_columns[0]}",f"{selected_columns[1]}"),
            x_title='Sentiments', y_title='Count',
        )
        fig.add_trace(go.Bar(
            x=list(df['Sentiment']),
            y=list(df[selected_columns[0]]),
            text=list(df[selected_columns[0]]),
            name='Emotion',
            marker=dict(color=colors, coloraxis="coloraxis"),
            showlegend=False), 
            row=1, col=1)
        fig.update_traces(texttemplate='%{text:.2s}',textposition='outside')
        fig.add_trace(go.Bar(
            x=list(df['Sentiment']),
            y=list(df[selected_columns[1]]),
            text=list(df[selected_columns[1]]),
            name='Emotion',
            marker=dict(color=colors, coloraxis="coloraxis"),
            showlegend=False), 
            row=1, col=2)
        fig.update_traces(texttemplate='%{text:.2s}',textposition='outside')
        fig.update_layout(height=500,width=1000,title_text="Emotions with their percentages")
        st.write(fig)
    elif length==3:
        colors=['#636EFA','#EF553B','#00CC96','#AB63FA','#FFA15A','#19D3F3','#FF6692']
        fig = make_subplots(
            rows=2, cols=2,vertical_spacing=0.1,horizontal_spacing=0.03,
            specs=[[{"type": "bar"},{"type": "bar"}],[{"type": "bar"},None]],
            shared_yaxes=True,
            subplot_titles=(f"{selected_columns[0]}",f"{selected_columns[1]}",f"{selected_columns[2]}"),
            y_title='Count',
        )
        fig.add_trace(go.Bar(
            x=list(df['Sentiment']),
            y=list(df[selected_columns[0]]),
            text=list(df[selected_columns[0]]),
            name='Emotion',
            marker=dict(color=colors, coloraxis="coloraxis"),
            showlegend=False), 
            row=1, col=1)
        fig.update_traces(texttemplate='%{text:.2s}',textposition='outside')
        fig.add_trace(go.Bar(
            x=list(df['Sentiment']),
            y=list(df[selected_columns[1]]),
            text=list(df[selected_columns[1]]),
            name='Emotion',
            marker=dict(color=colors, coloraxis="coloraxis"),
            showlegend=False), 
            row=1, col=2)
        fig.update_traces(texttemplate='%{text:.2s}',textposition='outside')
        fig.add_trace(go.Bar(
            x=list(df['Sentiment']),
            y=list(df[selected_columns[2]]),
            text=list(df[selected_columns[2]]),
            name='Emotion',
            marker=dict(color=colors, coloraxis="coloraxis"),
            showlegend=False), 
            row=2, col=1)
        fig.update_traces(texttemplate='%{text:.2s}',textposition='outside')    
        fig.update_layout(height=1000,width=1000,title_text="Emotions with their percentages")
        st.write(fig)
    elif length==4:
        colors=['#636EFA','#EF553B','#00CC96','#AB63FA','#FFA15A','#19D3F3','#FF6692']
        fig = make_subplots(
            rows=2, cols=2,vertical_spacing=0.1,horizontal_spacing=0.03,
            specs=[[{"type": "bar"},{"type": "bar"}],[{"type": "bar"},{"type": "bar"}]],
            shared_yaxes=True,
            subplot_titles=(f"{selected_columns[0]}",f"{selected_columns[1]}",f"{selected_columns[2]}",f"{selected_columns[3]}"),
            y_title='Count',
        )
        fig.add_trace(go.Bar(
            x=list(df['Sentiment']),
            y=list(df[selected_columns[0]]),
            text=list(df[selected_columns[0]]),
            name='Emotion',
            marker=dict(color=colors, coloraxis="coloraxis"),
            showlegend=False), 
            row=1, col=1)
        fig.update_traces(texttemplate='%{text:.2s}',textposition='outside')
        fig.add_trace(go.Bar(
            x=list(df['Sentiment']),
            y=list(df[selected_columns[1]]),
            text=list(df[selected_columns[1]]),
            name='Emotion',
            marker=dict(color=colors, coloraxis="coloraxis"),
            showlegend=False), 
            row=1, col=2)
        fig.update_traces(texttemplate='%{text:.2s}',textposition='outside')
        fig.add_trace(go.Bar(
            x=list(df['Sentiment']),
            y=list(df[selected_columns[2]]),
            text=list(df[selected_columns[2]]),
            name='Emotion',
            marker=dict(color=colors, coloraxis="coloraxis"),
            showlegend=False), 
            row=2, col=1)
        fig.update_traces(texttemplate='%{text:.2s}',textposition='outside')
        fig.add_trace(go.Bar(
            x=list(df['Sentiment']),
            y=list(df[selected_columns[3]]),
            text=list(df[selected_columns[3]]),
            name='Emotion',
            marker=dict(color=colors, coloraxis="coloraxis"),
            showlegend=False), 
            row=2, col=2)
        fig.update_traces(texttemplate='%{text:.2s}',textposition='outside')    
        fig.update_layout(height=1000,width=1000,title_text="Emotions with their percentages")
        st.write(fig)    
    else:
        st.write("Only upto 4 states can be compared at a time")
    st.markdown("<hr></hr>",unsafe_allow_html=True)
    st.markdown("Kindly use the side bar to navigate and view the features as per your desire -->")
###########################################################3
elif option == 'Polarity and Subjectivity':

    st.write("<h4><u>Polarity</u>:</h4><i>Refers to identifying sentiment orientation (positive, neutral, and negative) in written or spoken language.It is a float which lies in the range of [-1,1].</i>",unsafe_allow_html=True)
    st.markdown("<br>",unsafe_allow_html=True)
    st.write("<h4><u>Subjectivity</u>:</h4><i>It is a float which lies in the range of [0,1].Subjective sentences generally refer to personal opinion, emotion or judgment whereas objective refers to factual information.If subjectivity is close to 0 then the sentence is objective and if it is close to 1 then the sentence is subjective.</i>",unsafe_allow_html=True)
    st.markdown("<hr></hr>",unsafe_allow_html=True)
    st.sidebar.markdown('**Click on the legend to view Subjectivity or Polarity individually**')
    #Subjectivity
    dfn1 = pd.DataFrame({'Date': list(d['Datetime']), 'Subjectivity':list(d['Subjectivity'])})
    dfn1['date_ordinal'] = pd.to_datetime(dfn1['Date']).apply(lambda date: date.toordinal())
    reg1 = LinearRegression().fit(np.vstack(list(dfn1['date_ordinal'])), list(dfn1['Subjectivity']))
    dfn1['bestfit'] = reg1.predict(np.vstack(list(dfn1['date_ordinal'])))
    coef1=reg1.coef_
    #Polarity
    dfn = pd.DataFrame({'Date': list(d['Datetime']), 'Polarity':list(d['Polarity'])})
    dfn['date_ordinal'] = pd.to_datetime(dfn['Date']).apply(lambda date: date.toordinal())
    reg = LinearRegression().fit(np.vstack(list(dfn['date_ordinal'])), list(dfn['Polarity']))
    dfn['bestfit'] = reg.predict(np.vstack(list(dfn['date_ordinal'])))
    coef=reg.coef_
    # Create figure with secondary y-axis
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    # Add traces
    fig.add_trace(go.Scatter(name='Avg.Subjectivity', x=dfn1['Date'], y=dfn1['Subjectivity'].values,legendgroup='group1',mode='lines',line=dict(color='#00CC96')),secondary_y=True,)
    fig.add_trace(go.Scatter(name='Regression', x=list(dfn1['Date']), y=dfn1['bestfit'],legendgroup='group1',line=dict(color='#00CC96',dash='dash')),secondary_y=True,)
    
    fig.add_trace(go.Scatter(name='Avg.Polarity', x=dfn['Date'], y=dfn['Polarity'].values,legendgroup='group2', mode='lines',line=dict(color='#AB63FA')),secondary_y=False,)
    fig.add_trace(go.Scatter(name='Regression', x=list(dfn['Date']), y=dfn['bestfit'],legendgroup='group2',line=dict(dash='dash')),secondary_y=False,)
    # Add figure title
    fig.update_layout(
        title_text="<b>Overall Change</b>",width=900,height=500
    )
    # Set x-axis title
    fig.update_xaxes(title_text="<b>Date[2020]</b>",
        ticktext=["March", "April", "May", "June"],
        tickvals=["2020-03-31", "2020-04-30", "2020-05-31", "2020-06-22"],
    )
    # Set y-axes titles
    fig.update_yaxes(title_text="<b>Polarity</b> ", secondary_y=False)
    fig.update_yaxes(title_text="<b>Subjectivity</b>", secondary_y=True)
    fig.update_layout(legend=dict(
    orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=0.9
    ))
    st.write(fig)
    st.write("<ol><li><i>Above graph shows how <b>subjectivity</b> (objective [0–1] subjective) and <b>polarity</b> (negative [-1 — +1] positive) of <b>COVID-19</b> related tweets change over time. The dash lines represent the simple <b>linear regression</b> for average subjectivity and average polarity.<br></i></li><hr></hr><li><i>According to the chart above, with the development of <b>COVID-19</b>, the related tweets’ expression maintained a subjectivity of <b>0.35</b> on average, and people’s feelings became more negative <b>(from about 0.09 to about 0.07)</b> on average.To analyse further we went deep into what actual emotions the tweets reflected.</i></li></ol>",unsafe_allow_html=True)
    st.markdown("<hr></hr>",unsafe_allow_html=True)
    st.subheader('Equation of Polarity')
    st.write(coef[0],'*Date +',reg.intercept_,unsafe_allow_html=True)
    st.subheader('Equation of Subjectivity')
    st.write(coef1[0],'*Date +',reg1.intercept_)
    st.markdown("<hr></hr>",unsafe_allow_html=True)
    st.markdown("Kindly use the side bar to navigate and view the features as per your desire -->")
#####################################################
else:
    st.header("Conclusion")
    st.write('<br></br>',unsafe_allow_html=True)
    st.write(" With all this information we can say that the country is now reacting positively towards the challenge presented to the nation as compared to the past few months.This positivity shows the resilience of the citizens of India in such tough times , where we give a new saying to the world.")
    st.write('<br></br>',unsafe_allow_html=True)
    st.write('<b><i>UNITED WE FALL<br>DIVIDED WE STAND</i></b>',unsafe_allow_html=True)
    

    

