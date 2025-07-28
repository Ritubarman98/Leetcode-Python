nums=list(map(int, input().split()))
k=int(input())
n = len(nums)
k = k % n
nums[:] = nums[-k:] + nums[:-k]
print(nums)