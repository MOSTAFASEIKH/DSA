def gcd(m,n):
    i=min(m,n)
    while i>0:
        if (m%i)==0 and (n%i)==0:
            return(i)
        else:
            i=i-1
# to get the GCD output:
m=int(input("Enter the First Number:"))
n=int(input("Enter the Second Number:"))
x = gcd(m,n)
print("The GCD output is:",x)