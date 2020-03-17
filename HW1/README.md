# Week ONE learning progress

## Content
* 本金平均攤還 vs. 本息平均攤還
* Python code Learning Progress
* 流程圖


### 本金平均攤還 vs. 本息平均攤還
傳統貸款大部分是使用「本息平均」攤還，每月繳納月付金均相同。而本金平均攤還則是每月應繳本金相同，但卻因為每期利息不同所以總付款金額不一樣。
***
本金平均攤還公式：
* 每期應繳本金＝借款總額/總其數
* 當月利息＝每期借款餘額＊月利率
* 當月月付金＝每期應繳本金＋當月利息
***
本息平均攤還
* 每期應還本金平均攤還率＝{[(1+月利率)＾月數]＊月利率}/{[(1+月利率)＾月數]-1}
* 當月月付金＝本金＊平均攤還率
* 當月利息＝本金餘額＊月利息
* 每期應繳本金＝當月月付金-當月利息
***
接著利用Python 試算不同情況下兩者所需支付的金額

### Python Code Learning Progress

#### 前期過程
##### CAM

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
    
一開始寫到這裡都沒有什麼問題，先得到需要的參數值後，就可以直接獲得每期應負本金（本金/總期數），在此假設為變數principle_payable。
然而到了我想要求出整個貸款的總利率與總支出階段，我卡住了。剛開始我是這麼寫的：

    for i in range(period*12):
     interest_payable=(principle*10000- i*principle_payable)*((yr_interest*0.01)/12)
     print("The interest payable in",(i+1),"th month= $",math.ceil(interest_payable))
     total_payable= principle_payable+interest_payable
     print("The total payable in",(i+1),"th month= $",math.ceil(total_payable))
     sum_in=sum(interest_payable)
     sum_to=sum(total_payable)
     print(sum_in)
     print(sum_to)

但print出來的結果永遠都是最後一期所要支付的利息與總金額，後來我才發現，因為迴圈的關係，他只會跑到最後一個給我，因此我把code改成如下：

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

先設兩個需要的變數為零，利用y=x+y方式應用迴圈，得到迴圈的總額。
##### CPM
後來我很好奇究竟CAM跟CPM這兩個方法的結果跑出來會不會一樣，因此我多寫了CPM的程式：

    m_interest=yr_interest*0.01/12

    m_payable_rate= (((1+m_interest)**(12*period))*m_interest)/(((1+m_interest)**(12*period))-1)
    Itotal_payable=(principle*10000*m_payable_rate)
    Iforall=Itotal_payable*period*12
    print("The total month payable in CPM is $",math.ceil(Itotal_payable))
    print("The total payment in CPM is $",math.ceil(Iforall))
##### Comparison
最後將CPM與CAM的支付總額作比較，透過if-else的公式達到條件性的排除

    if Iforall>forall:
     print("The method of CAM is better than CPM")
    elif Iforall<forall:
     print("The methods of CPM is better than CAN")
    else:
     print("They are the same")

### 流程圖
> 蒐集參數
>> 參數包括：本金金額（萬元）、年利率（％）以及總期數（年）
> 跑出CPM的每期固定本金與每期不同利息、總額
> 跑出CPM借貸總支付利息與金額
> 跑出CAM借貸每期固定總額與借貸期間總金額
> 比較CPM與CAM何者支付期間所需支付總金額較少
>> 較少支付總額的方法會跑出來推薦借貸者

