# Enter your code here. Read input from STDIN. Print output to STDOUT

N=raw_input()
A=raw_input().strip().split(" ")
print sorted(set(A))[-2]
    
