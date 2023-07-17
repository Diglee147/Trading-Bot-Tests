import time
import json

def send_data_to_mql(data):
    with open('communication.json', 'w') as f:
        json.dump(data, f)

def receive_data_from_mql():
    with open('communication.json', 'r') as f:
        data = json.load(f)
    return data

# Exemplo de uso
send_data_to_mql({'command': 'buy', 'symbol': 'EURUSD', 'volume': 0.01})
time.sleep(1)  # Espera um pouco para o MQL4 ter tempo para ler o arquivo
response = receive_data_from_mql()
print(response)
