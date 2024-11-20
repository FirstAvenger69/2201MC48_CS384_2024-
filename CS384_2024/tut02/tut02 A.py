n=input()
n=int(n)

while n>=10:
    sum=0
    num=n

    while num>0:
        sum=sum+num%10
        num=num/10
        num=int(num)

    n=sum
    print(n)