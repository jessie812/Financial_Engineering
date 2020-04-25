# Week 4 Learning Progress

## Content
* Brownian Motion and Geometric Motion
* Interlude: Ito
* Stock Model
* Risk-Neutral
* Interlude: CAPM
* Black-Scholes Formula
* Consider dividend

## Text
### Brownian Motion and Geometric Brownian Motion
#### Brownian Motion
stochastoc process {X(t),t>=0},is a (μ,σ)Brownian motion.

If μ=0 and σ=1, (0,1)Brownian motion=Wiener process.
#### Geometric Brownian Motion
Y(t)=exp{X(t)}

dX=μdt+σdW...prove it below(by Ito Process)
### Interlude: Ito
why dX=μdt+σdW ?
#### Ito Process
assume X={Xt,t>=0} is a stochastic process

    Ito process: Xt= X0+ ∫a(Xs,s)ds+ ∫b(Xs,s)dWs

a(Xs,s) is drift; b(Xs,s) is diffusion

    --(SDE)-- dXt= a(Xt,t)dt+ b(Xt,t)dWt
    --(Simple)-- dXt= atdt+ btdWt

Xt is a (at,bt^2) Brownian Process. If at=0, Xt is martingale
#### Ito Integral
Ito Process: dSt= μtdt+ σtdWt

(consider φt strategy) φtdSt= φt(μtdt+ σtdWt)

(Ito Integral) G(φ)=∫φtdSt= ∫φtμtdt+ ∫φtσtdWt
#### Ito Lemma
in Ito Process: dX= atdt+ btdW

if df(x)=f'(x)adt+ f'(x)bdWt+ (1/2)f"(x)b^2dt 則符合 Ito Lemma

(dX= atdt+ btdW)

df(x)= f'(x)dX+ (1/2)f"(x)(dX)^2

    Ito Formula: df(x)= f'(x)adt+ f'(x)bdWt+ (1/2)f"(x)b^2dt

replace f(x), f'(x), f"(x) with Y

dY/Y= (μ+σ^2/2)dt+ σdW

back to Geometric Brownian Motion

Y(t)= exp(X(t)) <=> X(t)= ln(Y(t))

X(t) is a (μ,σ) Brownian Motion, dX= μdt+ σdW, dY/Y= (μ+σ^2/2)dt+ σdW

Similarly, if dY/Y= μdt+ σdW, then dX= (μ-σ^2/2)dt+ σdW
### Stock Model
Set Stock Model as geometric Brownian Motion

dSt= μStdt+ σStdBt, 0<=t<=T

St= S0* exp{(μ-σ^2/2)t+ σBt}

--ln-- ln(St/S0)= (μ-σ^2/2)t+ σBt, where Bt~n(0,1)

ln(St/S0)~ n((μ-σ^2/2)t, (σ^2)t)

ln(St)~ n(ln(S0)+(μ-σ^2/2)t, (σ^2)t)

St~log-normal
### Risk-Neutral
St is current stock price; K is forward price

f= exp(-rt)E[St-K]= exp(-rt)E[St]- exp(-rt)K

in risk-neutral world: E[St]=exp(rt)S

therefore f= S- exp(-rt)K
### Interlude: CAPM
+ valuing risky cashflow

then f=exp(-θt)E[St]- exp(-rt)K, and E[St]= exp(θt)S

θ= r+ β(E[rm]-r)
### Black-Scholes Formula
c(call)= exp(-rt)E[max(0, St-X)]

let μ becomes the annual expected rate of return of the stock and σ^2 becomes annualized variance of the rate of return on the stock

If St is log-normal

then ln(St)~ n(ln(S)+(μ-σ^2/2)t, (σ^2)t)

and in risk-neutral world μ=r

ln(St)~ n(ln(S)+(r-σ^2/2)t, (σ^2)t)

c= exp(-rt)E[max(0, St-X)]= exp(-rt)∫(St-X)g(St)dSt

= Sn(d1)-exp(-rt)Xn(d2)

(d1= (ln(St/X)+(r+1/2(σ^2))t)/σ√t; d2= d1-σ√t)

p(put)= c+ exp(-rt)X-St= exp(-rt)Xn(-d2)-Sn(-d1)

### Consider dividend
head_S= St- dividend
