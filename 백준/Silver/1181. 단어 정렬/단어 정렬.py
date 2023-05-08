

n = int(input())
arr = []

for i in range(n):
    arr.append(input())

#중복 제거 위해
arr = list(set(arr))
arr.sort()
arr.sort(key=len)

for x in arr:
    print(x)