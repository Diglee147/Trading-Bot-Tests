//+------------------------------------------------------------------+
//| Script program start function                                    |
//+------------------------------------------------------------------+
void OnStart()
  {
   string symbol = "EURUSD"; // The currency pair
   int timeframe = PERIOD_H1; // The timeframe
   datetime from_time = StrToTime("2023.01.01 00:00"); // The start time
   datetime to_time = TimeCurrent(); // The end time

   // Request the historical data
   int rates_total = iBars(symbol, timeframe);
   MqlRates rates_array[];

   // Get the historical data
   if(CopyRates(symbol, timeframe, 0, rates_total, rates_array) > 0)
     {
      // Open the file for writing
      string file_name = symbol + "_" + (string)timeframe + ".csv";
      ResetLastError();
      int file_handle = FileOpen(file_name, FILE_WRITE|FILE_CSV, ';');
      if(file_handle != INVALID_HANDLE)
        {
         // Write the data to the file
         for(int i = 0; i < rates_total; i++)
           {
            FileWrite(file_handle, TimeToString(rates_array[i].time, TIME_DATE|TIME_MINUTES), rates_array[i].open, rates_array[i].high, rates_array[i].low, rates_array[i].close, rates_array[i].tick_volume);
           }
         // Close the file
         FileClose(file_handle);
         Print("Data has been written to ", file_name);
        }
      else
        {
         Print("Error opening file. Error code = ", GetLastError());
        }
     }
   else
     {
      Print("Error copying rates. Error code = ", GetLastError());
     }
  }
