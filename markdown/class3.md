好的！我幫你把今天上課學到的 Python 指令內容，用**小學六年級可以懂的方式**整理出來，讓你更容易複習～

---

## 🔶 1. Streamlit 是什麼？

Streamlit 是一個可以讓你用 Python 做出漂亮網頁的工具，就像做小程式一樣簡單！

```python
import streamlit as st
```

這行是「叫出」Streamlit 這個工具箱，我們幫它取個簡稱叫 `st`，之後用 `st` 來操作就好！

---

## 🟦 2. 顯示標題

```python
st.title("我是標題")
```

這行會在網頁最上面顯示一個大大的標題。

---

## 🔢 3. 輸入數字

```python
st.number_input("請輸入一個數字", step=1, min_value=0)
```

這會在網頁上放一個輸入框，可以讓使用者輸入數字。

- `step=1`：每次加或減都跳一格
- `min_value=0`：最小只能輸入 0

---

## ✏️ 4. 顯示文字

```python
st.write("我想顯示的文字")
```

用來顯示文字，也可以加上一些變數，像這樣：

```python
st.write(f"你輸入的數字是: {number}")
```

---

## 🧮 5. 列表（像裝東西的箱子）

```python
a = [90, 50, 20, 80, 70]
print(a[1])  # 印出第2個數字（從0開始算）
```

```python
name = ["合合", "小明", "小美", "幕幕", "黑黑"]
print(name[2:5])  # 印出第3~5個名字（不包含第5個）
```

---

## 🔁 6. for 迴圈（重複做事情）

```python
for i in range(5):
    print(i)
```

這會把 0 到 4 都印出來（總共 5 個數字）

可以設定起點、終點和每次跳幾格：

```python
for i in range(1, 10, 2):
    print(i)  # 印出 1, 3, 5, 7, 9
```

---

## 🎓 7. 考試成績判斷

輸入一個分數，告訴你是什麼等級：

```python
if score >= 90:
    st.write("你獲得了 A 級成績！")
elif 80 <= score < 90:
    st.write("你獲得了 B 級成績！")
...
```

---

## 🟡 8. 計算面積

### 圓形面積公式：

```python
area = 3.14 * 半徑 ** 2
```

### 矩形面積公式：

```python
area = 長度 * 寬度
```

使用 `st.number_input()` 來讓使用者輸入數字，再算出面積～

---

## 🖱️ 9. 按鈕和動畫

```python
if st.button("點我", key="balloons"):
    st.balloons()  # 點下去會出現氣球動畫
```

```python
if st.button("點我", key="snow"):
    st.snow()  # 會出現雪花動畫
```

---

## 🔘 10. 單選與下拉選單

```python
st.radio("請選擇", options=["選項1", "選項2"])
```

```python
st.selectbox("請選擇", options=["A", "B", "C"])
```

這兩個都可以讓使用者從選項中選一個！

---

## 🔺 11. 數字金字塔

你輸入一個數字，它會畫出像金字塔一樣的數字：

```text
    1
   1 2
  1 2 3
  ...
```

---

## 🔒 12. 密碼檢查

```python
password = st.text_input("請輸入密碼：", type="password")
```

輸入密碼，如果正確就會顯示對應的人名：

```python
if password == "5457":
    st.write("密碼正確，歡迎Katie！")
```

---

如果你想要我幫你做成簡單小卡片筆記版，或是畫圖輔助也可以喔！😄
你想要再複習哪一個部分呢？
