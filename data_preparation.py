import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Load the data
df = pd.read_csv('EURUSD_H1.csv')

# Clean the data
# Drop any rows with missing values
df = df.dropna()

# Create features
# For example, create a feature that represents the difference between the high and low prices
df['High_Low_Difference'] = df['High'] - df['Low']

# Normalize the data
scaler = MinMaxScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

# Split the data into training, validation and test sets
train_df, test_df = train_test_split(df_scaled, test_size=0.2, random_state=42)
train_df, val_df = train_test_split(train_df, test_size=0.25, random_state=42)

# Save the prepared data
train_df.to_csv('train.csv', index=False)
val_df.to_csv('val.csv', index=False)
test_df.to_csv('test.csv', index=False)
