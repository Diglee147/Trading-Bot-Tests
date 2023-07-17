import backtrader as bt
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
                self.buy()
        else:
            if model.predict(np.array([self.dataclose[0]])) < self.dataclose[0]:
                self.sell()

# Create a cerebro
cerebro = bt.Cerebro()

# Add the strategy
cerebro.addstrategy(ForexStrategy)

# Load the data
data = bt.feeds.YahooFinanceCSVData(dataname='historical_data.csv')
cerebro.adddata(data)

# Set our desired cash start
cerebro.broker.setcash(1000.0)

# Run over everything
cerebro.run()

# Print out the final result
print('Final Portfolio Value: %.2f' % cerebro.broker.getvalue())
