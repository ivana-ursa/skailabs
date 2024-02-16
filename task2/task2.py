from flask import Flask, request, jsonify

app = Flask(__name__)

# REST endpoint that receives a POST request and detects unauthorized sales
@app.route('/detect_unauthorized_sales', methods = ['POST'])
def detect_unauthorized_sales():
    try:
        data = request.get_json()

        # check if 'productListings' and 'salesTransactions' exist in the JSON data
        if 'productListings' not in data or 'salesTransactions' not in data:
            return jsonify({'error': 'Invalid input'}), 400
        
        product_listings = data['productListings']
        sales_transactions = data['salesTransactions']

        # check for unauthorized sales
        unauthorized_sales = check_for_unauthorized_sales(product_listings, sales_transactions)
        
        # return the result in JSON format
        return jsonify(unauthorized_sales), 200
    
    except Exception as e:
        # return the error in JSON format
        return jsonify({'error': str(e)}), 500

# function that checks for unauthorized sales
def check_for_unauthorized_sales(product_listings, sales_transactions):
    unauthorized_sales = {}
    # organize the data in a dictionary where the key is productID and the value is a list of authorizedSellerIDs
    # assumption: one productID can have multiple authorizedSellerIDs
    authorized_sellers = {listing['productID']: [] for listing in product_listings}
    for listing in product_listings:
        authorized_sellers[listing['productID']].append(listing['authorizedSellerID'])
    
    # iterate through all transactions and check if the sellerID is authorized
    for transaction in sales_transactions:
        product_id = transaction['productID']
        seller_id = transaction['sellerID']

        if product_id in authorized_sellers and seller_id not in authorized_sellers[product_id]:
            unauthorized_sales.setdefault(product_id, []).append(seller_id)
    
    # create a JSON from the unauthorized_sales dictionary
    unauthorized_sales_json = [{'productID': sale, 'unauthorizedSellerID': unauthorized_sales[sale]} for sale in unauthorized_sales]

    return {'unauthorizedSales': unauthorized_sales_json}

if __name__ == '__main__':
    app.run(debug = True) 