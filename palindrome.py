N,data=raw_input(),raw_input().split()
print any([ val==val[::-1] for val in data]) and all([ val>0 for val in map(int,data)])
