# 使用兩個 for 迴圈來生成 99 乘法表
# 讓使用者輸入兩個數字,分別存在變數 num1 和 num2 中
num1 = input("請輸入乘數: ")
num2 = input("請輸入被乘數: ")
num1 = int(num1)
num2 = int(num2)
# ljust() 方法返回一個原字符串左對齊,並使用空格填充至指定長度的新字符串
# end="  " 代表每次印出來的東西都會以兩個空格結尾
# print 輸出文字,會自動換行,如果不想要換行,可以在 print 後面加上 end=""
for i in range(1, num1+1):
    print(f"\n")
    for j in range(1, num2+1):
        print(f"{j} * {i} = {i*j}".ljust(10) ,end="  ")