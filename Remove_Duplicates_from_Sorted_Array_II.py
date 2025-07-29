nums=list(map(int, input().split()))
write = 0

for i in nums:
    if write < 2 or i != nums[write - 2]:
        nums[write] = i
        write += 1
print(nums[:write])
print (write)