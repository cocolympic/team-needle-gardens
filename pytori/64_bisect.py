import bisect 
nums = [1, 3, 4, 7] 

pos = bisect.bisect(nums, 5) 
print(pos) 

bisect.insort(nums, 5) 
print(nums)