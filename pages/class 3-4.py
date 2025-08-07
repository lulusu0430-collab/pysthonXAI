import streamlit as st
import random

i = random.randint(0, 100)

a = st.number_input("請輸入你的數字:", step=1, min_value=0, max_value=100)

if i < a:
    st.write("再小一點")
elif i > a:
    st.write("再大一點")
elif i == a:
    st.write("恭喜答對")
