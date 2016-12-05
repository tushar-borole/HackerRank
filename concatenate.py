import numpy
N,M,P=map(int,raw_input().strip().split(" "))
array_N=[]
for _ in range(N+M):
    array_N.append(map(int,raw_input().strip().split(" ")))
    
print numpy.reshape(numpy.concatenate(array_N),(N+M,P)) 
