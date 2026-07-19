def gcd(m,n):
    cf=[]
    for i in range(1,(min(m,n)+1)):
        if (m%i)==0 and (n%i)==0:
            cf.append(i)
    return(cf[-1])
# to get the GCD output:
m=int(input("Enter the First Number:"))
n=int(input("Enter the Second Number:"))
x = gcd(m,n)
print("The GCD output is:",x)
     
         