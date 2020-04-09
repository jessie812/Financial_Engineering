##input
x=float(input("Please enter strike price($) "))
s=float(input("Please enter stock price($) "))
r=float(input("Please enter riskless interest rate(%) "))*0.01
u=float(input("Please enter multiple "))
d=float(input("Please enter multiple of fall "))
n=int(input("Please enter # of periods "))

###progress
##background
import math 

R=math.exp(r)
p=(R-d)/(u-d)

s_=[] #last degree of stock price
c_=[] #last degree of calls value
p_=[] #last degree of put value
for i in range(1,n+2):
    s_.append((s*(u**(n-i+1))*(d**(i-1))))
    c_.append(max(s_[i-1]-x,0))
    p_.append(max(0,x-s_[i-1]))

##for loop
#call
c=[[0]*n for i in range(n)]

for i in range(n):
    c[0][i]=round((p*c_[i]+(1-p)*c_[i+1])/R, 3)
for i in range(1,n):
    for j in range(n-1):
        c[i][j]=round((p*c[i-1][j]+(1-p)*c[i-1][j+1])/R,3)
for i in range(n):
    for j in range(n-i):
        print(c[i][j]," ",end=" ")
    print()

#put
put=[[0]*n for i in range(n)]

for i in range(n):
    put[0][i]=round((p*p_[i]+(1-p)*p_[i+1])/R, 3)
for i in range(1,n):
    for j in range(n-1):
        put[i][j]=round((p*put[i-1][j]+(1-p)*put[i-1][j+1])/R, 3)
for i in range(n):
    for j in range(n-i):
        print(put[i][j]," ",end=" ")
    print()

##Conclusion
print("Call value = ", c[n-1][0])
print("Put value = ", put[n-1][0])

