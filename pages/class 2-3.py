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
