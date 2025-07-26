digits = list(map(int, input().split()))
new_digits=[]
string=''
for i in digits:
    string= string+str(i)
x=int(string)+1
print(x)
for i in (str(x)):
    new_digits.append(int(i))
print(new_digits)