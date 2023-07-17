import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Load the validation data
val_df = pd.read_csv('val.csv')

# Separate the features and the target
X_val = val_df.drop('Close', axis=1)
y_val = val_df['Close']

# Load the trained model
model = load_model('model.h5')

# Make predictions on the validation data
y_pred = model.predict(X_val)

# Calculate performance metrics
performance_metrics = {}
performance_metrics['MSE'] = mean_squared_error(y_val, y_pred)
performance_metrics['MAE'] = mean_absolute_error(y_val, y_pred)
performance_metrics['R^2'] = r2_score(y_val, y_pred)

# Plot the results
plt.plot(y_val, label='Actual')
plt.plot(y_pred, label='Predicted')
plt.xlabel('Time')
plt.ylabel('Price')
plt.legend()
plt.show()

# Save the performance metrics for future reference
# You can save the metrics in a data structure or write them to a file

# Example: Saving the metrics in a file
metrics_file = open('performance_metrics.txt', 'w')
for metric, value in performance_metrics.items():
    metrics_file.write(f'{metric}: {value}\n')
metrics_file.close()
