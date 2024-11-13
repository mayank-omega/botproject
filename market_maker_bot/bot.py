# bot.py
from trading_bot_class import YourTradingBotClass
from config import API_KEY, API_SECRET
from order_manager import PaperOrderManager

if __name__ == "__main__":
    # Initialize your paper trading bot
    api_client = None  # Replace with your paper trading API client if needed
    order_manager = PaperOrderManager(api_client)
    bot = YourTradingBotClass(API_KEY, API_SECRET, order_manager)
    bot.run()  # Start the trading logic``