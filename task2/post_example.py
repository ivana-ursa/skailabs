import requests

url = 'http://127.0.0.1:5000/detect_unauthorized_sales'
json_example = {
  "productListings": [{"productID": "123", "authorizedSellerID": "A1"}, {"productID": "123", "authorizedSellerID": "A2"}, {"productID": "234", "authorizedSellerID": "A3"}],
  "salesTransactions": [{"productID": "123", "sellerID": "B2"}]
}
response = requests.post(url, json=json_example)
print(response.json())