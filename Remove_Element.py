nums=list(map(int, input().split()))
val=int(input())
nums1=[]
for i in nums:
    if i!=val:
        nums1.append(i)            
for i in range(len(nums1)):
        nums[i] = nums1[i]
for i in range(len(nums1), len(nums)):
    nums[i] = "_"
        
print(len(nums1), ",", nums)
