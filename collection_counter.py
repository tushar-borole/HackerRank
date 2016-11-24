# Enter your code here. Read input from STDIN. Print output to STDOUT
X=input()
shoe_size=map(int,raw_input().strip().split(" "))
number_customer=input()
money_earned=0
for data in range(number_customer):
    size,price=map(int,raw_input().strip().split(" "))
    if(size in shoe_size):
        money_earned=price + money_earned
        shoe_size.remove(size)
        
print money_earned
