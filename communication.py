import os

# Define o caminho do arquivo compartilhado
shared_file_path = "shared_file.txt"

# Função para enviar dados para o MQL4
def send_data_to_mql(data):
    with open(shared_file_path, "w") as file:
        file.write(data)

# Função para receber dados do MQL4
def receive_data_from_mql():
    with open(shared_file_path, "r") as file:
        data = file.read()
    return data

# Exemplo de uso
data_to_send = "Hello MQL4!"
send_data_to_mql(data_to_send)

# Aguarda a resposta do MQL4
response_from_mql = receive_data_from_mql()
print("Response from MQL4:", response_from_mql)
