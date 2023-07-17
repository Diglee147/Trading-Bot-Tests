import pandas as pd
from tensorflow import keras
from tensorflow.keras import layers
from kerastuner.tuners import RandomSearch

# Load the training data
train_df = pd.read_csv('train.csv')

# Separate the features and the target
X_train = train_df.drop('Close', axis=1)
y_train = train_df['Close']

def build_model(hp):
    model = keras.Sequential()
    model.add(layers.Dense(units=hp.Int('units_1', min_value=64, max_value=256, step=32), activation='relu', input_shape=(X_train.shape[1],)))
    model.add(layers.Dropout(hp.Float('dropout_1', min_value=0.1, max_value=0.5, step=0.1)))
    
    for i in range(hp.Int('num_layers', 1, 3)):
        model.add(layers.Dense(units=hp.Int('units_' + str(i+2), min_value=64, max_value=256, step=32), activation='relu'))
        model.add(layers.Dropout(hp.Float('dropout_' + str(i+2), min_value=0.1, max_value=0.5, step=0.1)))
    
    model.add(layers.Dense(1))
    
    model.compile(
        optimizer=keras.optimizers.Adam(hp.Choice('learning_rate', values=[1e-2, 1e-3, 1e-4])),
        loss='mean_squared_error',
        metrics=['mean_squared_error'])
    
    return model

tuner = RandomSearch(
    build_model,
    objective='val_mean_squared_error',
    max_trials=5,
    executions_per_trial=3,
    directory='my_dir',
    project_name='helloworld')

tuner.search_space_summary()

tuner.search(X_train, y_train,
             epochs=50,
             validation_data=(X_val, y_val))

tuner.results_summary()
