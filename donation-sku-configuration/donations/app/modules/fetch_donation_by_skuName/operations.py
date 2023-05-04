from lib.dbutils import source_collection

# to fetch a donation sku document from the "donation_sku" collection based on the sku_name
def fetch_donation_sku(sku_name):
    sku = source_collection.find_one({"sku_name": sku_name})
    if sku:
        print("SKU returned successfully")
        return sku
    else:
        print("Error: SKU not found.")
        return None