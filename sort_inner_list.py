# Enter your code here. Read input from STDIN. Print output to STDOUT
N,M=map(int,raw_input().strip().split(" "))
list_data=[]
for i in range(N):
    list_data.append(map(int,raw_input().strip().split(" ")))
K=input()
sorted_list=sorted(list_data, key=lambda x: x[K])
for data in sorted_list:
    print " ".join(map(str,data))
