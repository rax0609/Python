import random

def guess_number():
    target_number = random.randint(1, 100)
    attempts = 0
    low = 1
    high = 100

    while True:
        if low == high:
            print(f"由於您的猜測範圍僅剩答案 {target_number} 了，所以您失敗了。")
            break
        guess = int(input(f"猜一個介於 {low} 和 {high} 之間的數字："))
        attempts += 1
        print(f"{target_number}")
        if guess < low or guess > high:
            print(f"請輸入介於 {low} 和 {high} 之間的數字。")
        elif guess < target_number:
            print("這數字太低了！")
            low = guess + 1
        elif guess > target_number:
            print("這數字太高了！")
            high = guess - 1
        else:
            print(f"恭喜！ 您在 {attempts} 次嘗試中猜中了數字。")
            break

guess_number()