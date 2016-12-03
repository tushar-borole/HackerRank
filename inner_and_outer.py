import numpy
A=numpy.array(map(int,raw_input().strip().split(" ")))
B=numpy.array(map(int,raw_input().strip().split(" ")))
print numpy.inner(A, B) 
print numpy.outer(A, B) 
