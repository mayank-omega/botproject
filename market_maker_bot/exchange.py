import requests

class ExchangeAPI:
    def __init__(self, api_key, api_secret, base_url='https://api.example.com'):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url

    def _create_headers(self):
        # Create headers for the API requests
        return {
            'Content-Type': 'application/json',
            'X-API-Key': self.api_key,
            # You may need to include other headers like signature, etc.
        }

    def get_market_data(self, symbol):
        """Fetch market data for a given symbol."""
        url = f"{self.base_url}/market_data/{symbol}"
        response = requests.get(url, headers=self._create_headers())
        if response.status_code == 200:
            return response.json()  # Return the market data as a dictionary
        else:
            raise Exception(f"Error fetching market data: {response.text}")

    def place_order(self, symbol, quantity, order_type='market'):
        """Place an order for a given symbol."""
        url = f"{self.base_url}/orders"
        order_data = {
            'symbol': symbol,
            'quantity': quantity,
            'order_type': order_type
        }
        response = requests.post(url, json=order_data, headers=self._create_headers())
        if response.status_code == 201:
            return response.json()  # Return the order details as a dictionary
        else:
            raise Exception(f"Error placing order: {response.text}")

    def get_account_balance(self):
        """Fetch the account balance."""
        url = f"{self.base_url}/account/balance"
        response = requests.get(url, headers=self._create_headers())
        if response.status_code == 200:
            return response.json()  # Return the account balance as a dictionary
        else:
            raise Exception(f"Error fetching account balance: {response.text}")

    def get_open_orders(self):
        """Fetch all open orders."""
        url = f"{self.base_url}/orders/open"
        response = requests.get(url, headers=self._create_headers())
        if response.status_code == 200:
            return response.json()  # Return the open orders as a list
        else:
            raise Exception(f"Error fetching open orders: {response.text}")

    def cancel_order(self, order_id):
        """Cancel an order by its ID."""
        url = f"{self.base_url}/orders/{order_id}/cancel"
        response = requests.post(url, headers=self._create_headers())
        if response.status_code == 200:
            return response.json()  # Return cancellation confirmation
        else:
            raise Exception(f"Error cancelling order: {response.text}")

# Example usage
if __name__ == "__main__":
    # Example of how to use the ExchangeAPI class
    api_key = 'your_api_key'
    api_secret = 'your_api_secret'
    exchange = ExchangeAPI(api_key, api_secret)

    try:
        market_data = exchange.get_market_data('BTCUSD')
        print("Market Data:", market_data)

        order_response = exchange.place_order('BTCUSD', 1)
        print("Order Response:", order_response)

        balance = exchange.get_account_balance()
        print("Account Balance:", balance)

        open_orders = exchange.get_open_orders()
        print("Open Orders:", open_orders)

    except Exception as e:
        print("An error occurred:", e)