nums=list(map(int, input().split()))
n = len(nums)        
        
left = [1] * n
for i in range(1, n):
    left[i] = left[i - 1] * nums[i - 1]        

right = [1] * n
for i in range(n - 2, -1, -1):
    right[i] = right[i + 1] * nums[i + 1]        

result = [0] * n
for i in range(n):
    result[i] = left[i] * right[i]

print(result)