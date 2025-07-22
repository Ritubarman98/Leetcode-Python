target=int(input())
arr=list(map(int, input(). split(" ")))
dict={}
for i in range(len(arr)):
        num=arr[i]
        x= target-arr[i]
        if x in dict:
            print(dict[x], i)
        dict[num] = i