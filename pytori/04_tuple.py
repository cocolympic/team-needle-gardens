#ランダムに曜日と月と数字を選ぶ
import random

tuple_days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
tuple_months = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", 
                "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
tuple_pi = (3.14, 1.59, 2.65, 3.58)

print(random.choice(tuple_days))    
print(random.choice(tuple_months))  
print(random.choice(tuple_pi))      