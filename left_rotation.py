# https://www.hackerrank.com/challenges/array-left-rotation
n, d = map(int, input().strip().split())
arr = list(map(int, input().strip().split()))

for i in range(d):
    spliced_integer = arr.pop(0)
    arr.append(spliced_integer)

print(" ".join(str(x) for x in arr))
