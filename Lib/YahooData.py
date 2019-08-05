#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 13:52:32 2019

@author: Thomas
"""
import pandas as pd  
import numpy as np
from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
yf.pdr_override() 

# function to get the price data from yahoo finance 
def getDataBatch(tickers, startdate, enddate):
  def getData(ticker):
    return (pdr.get_data_yahoo(ticker, start=startdate, end=enddate))
  datas = map(getData, tickers)
  return(pd.concat(datas, keys=tickers, names=['Ticker', 'Date']))

def getAdjPrice(tickers, start_dt, end_dt): 
    px_data = getDataBatch(tickers, start_dt, end_dt)
    px = px_data[['Adj Close']]
    return(px)

def getReturn(tickers, start_dt, end_dt): 
    px_data = getDataBatch(tickers, start_dt, end_dt)
    Ret = px_data[['Adj Close']].reset_index().pivot(index='Date', columns='Ticker', values='Adj Close').pct_change().dropna()
    return(Ret)
