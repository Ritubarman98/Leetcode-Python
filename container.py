n = int(input())
height = list(map(int, input().split()))
max_water = 0

for i in range(n):
    for j in range(i + 1, n):
        width = j - i
        container_height = min(height[i], height[j])
        area = width * container_height
        max_water = max(max_water, area)

print(max_water)