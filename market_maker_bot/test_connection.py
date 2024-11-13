import ccxt
from config import config

def test_exchange_connection():
    try:
        # Initialize exchange
        exchange = getattr(ccxt, config['exchange_id'])({
            'apiKey': config['api_key'],
            'secret': config['api_secret'],
            'enableRateLimit': True
        })
        
        # Test public API
        print("Testing market data retrieval...")
        ticker = exchange.fetch_ticker('BTC/USDT')
        print(f"Current BTC/USDT price: {ticker['last']}")
        
        # Test private API
        print("\nTesting account access...")
        balance = exchange.fetch_balance()
        print(f"USDT Balance: {balance.get('USDT', {}).get('free', 0)}")
        
        print("\nConnection test successful!")
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    test_exchange_connection()