import streamlit as st
import requests
import pandas as pd

'''
# RookieModel front
'''

url = 'https://rookiesimage-t33c7owjcq-ew.a.run.app/predict'

params={}

params["games_played"]=st.text_input("Number of games played", value="71")
params["minutes_played"]=st.text_input("Average minutes played per game", value="10.1")
params["field_goals_attempted"]=st.text_input("Average of field goals attempted per game", value="3.2")
params["field_goals_percentage"]=st.text_input("Percentage of field goals made per game", value="39.6")
params["three_pointers_attempted"]=st.text_input("Average of three pointers attempted per game", value="0.5")
params["three_pointers_percentage"]=st.text_input("Percentage of three pointers made per game", value="21.9")
params["free_throws_attempted"]=st.text_input("Average of free throws attempted per game", value="0.7")
params["free_throws_percentage"]=st.text_input("Percentage of free throws made per game", value="83.7")
params["offensive_rebounds"]=st.text_input("Average of offensive rebounds per game", value="0.1")
params["defensive_rebounds"]=st.text_input("Average of defensive rebounds per game", value="0.9")
params["assists"]=st.text_input("Average of assists per game", value="1.7")
params["steals"]=st.text_input("Average of steals per game", value="0.5")
params["blocks"]=st.text_input("Average of blocks per game", value="0.1")
params["turnovers"]=st.text_input("Average of turnovers per game", value="0.7")

if st.button("Click me"):

    response=requests.get(url,params=params)
    st.markdown(f"status_code: {response.status_code}")
    if response.status_code==200:
        if response.json():
            if response.json()["five_years_rookie"]==0:
                st.subheader("⛹️‍♂️❌ You should not invest in this rookie.")
            else:
                st.subheader("⛹️‍♂️✅ You should invest in this rookie.")
