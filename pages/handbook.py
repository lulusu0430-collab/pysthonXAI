import streamlit as st

with st.expander("CLASS 1"):
    st.write(
        """
👋 二、顯示文字
python
Copy
Edit
print("Hello, World!")
▶ print() 是顯示東西在畫面上（終端機）用的。

🔢 三、基本資料型態（電腦認得的資料類型）
資料	說明	種類
1	整數	int
1.0	小數	float
"1" 或 'hello'	文字（字串）	str
True / False	是/否、對/錯	bool

📦 四、變數（像是小箱子裝東西）
python
Copy
Edit
a = 1
print(a)
a = "apple"
print(a)
▶ a = 1 是把「1」裝進叫做 a 的箱子裡
▶ a = "apple" 是把 a 裡的東西改成 "apple"

➕ 五、運算（加減乘除）
python
Copy
Edit
print(1 + 1)  # 加
print(1 - 1)  # 減
print(2 * 2)  # 乘
print(4 / 2)  # 除
print(5 // 2)  # 取商（只看整數部分）
print(5 % 2)  # 取餘數（剩下的）
print(2**3)  # 次方（2的3次方=8）

🥇 六、運算優先順序（誰先算？）
() 括號最優先

** 次方

* / // %（乘除）

+ -（加減）

🔤 七、字串的運算
python
Copy
Edit
print("apple" + " pen")  # 合併變 "apple pen"
print("apple " * 3)  # 重複三次
python
Copy
Edit
print(len("apple"))  # 看長度，這裡是5個字

🧐 八、看資料是什麼型態（type）
python
Copy
Edit
print(type(1))  # <class 'int'>
print(type("apple"))  # <class 'str'>
print(type(True))  # <class 'bool'>

🔄 九、型態轉換（變形術！）
想變成	用這個
變整數	int()
變小數	float()
變字串	str()
變布林	bool()

python
Copy
Edit
print(int(1.2))  # 小數變整數
print(float("1.23"))  # 字串變小數
print(str(100))  # 數字變字串
print(bool(0))  # 0會變False
🚫 小心：不能把 "hello" 變成數字，會出錯！

⌨️ 十、使用者輸入（請人輸入資料）
python
Copy
Edit
a = input("請輸入一些文字:")
print(a)
▶ input() 是請使用者輸入
▶ 注意！輸入的東西一律是字串

所以想加數字時，要記得轉換：

python
Copy
Edit
print(int(a) + 10)

🧮 十一、小小計算練習
python
Copy
Edit
a = float(input("請輸入圓的半徑:"))
print("圓的面積為:", 3.14 * a**2)
python
Copy
Edit
a = float(input("請輸入國文其中成績:"))
b = float(input("請輸入數學其中成績:"))
print("總分為:", a + b)
print("平均為:", (a + b) / 2)
❗ 最後的小提醒
python
Copy
Edit
name = float(input("請輸入你的名字:"))
這邊有點怪怪的，名字應該是文字（str），不要轉成 float：
✅ 正確應該是：

python
Copy
Edit
name = input("請輸入你的名字:")
age = float(input("請輸入你的年齡:"))
print("你好，我是", name, "我今年", age, "歲")

"""
    )
with st.expander("CLASS 2"):
    st.write(
        """
🧠 一、什麼是比較運算子？
比較運算子是在比大小或比相不相同，結果會是 True（對的）或 False（錯的）。

比較方式	寫法	說明	範例結果
相等嗎？	==	左邊跟右邊一樣嗎？	1 == 1 → True
不相等？	!=	左邊跟右邊不一樣嗎？	1 != 1 → False
大於嗎？	>	左邊比右邊大？	2 > 1 → True
小於嗎？	<	左邊比右邊小？	2 < 1 → False
大於或等於？	>=	左邊大或一樣？	1 >= 1 → True
小於或等於？	<=	左邊小或一樣？	1 <= 1 → True

🔁 二、邏輯運算子是什麼？
邏輯運算子是用來做「對或錯」的計算，有點像我們生活中在判斷事情一樣。

✅ and（而且）
兩個條件都要對（True），結果才是對。

左邊	右邊	結果
True	True	True ✅
True	False	False ❌
False	True	False ❌
False	False	False ❌

✅ or（或者）
只要有一個條件是對的，結果就是對。

左邊	右邊	結果
True	True	True ✅
True	False	True ✅
False	True	True ✅
False	False	False ❌

✅ not（不是）
這是「顛倒」的意思，not True 會變成 False，not False 會變成 True。

📚 三、誰先算？（優先順序）
當你寫很多運算的時候，Python 會照順序來決定誰先算：

()：括號最先算，像數學一樣

**：次方（像 2**3 = 8）

* / // %：乘法、除法、整除、餘數

+ -：加法、減法

== != > < >= <=：比較

not：邏輯「不是」

and：邏輯「而且」

or：邏輯「或者」

🧪 小小測驗（可以試著自己回答喔）：
python
Copy
Edit
print(3 > 2 and 5 < 10)  # True 還是 False？
print(not (2 == 2))      # True 還是 False？
print(1 + 2 * 3)         # 是多少？（先算乘法喔）
"""
    )
