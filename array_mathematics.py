import numpy

N,M=map(int,raw_input().strip().split(" "));
A=[]
B=[]
a=[]
b=[]

for i in range(N):
    a.append(raw_input().strip().split(" "));
for i in range(N):
    b.append(raw_input().strip().split(" "));

A = numpy.array(a, int)
B = numpy.array(b, int)

print A + B
print A - B
print A * B
print A / B
print A % B
print A ** B
