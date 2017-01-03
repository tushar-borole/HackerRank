import numpy

N,M=map(int,raw_input().strip().split(" "))
array_list=[]
for i in range(N):
    array_list.append(map(int,raw_input().strip().split(" ")))

my_array = numpy.array(array_list)
sum_of_array = numpy.sum(my_array, axis = 0) 
print numpy.prod(sum_of_array)     
