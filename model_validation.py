import pandas as pd
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
mse = mean_squared_error(y_val, y_pred)
mae = mean_absolute_error(y_val, y_pred)
r2 = r2_score(y_val, y_pred)

# Print the performance metrics
print(f'MSE: {mse}')
print(f'MAE: {mae}')
print(f'R^2: {r2}')
