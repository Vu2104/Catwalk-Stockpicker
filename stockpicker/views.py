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

def index(request): # this view renders the index page of the catwalk web application
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

def pickStock(request): # function that allows user to pick 8 stocks
    ticker = request.GET.get("t") # gets string value from url when user picks specific stock on grid

    if ticker not in picked and len(picked) < 8: # checks if ticker has not been added to the picked list and the number of picked stocks is less than 8
        picked.append(ticker)

    return redirect('stockpicker')

def reset(request):
    picked.clear()
    return redirect('stockpicker')

def catwalk(request):
    picked.clear() # clear the ticker list when catwalk button is clicked

    random_tickers= [] # list for catwalk-algorithm randomly generated tickers

    # randomly generated tickers in the 0,1,8,9 ROWS of the table
    first_row_ticker = list(range(0,10))     # generate random ticker of the first row
    second_row_ticker = list(range(10,20))   # generate random ticker of the second row
    ninth_row_ticker = list(range(80,90))    # generate random ticker of the ninth row
    tenth_row_ticker = list(range(90,100))    # generate random ticker of the tenth row

    combined_row_tickers = first_row_ticker + second_row_ticker + ninth_row_ticker + tenth_row_ticker # list of the combined row tickers

    # randomly generated tickers in the 0,1,8,9 COLUMNS of the table
    first_column_ticker = list(range(0,100,10))      # same idea ?
    second_column_ticker = list(range(1,100,10))  
    ninth_column_ticker =  list(range(8,100,10))  
    tenth_column_ticker = list(range(9,100,10)) 

    combined_column_tickers = first_column_ticker + second_column_ticker + ninth_column_ticker + tenth_column_ticker #combined list of perimeter tickers

    perimeter = combined_row_tickers + combined_column_tickers # perimeter of the whole grid

    start_perimeter_ticker = random.choice(perimeter) # randomly choose one of that perimeter tickers
    random_tickers.append(tickers[start_perimeter_ticker])
    print(tickers.index(tickers[start_perimeter_ticker]))


    while len(random_tickers) < 8:
        next_ticker = random.choice(tickers)  # choose in the 100 tickers

        if next_ticker in random_tickers:    
            continue

        last_ticker = random_tickers[-1]
        last_index = tickers.index(last_ticker)
        next_index = tickers.index(next_ticker)

        if abs(next_index - last_index) <= 3 or abs(next_index - last_index) >= 10:    # this mean the loop if the step less than or equal 3 and if the 
            continue                                                                   #    step greater than or equal to 10, skip adding the stock to picked stocks list
            

        random_tickers.append(next_ticker)        # append to the random_tickers if all the conditions are satisfied

    for a in random_tickers: # append the random stocks from algorithm to the picked stock list
          picked.append(a)

    return redirect('stockpicker')



