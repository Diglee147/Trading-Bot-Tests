string json_file_path = "C:\\Users\\YourUsername\\PathToYourPythonScript\\communication.json";

void OnStart() {
    while (true) {
        string json_content = FileReadText(json_file_path);
        if (json_content != "") {
            // Processa o conteúdo do JSON aqui
            // Por exemplo, se o JSON contém um comando para comprar, então execute uma ordem de compra

            // Depois de processar o JSON, você pode escrever uma resposta no mesmo arquivo
            FileDelete(json_file_path);  // Primeiro, exclua o arquivo antigo
            int file_handle = FileOpen(json_file_path, FILE_WRITE|FILE_TXT|FILE_ANSI);
            if (file_handle != INVALID_HANDLE) {
                FileWrite(file_handle, "{\"response\": \"success\"}");
                FileClose(file_handle);
            }
        }
        Sleep(1000);  // Dorme por um segundo
    }
}
