import pandas as pd
import pandas_datareader as pdr
import matplotlib.pyplot as plt
import yfinance as yf

# Set the start and end dates
start_date = '2010-01-01'
end_date = '2020-01-01'

# Set the ticker
ticker = '^GSPC'

# Retrieve data for the ticker from Yahoo Finance yf
data = yf.download(ticker, start_date, end_date)
print (data)



# Calculate the monthly return for the S&P 500 index
monthly_return = data['Adj Close'].pct_change()

# Set the initial investment and the number of months to invest
initial_investment = 300
num_months = 120

# Calculate the value of the investment for each month
investment = [initial_investment]
for i in range(1, num_months):
    investment.append(investment[-1] * (1 + monthly_return[i]))

# Calculate the annualized return
annualized_return = (investment[-1] / initial_investment) ** (12 / num_months) - 1

# Print the final value of the investment and the annualized return
# print(f'Final value of the investment:' {investment[-1]:.2f})
print('Annualized return: ',annualized_return,' %')

# Plot the evolution of the investment
plt.plot(investment)
plt.xlabel('Month')
plt.ylabel('Value of Investment')
plt.title('Evolution of Investment')
plt.show()