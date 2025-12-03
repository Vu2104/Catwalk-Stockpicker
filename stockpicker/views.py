from django.shortcuts import render, redirect
import random,string

tickers = [] # list that holds all ticker symbols for stocks
summary = {} # dictionary that holds a nested dictionary of stock ticker summary values
picked = [] # list that holds selected stocks by user/catwalk

# created functions, lists, and dictionaries to store all the values and summary values for the stock picker web application.
# we decided to calculate all the summary values immediately with functions so that it's understandable to follow while reading the source code.

def tickerFunction(): # creates stock ticker symbols of 4 uppercase letters
        sTickerName = ''
        for i in range(4):
                sTickerName += random.choice(string.ascii_uppercase)
        return sTickerName

def stockOpen(): # creates a random open value from 10.0 to 200.0
        fOpenValue = round(random.uniform(10,200),2)
        return fOpenValue

def stockClose(): # creates a random close value from 10.0 to 200.0
        fCloseValue = round(random.uniform(10,200),2)
        return fCloseValue

def stockChange(fOpen, fClose): # calculates the percent difference between the close and open value of stock
        fPercentChange = ((fClose - fOpen) / fOpen) * 100
        return round(fPercentChange, 2)

def stockSwing(fChange): # string describing the swing of stock. Takes the difference between the close and 
        if fChange >= 0: #      open value and returns "Up" if positive and "Down" if negative
            return "Up"
        else:
            return "Down"

for i in range(100): # creates 100 random Ticker symbols and appends to tickers list
        sTickerName = tickerFunction()
        tickers.append(sTickerName)

for t in tickers: # calls functions defined above to create summary values for each stock in tickers list
        fOpen = stockOpen() # generates open value

        fClose = stockClose() # generates close value

        fChange = round(fClose - fOpen, 2) # calculates difference between close and open value

        fPercentChange = stockChange(fOpen, fClose) # calculates percent difference between close and open value

        sSwing = stockSwing(fChange) # returns swing of stock, up or down depending on 

        summary[t] = {"swing" : sSwing, # for each stock ticker symbol, create a key value pair with ticker name as the key
                    "close" : fClose,   # and a nested dictionary that holds the stock's summary values
                    "open" : fOpen, 
                    "change" : fChange,
                    "percentChange": fPercentChange    
                }
    
### VIEWS ###

def index(request): # this view renders the index page of the catwalk web application
    return render(request,'catwalkpages/index.html')    #render the homepage 


def stockPickerPage(request): # this view provides the functionality for manually picking 8 stocks of the user's choosing
    context = {                     # context includes the tickers list, the picked stocks list, and the length of the picked stocks list.
        "stocksToPick": tickers,
        "pickedStocks": picked,
        "pickedStocksLength": len(picked)
    }

    changeTotal = 0.0
    percentChangeTotal = 0.0

    if len(picked) == 8: # when the user picks 8 stocks, total dollar change and total percentage change is calculated
        for i in picked:
            changeTotal += summary[i]["change"] # accesses the dollar change value of a stock using ticker name as key 
            percentChangeTotal += summary[i]["percentChange"] # accesses percent change value of a stock using ticker name as key
    
    context["summary"] = summary # adds summary to the context
    context["changeTotal"] = round(changeTotal, 2) # adds changeTotal to the context, rounded to two decimal points
    context["percentChangeTotal"] = round(percentChangeTotal, 2) # adds percentChangeTotal to the context, rounded to two decimal points

    return render(request,'catwalkpages/stockpicker.html',context) # renders the stockpicker web app template

def pickStock(request): # function that allows user to pick 8 stocks
    ticker = request.GET.get("t") # gets string value from url when user picks specific stock on grid

    if ticker not in picked and len(picked) < 8: # checks if ticker has not been added to the picked list and the number of picked stocks is less than 8
        picked.append(ticker)

    return redirect('stockpicker')

def reset(request): # reset function clears the picked list, removing all stocks that were picked from the list
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



