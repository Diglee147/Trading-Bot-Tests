//+------------------------------------------------------------------+
//|                                                      EA_Sample.mq4|
//|                        Copyright 2005, MetaQuotes Software Corp. |
//|                                              https://www.mql5.com |
//+------------------------------------------------------------------+
#property copyright "2005, MetaQuotes Software Corp."
#property link      "https://www.mql5.com"
#property version   "1.00"
//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int init()
  {
//----
   
//----
   return(0);
  }
//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
int deinit()
  {
//----
   
//----
   return(0);
  }
//+------------------------------------------------------------------+
//| Expert start function                                            |
//+------------------------------------------------------------------+
int start()
  {
//----
   double prediction = 0.0; // Replace this with the prediction from your model
   double lotSize = 0.01; // Replace this with your desired lot size
   int slippage = 3; // Replace this with your desired slippage
   double stopLoss = 0.0; // Replace this with your desired stop loss
   double takeProfit = 0.0; // Replace this with your desired take profit
   
   if (prediction > 0)
   {
      OrderSend(Symbol(), OP_BUY, lotSize, Ask, slippage, stopLoss, takeProfit);
   }
   else
   {
      OrderSend(Symbol(), OP_SELL, lotSize, Bid, slippage, stopLoss, takeProfit);
   }
   
   double balance = AccountBalance(); // Get the current account balance
   double equity = AccountEquity(); // Get the current account equity
   double drawdown = 100.0 * (balance - equity) / balance; // Calculate the drawdown in percent
   
   if (drawdown > 20.0) // If the drawdown is greater than 20%
   {
      Alert("High drawdown detected: ", drawdown, "%");
   }
   
//----
   return(0);
  }
//+------------------------------------------------------------------+
