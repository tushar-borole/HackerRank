import numpy
N=input()
list_data=[]
for _ in range(N*2):
    list_data.append(map(int,raw_input().strip().split(" ")))

A=numpy.array(list_data[:N])
B=numpy.array(list_data[N:])
print numpy.dot(A,B)
