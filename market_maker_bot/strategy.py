# strategy.py
from exchange import Exchange
from config import SYMBOL, SPREAD, ORDER_SIZE

class MarketMaker:
    def __init__(self):
        self.exchange = Exchange()

    def place_orders(self):
        ticker = self.exchange.fetch_ticker(SYMBOL)
        buy_price = ticker['ask'] - SPREAD / 2
        sell_price = ticker['bid'] + SPREAD / 2

        self.exchange.create_limit_buy_order(SYMBOL, ORDER_SIZE, buy_price)
        self.exchange.create_limit_sell_order(SYMBOL, ORDER_SIZE, sell_price)
        print(f'Placed buy order at {buy_price} and sell order at {sell_price}')