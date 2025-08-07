# with open("markdown\class3.md", "r", encoding="utf-8") as f1:
#     print(f1.read())


import streamlit as st

st.title("點餐機")
food = st.text_input("請點餐")


st.title("購物籃")
st.write(food)
st.button("刪除", key="delete_food")
st.clear_input("請輸入要刪除的商品")
st.button("清空購物籃", key="clear_basket")
st.clear_all()
st.button("結帳", key="checkout")
st.write("感謝您的購買！")


st.title("計算機")
num1 = st.number_input("請輸入第一個數字", step=1, min_value=0)
num2 = st.number_input("請輸入第二個數字", step=1, min_value=0)
operation = st.selectbox("請選擇運算", options=["加法", "減法", "乘法", "除法"])
if operation == "加法":
    result = num1 + num2
elif operation == "減法":
    result = num1 - num2
elif operation == "乘法":
    result = num1 * num2
elif operation == "除法":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "除數不能為零"
st.write(f"結果是: {result}")
