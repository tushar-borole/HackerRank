# Enter your code here. Read input from STDIN. Print output to STDOUT
T=input()
for i in range(T):
    a,b = raw_input().strip().split(" ")
    try:
        print int(a)/int(b)
    except ZeroDivisionError as e:
        print "Error Code:",e
    except  ValueError as e:
        print "Error Code:",e
