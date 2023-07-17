import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam

# Load the training and validation data
train_df = pd.read_csv('train.csv')
val_df = pd.read_csv('val.csv')

# Separate the features and the target
X_train = train_df.drop('Close', axis=1)
y_train = train_df['Close']
X_val = val_df.drop('Close', axis=1)
y_val = val_df['Close']

# Define the model
model = Sequential([
    Dense(128, activation='relu', input_shape=(X_train.shape[1],)),
    Dropout(0.2),
    Dense(128, activation='relu'),
    Dropout(0.2),
    Dense(1)
])

# Compile the model
model.compile(
    optimizer=Adam(0.001),
    loss='mean_squared_error'
)

# Train the model
history = model.fit(
    X_train,
    y_train,
    validation_data=(X_val, y_val),
    epochs=100,
    batch_size=32
)

# Save the model
model.save('model.h5')
