//+------------------------------------------------------------------+
//|                                                communication.mq4 |
//|                                                      Copyright 2023 |
//|                                                      OpenAI          |
//+------------------------------------------------------------------+

// Define o caminho do arquivo compartilhado
#property define FILE_PATH "shared_file.txt"

// Função para enviar dados para o Python
void SendDataToPython(string data)
{
    int file_handle = FileOpen(FILE_PATH, FILE_WRITE);
    if (file_handle != INVALID_HANDLE)
    {
        FileWriteString(file_handle, data);
        FileClose(file_handle);
    }
}

// Função para receber dados do Python
string ReceiveDataFromPython()
{
    string data = "";
    int file_handle = FileOpen(FILE_PATH, FILE_READ);
    if (file_handle != INVALID_HANDLE)
    {
        int file_size = FileSize(file_handle);
        if (file_size > 0)
        {
            data = FileReadString(file_handle, file_size);
        }
        FileClose(file_handle);
    }
    return data;
}

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int init()
{
    return INIT_SUCCEEDED;
}

//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
int deinit()
{
    return 0;
}

//+------------------------------------------------------------------+
//| Expert start function                                            |
//+------------------------------------------------------------------+
int start()
{
    // Aguarda os dados enviados pelo Python
    string data_from_python = ReceiveDataFromPython();
    
    // Faz algum processamento com os dados (opcional)
    // ...

    // Envia uma resposta de volta para o Python
    string response_to_python = "Hello Python!";
    SendDataToPython(response_to_python);

    return 0;
}
