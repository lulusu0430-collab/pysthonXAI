##🧠 一、什麼是比較運算子？
比較運算子是在比大小或比相不相同，結果會是 True（對的）或 False（錯的）。

比較方式 寫法 說明 範例結果
相等嗎？ == 左邊跟右邊一樣嗎？ 1 == 1 → True
不相等？ != 左邊跟右邊不一樣嗎？ 1 != 1 → False
大於嗎？ > 左邊比右邊大？ 2 > 1 → True
小於嗎？ < 左邊比右邊小？ 2 < 1 → False
大於或等於？ >= 左邊大或一樣？ 1 >= 1 → True
小於或等於？ <= 左邊小或一樣？ 1 <= 1 → True

##🔁 二、邏輯運算子是什麼？
邏輯運算子是用來做「對或錯」的計算，有點像我們生活中在判斷事情一樣。

##✅ and（而且）
兩個條件都要對（True），結果才是對。

左邊 右邊 結果
True True True ✅
True False False ❌
False True False ❌
False False False ❌

##✅ or（或者）
只要有一個條件是對的，結果就是對。

左邊 右邊 結果
True True True ✅
True False True ✅
False True True ✅
False False False ❌

✅ not（不是）
這是「顛倒」的意思，not True 會變成 False，not False 會變成 True。

##📚 三、誰先算？（優先順序）
當你寫很多運算的時候，Python 會照順序來決定誰先算：

()：括號最先算，像數學一樣

**：次方（像 2**3 = 8）

- / // %：乘法、除法、整除、餘數

* -：加法、減法

== != > < >= <=：比較

not：邏輯「不是」

and：邏輯「而且」

or：邏輯「或者」

🧪 小小測驗（可以試著自己回答喔）：
python
Copy
Edit
print(3 > 2 and 5 < 10) # True 還是 False？
print(not (2 == 2)) # True 還是 False？
print(1 + 2 \* 3) # 是多少？（先算乘法喔）
