from django.shortcuts import render, redirect
import random,string

tickers = []
summary = {}
picked = []

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
        fPercentChange = ((fClose - fOpen) / ((fClose + fOpen)/2)) * 100
        return round(fPercentChange, 2)

def stockSwing(fChange):
        if fChange >= 0:
            return "Up"
        else:
            return "Down"

for i in range(100):
        
        sTickerName = tickerFunction()
        tickers.append(sTickerName)

for t in tickers:
        fOpen = stockOpen()

        fClose = stockClose()

        fChange = round(fClose - fOpen, 2)

        fPercentChange = stockChange(fOpen, fClose)

        sSwing = stockSwing(fPercentChange)

        summary[t] = {"swing" : sSwing, 
                    "open" : fOpen, 
                    "close" : fClose, 
                    "change" : fChange,
                    "percentChange": fPercentChange    
                }
    
## views ##

def index(request):

    return render(request,'catwalkpages/index.html')    #render the homepage 


def stockPickerPage(request):
    context = {
        "stocksToPick": tickers,
        "pickedStocks": picked,
        "pickedStocksLength": len(picked)
    }

    changeTotal = 0.0
    percentChangeTotal = 0.0

    if len(picked) == 8:
        for i in picked:
            changeTotal += summary[i]["change"]
            percentChangeTotal += summary[i]["percentChange"]
    
    context["summary"] = summary
    context["changeTotal"] = round(changeTotal, 2)
    context["percentChangeTotal"] = round(percentChangeTotal, 2)

    return render(request,'catwalkpages/stockpicker.html',context)

def pickStock(request):
    ticker = request.GET.get("t")

    if ticker not in picked and len(picked) < 8:
        picked.append(ticker)
    
    print(picked)

    return redirect('stockpicker')

def reset(request):
    picked.clear()
    return redirect('stockpicker')

def catwalk(request):
    # the first random ticker in 2 layered-perimeter
    picked.clear() # clear the ticker list when catwalk button is clicked
    for k in range(8):
          random_ticker = random.choice(tickers)
          picked.append(random_ticker)
    return redirect('stockpicker')
          


