import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# 讀取數據
data = pd.read_csv("running_data.csv")

# 將數據分為前半部分和後半部分
first_half_pace = data.loc[0:299, "pace"]
second_half_pace = data.loc[300:599, "pace"]

# 進行 t 檢定
t_statistic, p_value = stats.ttest_ind(first_half_pace, second_half_pace, equal_var=False)

# 繪製前半部分和後半部分平均配速的分布圖
plt.figure(figsize=(8, 6))
plt.hist(first_half_pace, color="blue", alpha=0.5, label="first_half_pace")
plt.hist(second_half_pace, color="green", alpha=0.5, label="second_half_pace")
plt.title("Average pace distribution")
plt.xlabel("Pace (min/km)")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# 印出結果
print("t 檢定結果:")
print("t 值：{:.2f}".format(t_statistic))
print("p 值：{:.4f}".format(p_value))

# 解讀結果
alpha = 0.05
if p_value < alpha:
    print("根據統計結果，在前半部分和後半部分的平均配速之間存在顯著差異。")
else:
    print("根據統計結果，在前半部分和後半部分的平均配速之間沒有顯著差異。")

# 將數據分為前半部分和後半部分
first_half_Steps = data.loc[0:299, "Steps"]
second_half_Steps = data.loc[300:599, "Steps"]

# 進行 t 檢定
t_statistic, p_value = stats.ttest_ind(first_half_Steps, second_half_Steps, equal_var=False)

# 繪製前半部分和後半部分平均步頻的分布圖
plt.figure(figsize=(8, 6))
plt.hist(first_half_Steps, color="blue", alpha=0.5, label="first_half_Steps")
plt.hist(second_half_Steps, color="green", alpha=0.5, label="second_half_Steps")
plt.title("Average Steps distribution")
plt.xlabel("Steps")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# 印出結果
print("t 檢定結果:")
print("t 值：{:.2f}".format(t_statistic))
print("p 值：{:.4f}".format(p_value))

# 解讀結果
alpha = 0.05
if p_value < alpha:
    print("根據統計結果，在前半部分和後半部分的平均步頻之間存在顯著差異。")
else:
    print("根據統計結果，在前半部分和後半部分的平均步頻之間沒有顯著差異。")

# 將數據分為前半部分和後半部分
first_half_fatigue = data.loc[0:299, "Fatigue"]
second_half_fatigue = data.loc[300:599, "Fatigue"]

# 進行 t 檢定
t_statistic, p_value = stats.ttest_ind(first_half_fatigue, second_half_fatigue, equal_var=False)

# 繪製前半部分和後半部分疲累度的直方圖
plt.figure(figsize=(8, 6))
plt.hist(first_half_fatigue, color="blue", alpha=0.5, label="first_half_fatigue")
plt.hist(second_half_fatigue, color="green", alpha=0.5, label="second_half_fatigue")
plt.title("Fatigue Distribution")
plt.xlabel("Fatigue")
plt.ylabel("Frequency")
plt.legend()
plt.show()

# 印出結果
print("t 檢定結果:")
print("t 值：{:.2f}".format(t_statistic))
print("p 值：{:.4f}".format(p_value))

# 解讀結果
alpha = 0.05
if p_value < alpha:
    print("根據統計結果，在前半部分和後半部分的疲累度之間存在顯著差異。")
else:
    print("根據統計結果，在前半部分和後半部分的疲累度之間沒有顯著差異。")

# 散點圖
plt.scatter(data['distance'], data['running efficiency'])
plt.xlabel('distance')
plt.ylabel('running efficiency')
plt.title('Correlation plot between distance and running efficiency')

# 提取卡路里消耗數據列
calorie_expenditure = data["calorie expenditure"]

# 計算總卡路里消耗
total_calories = calorie_expenditure.sum()
print("在599天不懈地跑步下，你的總卡路里消耗：{:.2f}".format(total_calories))

# 整體分析與建議
print("=============整體分析與建議=============")
if p_value < alpha:
    print("根據統計結果，你隨著時間訓練跑步配速和步頻都有顯著的進步。")
else:
    print("根據統計結果，你隨著時間訓練跑步配速和步頻沒有顯著的進步。")

if p_value < alpha:
    print("根據統計結果，你隨著時間訓練運動後疲累度有明顯降低。")
else:
    print("根據統計結果，你隨著時間訓練運動後疲累度沒有明顯降低。")

print("根據距離和跑步效率的相關性分析，你的跑步效率在長距離時是最佳的。")
print("在599天不懈地跑步下，你的總卡路里消耗：{:.2f}".format(total_calories))
if total_calories > 898500:
    print("這顯示你的運動量相當大。繼續保持良好的運動習慣！")
else:
    print("這顯示你的運動量不夠多。請加強運動量，加油！")
