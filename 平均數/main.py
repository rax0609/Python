# Prompt the user to enter three numbers
num1 = float(input("請輸入一個數值-No1: "))
num2 = float(input("請輸入一個數值-No2: "))
num3 = float(input("請輸入一個數值-No3: "))

# Divide the numbers into groups of two and store the averages and their corresponding number pairs in a dictionary
averages = {
    (num1, num2): (num1 + num2) / 2,
    (num2, num3): (num2 + num3) / 2,
    (num1, num3): (num1 + num3) / 2
}

# Find the maximum average and its corresponding number pair
max_average = max(averages, key=averages.get)

# Print the maximum average and its corresponding number pair
print("Maximum average:", averages[max_average], "for the numbers:", max_average)
print(f"您輸入的三個數字為: {num1}, {num2}, {num3},依結果 { max_average } 的組合取得的平均分數最高")