import streamlit as st
import os

folderPath = "markdown"  # 設定資料夾路徑
files = os.listdir(folderPath)  # 列出資料夾中的所有檔案
# 這時候資料夾可能包含其他檔案,我們只需 .md 檔案
files_name = []  # 新增清單用來存放 .md 檔案
for f in files:  # 逐一檢查所有檔案, 看看是否以 .md 結尾
    if f.endswith(".md"):  # 如果檔案名稱以 .md 結尾
        # if ".md" in f: #如果檔案名稱包含 .md
        files_name.append(f)  # 將符合條件的檔案名稱加入清單
files_name.sort()  # 將清單排序, 預設是由小到大

for f in files_name:  # ['class1.md', 'class2.md']逐一讀取所有 .md 檔案
    # 用with open()讀取檔案內容並存到file扁屬裡面, 謀是為r, 檔案編碼為utf-8
    # 這樣可以讀用擔心檔案讀取後忘記關閉的問題
    # open參數格是為(檔案路, 檔案模式, 檔案編碼)
    # markdown\class1.md
    with open(f"{folderPath}/{f}", "r", encoding="utf-8") as file:
        content = file.read()
        # 開啟檔案後可以做很多事情, 這裡我們只讀取檔案內容
    with st.expander(f[:-3]):  # 使用expander, 標題為檔案名稱去掉.md
        st.markdown(content)  # 將檔案內容顯示在網頁上
