import streamlit as st  # 匯入streamlit模組並重新命名為st

st.title("複製")  # 設定網頁標題為 "Class 2-2"
# st.number_input() 函數用來創建一個數字,設定step=1可以讓使用者只能輸入整數
# min_value=0設定最小值為0，max_value=None則表示沒有最大值限制
number = st.number_input("請輸入一個數字", step=1, min_value=0)
# st.markdown() 可以在網頁使用markdown語法顯示文字
st.write(f"你輸入的數字是: {number}")


st.title("考試分數等級")
score = st.number_input("請輸入考試分數", step=1, min_value=0, max_value=100)
if score >= 90:
    st.write("你獲得了 A 級成績！")
elif 80 <= score < 90:
    st.write("你獲得了 B 級成績！")
elif 70 <= score < 80:
    st.write("你獲得了 C 級成績！")
elif 60 <= score < 70:
    st.write("你獲得了 D 級成績！")
else:
    st.write("你獲得了 F 級成績！")

st.title("密碼驗證")
password = st.number_input("請輸入密碼：", step=1, min_value=0, max_value=999)
if password == "543":
    st.write("密碼正確，歡迎狗！")
elif password == "430":
    st.write("密碼正確，歡迎進入！")
elif password == "123":
    st.write("密碼正確，歡迎貓！")
elif password == "456":
    st.write("密碼正確，歡迎兔子！")
else:
    st.write("密碼錯誤，請再試一次！")
