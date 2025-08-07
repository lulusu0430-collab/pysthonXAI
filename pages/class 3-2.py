import streamlit as st

st.title("點餐機")

if "cart" not in st.session_state:
    st.session_state.cart = []

product = st.text_input("請輸入要購買的物品：")

if st.button("加入購物車"):
    if product:
        st.session_state.cart.append(product)
    else:
        st.warning("請輸入商品名稱再加入！")

st.write("---")

st.subheader(" 購物車")
if st.session_state.cart:
    for i, item in enumerate(st.session_state.cart):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.write(f"• {item}")
        with col2:
            if st.button(" 刪除", key=f"delete_{i}"):
                st.session_state.cart.pop(i)
                st.rerun()
else:
    st.info("購物車目前是空的。")

st.write("---")

col1, col2 = st.columns(2)

with col1:
    if st.button("確認購買"):
        if st.session_state.cart:
            st.success(f"感謝購買：{'、'.join(st.session_state.cart)}！")
            st.session_state.cart = []
        else:
            st.warning("購物車是空的！")

with col2:
    if st.button(" 清空購物車"):
        st.session_state.cart = []
        st.info("已清空購物車")
