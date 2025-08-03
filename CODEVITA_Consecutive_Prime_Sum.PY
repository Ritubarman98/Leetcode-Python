n=int(input())
is_prime= [True]*(n+1)
is_prime[0]=False
is_prime[1]= False

for i in range(2, int(n**0.5)+1):
    if is_prime[i]:
        for j in range(i*i, n+1, i):
            is_prime[j]= False

primes=[]
for i in range(2, n+1):
    if is_prime[i]:
        primes.append(i)
        
primesum=0
count=0

for i in primes:
    primesum +=i
    
    if primesum>n:
        break
    if primesum == 2:
        continue
    if is_prime[primesum]:
        count +=1
print(count)