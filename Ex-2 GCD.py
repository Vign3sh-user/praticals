'''
Write a python program to implement the 
Euclid algorithm to generate the GCD of 
an array of 10 integers.
'''

def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)


arr=[12,24,32,44,52,64,72,84,92,28]
for i in range(1,len(arr)-1):
    n=gcd(arr[i],arr[i+1])
print("\n",arr)
print("\nGCD of the given array is: ",n,"\n")
