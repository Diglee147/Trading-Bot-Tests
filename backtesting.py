import backtrader as bt
import pandas as pd
from tensorflow.keras.models import load_model
import numpy as np

# Load the trained model
model = load_model('model.h5')

class ForexStrategy(bt.Strategy):
    def __init__(self):
        self.dataclose = self.datas[0].close

    def next(self):
        if self.order:
            return

        if not self.position:
            if model.predict(np.array([self.dataclose[0]])) > self.dataclose[0]:
                self.buy(size=1)  # Buy 1 unit of the asset
        else:
            if model.predict(np.array([self.dataclose[0]])) < self.dataclose[0]:
                self.sell(size=1)  # Sell 1 unit of the asset

# Prepare the data for backtesting
train_df = pd.read_csv('train.csv')
val_df = pd.read_csv('val.csv')
test_df = pd.read_csv('test.csv')

data = bt.feeds.PandasData(dataname=train_df)
cerebro = bt.Cerebro()
cerebro.adddata(data)

# Add the strategy
cerebro.addstrategy(ForexStrategy)

# Set the initial cash value
initial_cash = 100.0
cerebro.broker.setcash(initial_cash)

# Run the backtest on training data
cerebro.run()

# Calculate the final portfolio value on training data
train_portfolio_value = cerebro.broker.getvalue()

# Reset the backtest
cerebro.reset()

# Add the validation data
data = bt.feeds.PandasData(dataname=val_df)
cerebro.adddata(data)

# Run the backtest on validation data
cerebro.run()

# Calculate the final portfolio value on validation data
val_portfolio_value = cerebro.broker.getvalue()

# Reset the backtest
cerebro.reset()

# Add the test data
data = bt.feeds.PandasData(dataname=test_df)
cerebro.adddata(data)

# Run the backtest on test data
cerebro.run()

# Calculate the final portfolio value on test data
test_portfolio_value = cerebro.broker.getvalue()

# Save the final portfolio values for use by the bot
portfolio_value_file = open('portfolio_value.txt', 'w')
portfolio_value_file.write(f'Training Portfolio Value: {train_portfolio_value:.2f}\n')
portfolio_value_file.write(f'Validation Portfolio Value: {val_portfolio_value:.2f}\n')
portfolio_value_file.write(f'Test Portfolio Value: {test_portfolio_value:.2f}\n')
portfolio_value_file.close()
