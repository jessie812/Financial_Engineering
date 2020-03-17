#本金平均攤還CAM
import math

print("please enter total principle (10 thouland) = ")
principle=int(input())
print("please enter total period (year)= ")
period=int(input())
print("please enter annual interest(%)= ")
yr_interest=int(input())


principle_payable=(principle*10000)/(period*12)
print("The principle payable in every month= $", math.ceil(principle_payable))

total_interest=0
forall=0
for i in range(period*12):
     interest_payable=(principle*10000- i*principle_payable)*((yr_interest*0.01)/12)
     print("The interest payable in",(i+1),"th month= $",math.ceil(interest_payable))
     total_payable= principle_payable+interest_payable
     print("The total payable in",(i+1),"th month= $",math.ceil(total_payable))
     total_interest= total_interest+interest_payable
     forall= forall+total_payable
     
print("The total interest is $", total_interest)
print("The total payment of debt is $", forall)

# 本息平均攤還CPM
m_interest=yr_interest*0.01/12

m_payable_rate= (((1+m_interest)**(12*period))*m_interest)/(((1+m_interest)**(12*period))-1)
Itotal_payable=(principle*10000*m_payable_rate)
Iforall=Itotal_payable*period*12
print("The total month payable in CPM is $",math.ceil(Itotal_payable))
print("The total payment in CPM is $",math.ceil(Iforall))

if Iforall>forall:
     print("The method of CAM is better than CPM")
elif Iforall<forall:
     print("The methods of CPM is better than CAN")
else:
     print("They are the same")