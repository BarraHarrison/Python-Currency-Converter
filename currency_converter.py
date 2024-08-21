import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def get_conversion_rate(api_key, from_currency, to_currency):
    url = f"https://api.freecurrencyapi.com/v1/latest?apikey={api_key}&currencies={to_currency}&base_currency={from_currency}"
    response = requests.get(url)
    data = response.json()
    
    if 'data' in data and to_currency in data['data']:
        return data['data'][to_currency]
    else:
        print("Currency not found!")
        return None

def currency_converter():
    api_key = os.getenv('CURRENCY_API_KEY')  # Load API key from environment variable
    if not api_key:
        print("API key not found. Please set the CURRENCY_API_KEY environment variable.")
        return
    
    amount = float(input("Enter the amount of currency you want to convert: "))
    from_currency = input("Enter the currency you are converting from (e.g., USD): ").upper()
    to_currency = input("Enter the currency you are converting to (e.g., EUR): ").upper()
    
    rate = get_conversion_rate(api_key, from_currency, to_currency)
    
    if rate:
        converted_amount = amount * rate
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")

# Run the currency converter
currency_converter()
