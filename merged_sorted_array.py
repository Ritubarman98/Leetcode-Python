nums1=list(map(int, input().split()))
m=int(input())
nums2=list(map(int, input().split()))
n=int(input())
##nums1[:m] = nums1[:m]  
##nums1[m:] = nums2  
nums3=nums1[:m]+ nums2[:n]    
nums3.sort()
print(nums3)