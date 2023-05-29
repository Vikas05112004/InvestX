#!/usr/bin/env python
# coding: utf-8

# # Stochastic 
# 

# In[1]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


ticker = "MSFT"
start_date = "2022-05-23"
end_date = "2023-05-23"


data = yf.download(ticker, start=start_date, end=end_date)


def calculate_stochastic_oscillator(data, window=14):
    data["Lowest Low"] = data["Low"].rolling(window=window).min()
    data["Highest High"] = data["High"].rolling(window=window).max()
    data["%K"] = (data["Close"] - data["Lowest Low"]) / (data["Highest High"] - data["Lowest Low"]) * 100
    data["%D"] = data["%K"].rolling(window=3).mean()
    return data


data1 = calculate_stochastic_oscillator(data)
data1["%K"] = data1["%K"].fillna(0)  # jaha data nhi h 0 bhar do 
data1["%D"] = data1["%D"].fillna(0)

print()
plt.figure(figsize=(12, 6))
plt.plot(data.index, data["%K"], label="%K")
plt.plot(data.index, data["%D"], label="%D")
plt.title("Stochastic Oscillator")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()


# # Accumulation / Distribution Indicator

# In[2]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


ticker_symbol = "MSFT"
start_date = "2022-05-26"
end_date = "2023-05-26"


data = yf.download(ticker_symbol, start=start_date, end=end_date)


MFM = ((data['Close'] - data['Low']) - (data['High'] - data['Close'])) / (data['High'] - data['Low'])
MFM = MFM.fillna(0.0)  # Replace any NaN values with 0.0


MFV = MFM * data['Volume']


ADL = MFV.cumsum()

plt.figure(figsize=(10, 6))
plt.plot(ADL, label='ADL')
plt.title('Accumulation Distribution Line (ADL)')
plt.xlabel('Date')
plt.ylabel('ADL Value')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:





# # Implied Volatility

# In[ ]:





# In[ ]:





# 
