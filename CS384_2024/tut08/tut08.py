import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go

df = pd.read_csv('infy_stock.csv')

print(df.head(10))

print(df.isnull().sum())

df.dropna(inplace=True)

df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Closing Price', color='blue')
plt.title('Closing Price Over Time')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()

fig = go.Figure(data=[go.Candlestick(x=df.index,
                                       open=df['Open'],
                                       high=df['High'],
                                       low=df['Low'],
                                       close=df['Close'])])

fig.update_layout(title='Candlestick Chart',
                  xaxis_title='Date',
                  yaxis_title='Price',
                  xaxis_rangeslider_visible=False)
fig.show()

df['Daily Return'] = ((df['Close'] - df['Open']) / df['Open']) * 100

average_return = df['Daily Return'].mean()
median_return = df['Daily Return'].median()

std_dev_close = df['Close'].std()

print(f'Average Daily Return: {average_return:.2f}%')
print(f'Median Daily Return: {median_return:.2f}%')
print(f'Standard Deviation of Closing Prices: {std_dev_close:.2f}')

df['50_MA'] = df['Close'].rolling(window=50).mean()
df['200_MA'] = df['Close'].rolling(window=200).mean()

plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Closing Price', color='blue')
plt.plot(df['50_MA'], label='50-Day MA', color='orange')
plt.plot(df['200_MA'], label='200-Day MA', color='red')
plt.title('Moving Averages of Closing Price')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()

df['Volatility'] = df['Close'].rolling(window=30).std()

plt.figure(figsize=(12, 6))
plt.plot(df['Volatility'], label='30-Day Rolling Volatility', color='purple')
plt.title('Volatility of the Stock')
plt.xlabel('Date')
plt.ylabel('Volatility')
plt.legend()
plt.grid()
plt.show()

df['Trend'] = 'Neutral'
df.loc[df['50_MA'] > df['200_MA'], 'Trend'] = 'Bullish'
df.loc[df['50_MA'] < df['200_MA'], 'Trend'] = 'Bearish'

plt.figure(figsize=(12, 6))
plt.plot(df['Close'], label='Closing Price', color='blue')
plt.plot(df['50_MA'], label='50-Day MA', color='orange')
plt.plot(df['200_MA'], label='200-Day MA', color='red')

bullish = df[df['Trend'] == 'Bullish']
bearish = df[df['Trend'] == 'Bearish']

plt.scatter(bullish.index, bullish['Close'], label='Bullish', color='green', marker='^', alpha=1)
plt.scatter(bearish.index, bearish['Close'], label='Bearish', color='red', marker='v', alpha=1)

plt.title('Stock Trend Analysis')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid()
plt.show()
