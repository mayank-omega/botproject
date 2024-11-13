# main.py
import time
from strategy import MarketMaker
from logger import setup_logging

def main():
    setup_logging()
    market_maker = MarketMaker()

    while True:
        try:
            market_maker.place_orders()
            time.sleep(10)  # Wait for 10 seconds before placing new orders
        except Exception as e:
            print(f'Error: {e}')

if __name__ == "__main__":
    main()