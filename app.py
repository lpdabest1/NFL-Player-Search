
import streamlit as st
import Passing_Stats_Modern_Era
import Passing_Stats_Passer_Rating_Era
import Passing_Stats_Passer_Rating_Era_Players

# Page Configuration
st.set_page_config(
    page_title="NFL Position Performance Metrics",
    layout="centered",
    initial_sidebar_state="expanded",
)


st.title('Pro Football Performance Metric')
st.sidebar.title('Pro Football Statistics')


Pages = {"Passing Stats (Modern Era)": Passing_Stats_Modern_Era
        }
selection = st.sidebar.selectbox("Select One Of The Following Individual Categories",list(Pages.keys()))
page = Pages[selection]

if page:
    page.app()










