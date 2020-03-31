#Week TWO learning progress

## Content
* YTM, spot rate and forward rate
* Python code Learning Progress
* 流程圖

### YTM, spot rate and forward rate
spot rate 和 forward rate 大部分都在無息的情況下使用，然而因為債券大部分還是會支付利息的，所以市場上比較常使用YTM進行殖利率的計算
***
spot rate=(face value/ current value)^(1/period)-1
***
forward rate(t-1,t)=((1+spot rate(t))^t/(1+spot rate(t-1))^(t-1))^(1/(t-(t-1)))-1
***
YTM: current value= sigma(interest rate*face value/(1+YTM)^n)+face value/(1+YTM)^t, 
to simplify: YTM equals (period interest+ difference of face value and current value/period)/(face value+2*current value)/3
***
### Python code Learning Progress
NA

### 流程圖
輸入current value, face value, period(year), coupon rate
，就可以得出YTM 與 spot rate 最後則是2維陣列的forward rate
