from django.shortcuts import render,redirect
import random,string,math

random.seed(515)

def tickerFunction():
    sTickerName = ''
    for i in range(4):      # stock tickers symbols have 4 upper case letters ?
            sTickerName += random.choice(string.ascii_uppercase)

    return sTickerName

def stockOpen():
    fOpenValue = round(random.uniform(10,200),2)
    return fOpenValue

def stockClose():
    fCloseValue = round(random.uniform(10,200),2)
    return fCloseValue

def stockChange(fOpen, fClose):
    fPercentChange = ((fClose - fOpen) / abs(fClose)) * 100
    return round(fPercentChange, 2)

def stockSwing(fChange):
    if fChange >= 0:
        return "Up"
    else:
        return "Down"

def index(request):

    return render(request,'catwalkpages/index.html')    #render the homepage 


def stockPickerPage(request):
    context = {
        "stocks_to_pick": prices.keys()
    }

    return render(request,'catwalkpages/pick.html',context)


def reset(request):
    pass

def catwalk(request):
    pass

tickers = []

for i in range(10):
    
    sTickerName = tickerFunction()
    tickers.append(sTickerName)
 
prices = {}
for t in tickers:
    fOpen = stockOpen()

    fClose = stockClose()

    fChange = stockChange(fOpen, fClose)

    sSwing = stockSwing(fChange)

    prices[t] = [sSwing, fOpen, fClose, fChange]
