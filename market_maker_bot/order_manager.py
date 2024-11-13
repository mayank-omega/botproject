# order_manager.py
class OrderManager:
    def __init__(self, api_client):
        self.api_client = api_client

    def place_order(self, symbol, quantity, order_type='market'):
        # Code to place an order using the real API
        pass

class PaperOrderManager(OrderManager):
    def place_order(self, symbol, quantity, order_type='market'):
        print(f"Simulated order placed: {order_type} {quantity} of {symbol}")
        return {'success': True, 'symbol': symbol, 'quantity': quantity}