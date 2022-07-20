import requests # If not available, install it

r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

# Response of the URL
print(r.status_code)

# Print the Headers
print(r.headers)

# To get the encoding
print(r.encoding)

# To get the actual text
actual_content = r.text
print(actual_content)

# Find the bitcoin price now!
data = r.json() # Converting the entire to JSON format, easy to process

# Parsing through the JSON data to get the USD rate of bitcoin
bitcoin_price = data["bpi"]["USD"]["rate"]

# Remove the , symbol from the value
bitcoin_price = bitcoin_price.replace(',','')

# Convert to float, so we can round it off later
bitcoin_price = float(bitcoin_price)

# Round off the value for 2 digits
bitcoin_price = round(bitcoin_price, 2)

# Printing the value to the user
print(f"The price of bitcoin right now is: ${bitcoin_price}")