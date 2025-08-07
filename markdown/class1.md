##👋 二、顯示文字
python
Copy
Edit
print("Hello, World!")
▶ print() 是顯示東西在畫面上（終端機）用的。

##🔢 三、基本資料型態（電腦認得的資料類型）
資料 說明 種類
1 整數 int
1.0 小數 float
"1" 或 'hello' 文字（字串） str
True / False 是/否、對/錯 bool

##📦 四、變數（像是小箱子裝東西）
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
print(1 + 1) # 加
print(1 - 1) # 減
print(2 \* 2) # 乘
print(4 / 2) # 除
print(5 // 2) # 取商（只看整數部分）
print(5 % 2) # 取餘數（剩下的）
print(2\*\*3) # 次方（2 的 3 次方=8）

🥇 六、運算優先順序（誰先算？）
() 括號最優先

\*\* 次方

- / // %（乘除）

* -（加減）

🔤 七、字串的運算
python
Copy
Edit
print("apple" + " pen") # 合併變 "apple pen"
print("apple " \* 3) # 重複三次
python
Copy
Edit
print(len("apple")) # 看長度，這裡是 5 個字

🧐 八、看資料是什麼型態（type）
python
Copy
Edit
print(type(1)) # <class 'int'>
print(type("apple")) # <class 'str'>
print(type(True)) # <class 'bool'>

🔄 九、型態轉換（變形術！）
想變成 用這個
變整數 int()
變小數 float()
變字串 str()
變布林 bool()

python
Copy
Edit
print(int(1.2)) # 小數變整數
print(float("1.23")) # 字串變小數
print(str(100)) # 數字變字串
print(bool(0)) # 0 會變 False
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
print("圓的面積為:", 3.14 \* a\*\*2)
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
