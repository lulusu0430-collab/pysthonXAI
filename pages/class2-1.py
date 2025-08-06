# 比較運算子
print(1 == 1)  # True
print(1 != 1)  # false
print(1 > 1)  # false
print(1 < 1)  # false
print(1 >= 1)  # true
print(1 <= 1)  # true

# ` 邏輯運算子
# and 運算子
print(True and True)  # true
print(True and False)  # false
print(False and True)  # false
print(False and False)  # false


# or 運算子
print(True or True)  # true
print(True or False)  # true
print(False or True)  # true
print(False or False)  # false

# not 運算子
print(not True)  # false
print(not False)  # true

# 優先順序
# 1. () 括號
# 2. ** 次方
# 3. * / // % 乘 除 取商 取餘數
# 4. + - 加 減
# 5.  == != > < >= <= 比較運算子
# 6. not
# 7. and
# 8. or


# 密碼門檢查
password = input("請輸入密碼：")
if password == "543":
    print("密碼正確，歡迎狗！")
elif password == "430":
    print("密碼正確，歡迎進入！")
elif password == "123":
    print("密碼正確，歡迎貓！")
elif password == "456":
    print("密碼正確，歡迎兔子！")
else:
    print("密碼錯誤，請再試一次！")
# 連續使用if跟使用if else的差別
# elif可以排除前面有判斷過的條件, 所以縮短判斷條件的副難度, 也節省了時間
# 但是如果是使用多個if來做獨立判斷, 則每個if都會被執行,所以效率較低
