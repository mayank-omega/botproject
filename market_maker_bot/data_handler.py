# data_handler.py
import random

def fetch_market_data(symbol):
    # Simulated market data
    return {
        'symbol': symbol,
        'price': round(random.uniform(30000, 60000), 2)  # Simulated price between 30k and 60k
    }