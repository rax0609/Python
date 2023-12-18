# 讓使用者輸入綜合所得淨額,存在變數 num1 中
num1 = input("income ? ")
num1 = int(num1)


# 依據綜合所得淨額,計算應繳稅額,存在變數 num2 中
# 應繳稅額 = 綜合所得淨額 * 稅率 - 速算扣除數
# if else 的用法,可以參考 https://www.w3schools.com/python/python_conditions.asp
if num1 <= 560000:
    num2 = (num1 * 0.05) - 1000
elif num1 <= 1260000:
    num2 = (num1 * 0.12) - 2000
elif num1 <= 2520000:
    num2 = (num1 * 0.2) - 3000
elif num1 <= 4720000:
    num2 = (num1 * 0.3) - 4000
elif num1 >= 4720001:
    num2 = (num1 * 0.4) - 5000
# 輸出綜合所得淨額和應繳稅額
print(f"Income(綜合所得淨額)={num1}, tax(應繳稅額)={num2}")