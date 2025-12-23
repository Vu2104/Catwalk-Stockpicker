from django.shortcuts import render, redirect
import random,string

tickers = []
for i in range(100):        # there are 100 stocks to pick
    random_stock = ' '      # here i create an empty string for the stock, then I add the strings after it
    for j in range(4):      # stock tickers symbols have 4 upper case letters ?
        random_stock += random.choice(string.ascii_uppercase) # this is the randomly generated stock using imported string module
    tickers.append(random_stock)


def index(request):

    return render(request,'catwalkpages/index.html')    #render the homepage 


def stockPickerPage(request):
    context = {
        "stocks_to_pick": tickers
    }

        

    return render(request,'catwalkpages/pick.html',context)

def pickStock(request):
    ticker = request.GET.get("t")

    if ticker not in picked and len(picked) < 8:
        picked.append(ticker)
    
    print(picked)

    return redirect('stockpicker')

def reset(request):
    pass

def reset(request):

    return redirect("pick")

def catwalk(request):
    # the first random ticker in 2 layered-perimeter
    picked.clear() # clear the ticker list when catwalk button is clicked
    for k in range(8):
          random_ticker = random.choice(tickers)
          picked.append(random_ticker)
    return redirect('stockpicker')
          


