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

st.title("計算圓的面積")
radius = st.number_input("請輸入圓的半徑", step=0.1, min_value=0.0)
if radius > 0:
    area = 3.14 * radius**2
    st.write(f"圓的面積為: {area:.2f}")  # 使用:.2f格式化輸出保留兩位小數

st.title("計算矩形的面積")
length = st.number_input("請輸入矩形的長度", step=0.1, min_value=0.0)
width = st.number_input("請輸入矩形的寬度", step=0.1, min_value=0.0)
if length > 0 and width > 0:
    area = length * width
    st.write(f"矩形的面積為: {area:.2f}")  # 使用:.2f格式化輸出保留兩位小數


st.markdown("### 按鈕練習")
# st.button(可以在網頁顯示一ˊ個按鈕，當使用者點擊按鈕
# key是按鈕的識別名稱,可用來分別不同的按鈕
# 如果使用者點擊按鈕,st.button()會返回True,否則返回False
st.button("點我", key="button1")
if st.button("點我", key="balloons"):
    st.balloons()  # 點擊按鈕時會顯示氣球動畫
    st.balloons()
    st.balloons()
    st.balloons()
    st.balloons()
if st.button("點我", key="snow"):
    st.snow()  # 點擊按鈕時會顯示雪花動畫
st.markdown("### 單選按鈕練習")
# st.radio() 可以在網頁顯示一ˊ個單選按鈕組
# options是選項列表, index=0表示預設選中第一個選項
option = st.radio("請選擇一個選項", options=["選項1", "選項2", "選項3"], index=0)
st.write(f"你選擇的選項是: {option}")  #
# st.selectbox() 可以在網頁顯示一ˊ個下拉選單
# options是選項列表, index=0表示預設選中第一個選項
option = st.selectbox("請選擇一個選項", options=["選項A", "選項B", "選項C"], index=0)
st.write(f"你選擇的選項是: {option}")  #


st.title("數字金字塔")
number = st.number_input("請輸入金字塔的高度", min_value=1, value=5, step=1)
for i in range(1, number + 1):
    spaces = " " * (number - i)  # 計算前置空格
    numbers = " ".join(str(j) for j in range(1, i + 1))  # 生成數字序列
    st.write(f"{spaces}{numbers}")  # 顯示金字塔的一層

st.title("密碼門檢查")
password = st.text_input(
    "請輸入密碼：", type="password"
)  # 使用type="password"隱藏輸入的密碼
if password == "5457":
    st.write("密碼正確，歡迎Katie！")
elif password == "430":
    st.write("密碼正確，歡迎Lulu！")
else:
    st.write("密碼錯誤，請再試一次！")
