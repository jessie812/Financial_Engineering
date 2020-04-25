#input variables
s=float(input("Please enter current stock price($)= "))
sigma=float(input("Please enter 震盪率(%)= "))*0.01
d_period=int(input("Please enter # of dividends annually(1 or 2 or 4)= "))
d=int(input("Please enter dividend ($/per)= "))
x=float(input("Please enter forward price($)="))
r=float(input("Please enter expected rate(%)= "))*0.01
t=int(input("Please enter maturity(month)= "))/12

#preliminary work
from math import exp, log, e, sqrt
from scipy.stats import norm
def ln(x):
    return log(x,e)

#set dividend
D=0
if d_period==1:
    D=d*exp(-r*(1/12))
elif d_period==2:
    D=d*(exp(-r*(1/12))+exp(-r*(4/12)))
else:
    D=d*(exp(-r*(1/12))+exp(-r*(4/12))+exp(-r*(7/12))+exp(-r*(10/12)))

#find d1 and d2
head_s=s-D
d1=(ln(head_s/x)+(r+(sigma**2)/2)*t)/(sigma*sqrt(t))
d2=d1-sigma*sqrt(t)

#call and put
c=round(head_s*norm.cdf(d1)-x*exp(-r*t)*norm.cdf(d2),3)
p=round(x*exp(-r*t)*norm.cdf(-d2)-head_s*norm.cdf(-d1),3)

print("The call price is=$",c)
print("The put price is=$",p)