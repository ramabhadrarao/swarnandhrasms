import streamlit as st
import pandas as pd
import requests
from PIL import Image
#st.title("Swarnandhra Whatsapp Message Sender")
st.set_page_config(page_title="Swarnandhra", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

image = Image.open('logo.png')

st.image(image, caption='SWARNANDHRA Whatsapp Messages Sending Application')
uploaded_file = st.file_uploader("Choose a CSV file")
if uploaded_file:
     data=pd.read_csv(uploaded_file)
     st.dataframe(data)
     if not data.empty:     
          for index,x in data.iterrows():
               str1="http://bulkwhatsapp.live/wapp/api/send?apikey=952ab4e4144d4dd7b729f7251e89c855&mobile="
               str2=str(x[5])
               str3="&msg=""\"Dear Parent, Your son or daughter"
               str5=str(x[0])
               str6="college fees due amount is"
               str7=str(x[3])
               str8="<br>for the Final year  please clear the due amount on or before 30-4-2022. %0a Principal , SWARNANDHRA COLLEGE OF ENGINEERING AND TECHNOLOGY.Thank you\""
               result=str1+str2+str3+str5+str6+str7+str8
               #print(result)
               res = requests.get(result)
               response=res.json()
               #st.write(response["status"])
               if(response["status"] == "success"): 
                    st.success("Sms Sent Successfully"+str2+"-"+str5+"-"+str7)
               else:
                    st.warning("Sms Not Sent "+str2+"-"+str5+"-"+str7)
st.write("Developed by Rama Bhadra Rao Maddu & Dr Bomma Rama Krishna")