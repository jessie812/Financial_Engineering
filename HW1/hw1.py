import math
import numpy as np

print("please enter total principle (10 thouland) = ")
principle=int(input())
print("please enter total period (year)= ")
period=int(input())
print("please enter annual interest(%)= ")
yr_interest=int(input())


principle_payable=(principle*10000)/(period*12)
print("The principle payable in every month= $", math.ceil(principle_payable))

for i in range(period*12):
     interest_payable=(principle*10000- i*principle_payable)*((yr_interest*0.01)/12)
     print("The interest payable in",(i+1),"th month= $",math.ceil(interest_payable))
     total_payable= principle_payable+interest_payable
     print("The total payable in",(i+1),"th month= $",math.ceil(total_payable))


