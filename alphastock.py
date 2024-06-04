import requests

ticker = "MSFT"
api_key = "a4da50c012254024a9186fd58a74bd3c"

def get_stock_price(ticker_symbol, api):
    url = f"https://api.twelvedata.com/price?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    if "price" in response:
        price = float(response["price"])
        return price
    else:
        raise ValueError(f"Error fetching price for {ticker_symbol}: {response.get('message', 'Unknown error')}")

def get_stock_quote(ticker_symbol, api):
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    if "name" in response:
        return response
    else:
        raise ValueError(f"Error fetching quote for {ticker_symbol}: {response.get('message', 'Unknown error')}")

try:
    stock_quote = get_stock_quote(ticker, api_key)
    stock_price = get_stock_price(ticker, api_key)
    name = stock_quote['name']
    print(f"{name}: {stock_price}")
except ValueError as e:
    print(e)