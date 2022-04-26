import streamlit as st
import pandas as pd
import requests
from PIL import Image
#st.title("Swarnandhra Whatsapp Message Sender")

##########################################################
# .streamlit/secrets.toml
def check_password():
    """Returns `True` if the user had a correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if (
            st.session_state["username"] in st.secrets["passwords"]
            and st.session_state["password"]
            == st.secrets["passwords"][st.session_state["username"]]
        ):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # don't store username + password
            del st.session_state["username"]
        else:
            st.session_state["password_correct"] = False

    if "password_correct" not in st.session_state:
        # First run, show inputs for username + password.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        return False
    elif not st.session_state["password_correct"]:
        # Password not correct, show input + error.
        st.text_input("Username", on_change=password_entered, key="username")
        st.text_input(
            "Password", type="password", on_change=password_entered, key="password"
        )
        st.error("😕 User not known or password incorrect")
        return False
    else:
        # Password correct.
        return True




#########################################################











st.set_page_config(page_title="Swarnandhra", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

if check_password():
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