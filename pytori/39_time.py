import time
from datetime import datetime

current_time = time.time()  # Unix時間（秒）
print(f"現在のUnix時間: {current_time}")
print(f"読みやすい形式: {time.ctime(current_time)}")
print()
