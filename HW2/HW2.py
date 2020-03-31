
print("Please enter current bond price :")
pv=float(input())
print("Please enter face value :")
fv=float(input())
print("Please enter coupon rate (%):")
r=int(input())*0.01
print("Please enter bond period (year) :")
t=int(input())

#spot rate
sr=(fv/pv)**(1/t)-1
print(sr)
#YTM 
ytm=(fv*r+(fv-pv)/t)/((fv+2*pv)/3)
print(ytm)
#forward rate

f = [[0]*(t+1) for i in range(t+1)]
for i in range(t+1):
    for j in range(t+1):
        if i==j:
            f[i][j]=0
        elif i==0 and i<j:
            sj=(fv/pv)**(1/j)-1
            f[0][j]=round(((1+sj)**j)**(1/j)-1,4)
            j+=1
        elif i!=0 and i<j:
            sj=(fv/pv)**(1/j)-1
            si=(fv/pv)**(1/i)-1
            f[i][j]=(((1+sj)**j)/((1+si)**i))**(1/(j-i))-1
        else:
            f[i][j]="X"

import pandas as pd
pdf=pd.Series(f)

print(pdf)


