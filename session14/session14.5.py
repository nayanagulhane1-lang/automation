# <!-- #Use ChatGPT or Copilot to help you write a list comprehension that, given a list of product names from Flipkart, returns a new list with the names in uppercase but only if the name is longer than 6 characters. Paste your prompt and the AI's suggested code along with your final working code. -->

products = ["Laptop", "Mobile", "Headphones", "Keyboard", "Mouse"]

uppercase_products = [product.upper() for product in products if len(product) > 6]

print(uppercase_products)