#https://www.hackerrank.com/challenges/sparse-arrays?h_r=next-challenge&h_v=zen

n = int(input())
arr = []
dictionary = {}
for i in range(n):
    arr.append(input())


y = int(input())
arr1=[]
for i in range(y):
    value = input()
    arr1.append(value)
    if value not in arr:
        dictionary[value]=1
    else:
        dictionary[value] = dictionary[value] + 1


for item in dictionary:
    print(item)


