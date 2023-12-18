# 使用者輸入風險係數
while True:
    risk_factors = list(map(int, input("請輸入團隊的風險係數，以空格分隔：").split()))
    if all(0 <= risk <= 10 for risk in risk_factors):
        break
    else:
        print("所有風險係數必須在 0 到 10 之間，請重新輸入。")

# 計算風險最大值、最小值和平均值
max_risk = max(risk_factors)
min_risk = min(risk_factors)
avg_risk = round(sum(risk_factors) / len(risk_factors), 2)

# 判斷風險等級
risk_level = "LOW"
if any(risk > 8 for risk in risk_factors) or sum(risk >= 7 for risk in risk_factors) >= 2:
    risk_level = "HIGH"
elif any(risk > 6 for risk in risk_factors) or sum(risk >= 5 for risk in risk_factors) >= 2:
    risk_level = "MEDIUM"

# 輸出結果
print(f"風險最大值：{max_risk}")
print(f"風險最小值：{min_risk}")
print(f"風險平均值：{avg_risk}")
print(f"風險等級：{risk_level}")