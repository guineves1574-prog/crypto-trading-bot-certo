import ccxt
import pandas as pd
import time
import os
from ta.momentum import RSIIndicator

API_KEY = os.getenv("API_KEY")
SECRET = os.getenv("SECRET")

symbols = ["BTC/USDT", "ETH/USDT", "SOL/USDT"]
timeframe = "1h"

exchange = ccxt.binance({
    'apiKey': API_KEY,
    'secret': SECRET,
    'enableRateLimit': True
})

def get_data(symbol):
    candles = exchange.fetch_ohlcv(symbol, timeframe, limit=100)
    df = pd.DataFrame(candles, columns=['time','open','high','low','close','volume'])
    return df

def calculate_rsi(df):
    rsi = RSIIndicator(close=df['close'], window=14)
    df['rsi'] = rsi.rsi()
    return df

def check_trade(symbol):
    df = get_data(symbol)
    df = calculate_rsi(df)

    last_rsi = df['rsi'].iloc[-1]
    price = df['close'].iloc[-1]

    print(f"{symbol} | RSI: {last_rsi:.2f} | Price: {price}")

    if last_rsi < 30:
        print(f"🟢 SINAL DE COMPRA {symbol}")

    elif last_rsi > 70:
        print(f"🔴 SINAL DE VENDA {symbol}")

while True:
    try:
        for symbol in symbols:
            check_trade(symbol)

        time.sleep(60)

    except Exception as e:
        print("Erro:", e)
        time.sleep(10)
