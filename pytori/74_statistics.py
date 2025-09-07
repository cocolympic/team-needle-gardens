import statistics

# データの例
data = [10, 20, 30, 40, 50, 60, 70]

# 平均
mean_value = statistics.mean(data)

# 中央値
median_value = statistics.median(data)

# 最頻値
mode_value = statistics.mode(data)

# 分散
variance_value = statistics.variance(data)

# 標準偏差
stdev_value = statistics.stdev(data)

# 結果を表示
print("データ:", data)
print("平均:", mean_value)
print("中央値:", median_value)
print("最頻値:", mode_value)
print("分散:", variance_value)
print("標準偏差:", stdev_value)
