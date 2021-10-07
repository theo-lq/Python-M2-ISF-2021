import yfinance as yf
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns; sns.set(style="ticks")





def call(strike, premium=0, type="buy"):
    call_function = lambda x: (np.maximum(0, x - strike) - premium) * (1 if type == "buy" else -1)
    return call_function



def put(strike, premium=0, type="buy"):
    put_function = lambda x: (np.maximum(0, strike - x) - premium) * (1 if type == "buy" else -1)
    return put_function
    
    
    
    

def plot_curves(ticker_name, operations, expiration_date, alpha=0.1):
    ticker = yf.Ticker(ticker_name)
    
    strikes = [operation["strike"] for operation in operations]
    values = np.linspace(start=min(strikes)*(1-alpha), stop=max(strikes)*(1+alpha), num=500)
    strategie = np.zeros(shape=len(values))
    
    options = ticker.option_chain(expiration_date)
    calls = options.calls
    puts = options.puts
    
    last_historic = ticker.history(period='1d', interval='5m')
    actual_price = float(last_historic["Open"].tail(1))
    
    
    
    for operation in operations:
        if operation["op_type"] == "call":
            premium = float(calls.loc[calls["strike"] == operation["strike"], "lastPrice"])
            function = call(operation["strike"], premium=premium, type=operation["transaction_type"])
        if operation["op_type"] == "put":
            premium = float(puts.loc[puts["strike"] == operation["strike"], "lastPrice"])
            function = put(operation["strike"], premium=premium, type=operation["transaction_type"])
        
        label = ("Long " if operation["transaction_type"] == "buy" else "Short ") + operation["op_type"] + ", strike=" + str(operation["strike"])
        plt.plot(values, function(values), label=label, alpha=0.8)
        strategie = strategie + function(values)
    
    
    
    rule = strategie[:-1] * strategie[1:]
    break_evens = values[np.concatenate((rule, np.array([0]))) < 0].astype(int)
    
    
    plt.axvline(x=actual_price, c="black", alpha=0.3, ls='--', label="Spot")
    title = "Option strategy (" + ticker_name + "), Exp: " + expiration_date
    plt.plot(values, strategie, label="Strategy", lw=4)
    
    plt.fill_between(values, strategie, 0, where=(strategie < 0), alpha=0.30, color=sns.color_palette()[2], interpolate=True)
    plt.fill_between(values, strategie, 0, where=(strategie >= 0), alpha=0.30, color=sns.color_palette()[1], interpolate=True)
    
    plt.plot(break_evens, [0]*len(break_evens), 'o', c="black")
    
    for point in break_evens:
        movement = round(100 * (point / actual_price - 1), 2)
        string = ("+" if movement >= 0 else "-") + str(movement) + "%"
        plt.annotate(string, xy=(point, 0), xytext=(point, 0.03 * (max(strategie) - min(strategie))))
    
    sns.despine()
    plt.title(title)
    plt.xlabel("Stock Price")
    plt.ylabel("Loss / Profit")
    plt.legend()
    plt.show()







operation_1 = {'op_type': 'put', 'strike': 3290, 'transaction_type': 'buy'}
operation_2 = {'op_type': 'call', 'strike': 3290, 'transaction_type': 'buy'}

plot_curves("AMZN", [operation_1, operation_2], "2021-10-15")
