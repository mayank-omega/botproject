import time
import logging
from decimal import Decimal
import ccxt
from config import config

class SimpleMarketMaker:
    def __init__(self, config):
        self.exchange = getattr(ccxt, config['exchange_id'])({
            'apiKey': config['api_key'],
            'secret': config['api_secret'],
            'enableRateLimit': True
        })
        
        self.symbol = config['symbols'][0]  # Start with first symbol
        self.spread = Decimal(str(config['base_spread_percentage']))
        self.order_size = Decimal(str(config['order_size']))
        self.setup_logging()
        
    def setup_logging(self):
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def get_market_price(self):
        try:
            ticker = self.exchange.fetch_ticker(self.symbol)
            return Decimal(str(ticker['last']))
        except Exception as e:
            self.logger.error(f"Error getting market price: {e}")
            return None
    
    def place_orders(self, market_price):
        try:
            # Calculate order prices
            half_spread = market_price * self.spread / Decimal('2')
            bid_price = market_price - half_spread
            ask_price = market_price + half_spread
            
            # Place orders
            self.exchange.create_limit_buy_order(
                self.symbol,
                float(self.order_size),
                float(bid_price)
            )
            self.logger.info(f"Placed bid order: {self.order_size} @ {bid_price}")
            
            self.exchange.create_limit_sell_order(
                self.symbol,
                float(self.order_size),
                float(ask_price)
            )
            self.logger.info(f"Placed ask order: {self.order_size} @ {ask_price}")
            
        except Exception as e:
            self.logger.error(f"Error placing orders: {e}")
    
    def cancel_all_orders(self):
        try:
            self.exchange.cancel_all_orders(self.symbol)
            self.logger.info("Cancelled all existing orders")
        except Exception as e:
            self.logger.error(f"Error cancelling orders: {e}")
    
    def run(self):
        self.logger.info("Starting market maker bot...")
        
        while True:
            try:
                # Get current price
                market_price = self.get_market_price()
                if not market_price:
                    continue
                
                # Cancel existing orders
                self.cancel_all_orders()
                
                # Place new orders
                self.place_orders(market_price)
                
                # Wait before next update
                time.sleep(config['refresh_rate'])
                
            except Exception as e:
                self.logger.error(f"Error in main loop: {e}")
                time.sleep(config['refresh_rate'])

if __name__ == "__main__":
    # Create and run bot
    bot = SimpleMarketMaker(config)
    bot.run()