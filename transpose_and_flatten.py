import numpy
N,M=map(int,raw_input().strip().split(" "))
list_data=[]
for i in range(N):
    list_data.append(map(int, raw_input().strip().split(" ")))
print numpy.transpose(list_data)
print numpy.array(list_data).flatten()
