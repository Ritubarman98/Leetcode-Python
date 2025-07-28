nums= list(map(int, input().split()))
s={}
for i in (nums):
    if i in s:
        s[i] +=1
    else:
        s[i] = 1
print (max(s, key=s.get))