# Week 3 Learning Progress

## Content
* Binominal Option Pricing Model (BOPM)
* BOPM with probability
* Multi-Period and Backward
* HW discussion

## Text
### Binominal Option Pricing Model (BOPM)
#### Assumption
1. 時間是離散的
2. 股價是完全隨機，交易市場資訊與流動性完全透明，無法預測
3. u為漲價倍數，d為跌價倍數，其一定符合d<R<u，因為若是投資市場獲利低於無風險報酬則無人投資(當連續複利時R=e^r)
4. p是發生u的機率，因此d的機率則為(1-p)
#### Theory
在無套利市場，不論是利用選擇權操作或是購買債權、投資股票，其payoff會相等，因此假設今天買入h股的股票和B元債券則
`h*S(stock price)+B*R(riskless payoff)=option price`

若是再進一步考慮u,d，則會是`hSu+BR=Cu(or Pu)`和`hsd+BR=Cd(or Pd)`二項式後則可以得出

    h=(Cu-Cd)/(Su-Sd) (C, P可自由替換)
    B=(uCd-dCu)/(u-d)R OR B=(uPd-dPu)/(u-d)R
### BOPM with probability
#### Previous
然而上述並不完整，因為沒有考慮機率進去，若是考慮機率則
`E(S)=pSu+(1-p)Sd`
#### Pseudo Probability
將未考慮機率的BOPM用上式E(S)替代後會得

    C=hS+B=(((R-d)/(u-d))Cu+((u-R)/(u-d))Cd)/R
    then p approximately equal (R-d)/(u-d)

### Multi Period and Backward
若是總期數有n期，則到第n期時會有(n+1)個現貨價值，以n=2來說，第二期時就會有Suu, Sud, Sdd三種可能性，而從這三種可能性中可以直接推出選擇權的價格
，以買權為例，Cuu=max(Suu-X, 0), Cud=max(Sud-X, 0), and Cdd=max(Sdd-X, 0)，顯然第n期的C也會有(n+1)個，畢竟C是由S導過來的。然而在n=2時
第一期的C則是由第二期C決定，像是Cu=(pCuu+(1-p)Cud)/R, Cd=(pCud+(1-p)Cdd)/R。
以此類推，若是n=100時道理也是一樣的，由第100層推99th, 99th推98th...。

### HW discussion
從一開始的BOPM到最後的Backward都很明顯的表現出在計算option price的時候可以利用python中的巢狀遞迴跑出Binominal Process for the price。
```py
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
```
輸入老師在作業三中所給的範例，則會得出
```py
Please enter strike price($) 150
Please enter stock price($) 160
Please enter riskless interest rate(%) 18.232
Please enter multiple 1.5
Please enter multiple of fall 0.5
Please enter # of periods 3
[390.0, 30.0, 0, 0]
235.0   17.5   0.0   
141.458   10.208   
85.069    
```
Put 也是相同概念，得出的結果會是
```py
[0, 0, 90.0, 130.0]
0.0   22.5   85.0   
5.625   34.375   
11.875   
```
兩者的最後一個值就是買權跟賣權的價格，因此最後再加上這段程式碼：
```py
print("Call value = ", c[n-1][0])
print("Put value = ", put[n-1][0])
```
就可以得出payoff!

