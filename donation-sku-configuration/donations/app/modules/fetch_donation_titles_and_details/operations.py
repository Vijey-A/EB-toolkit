from donations.app.lib.dbutils import source_collection

# to fetch the details from source collection and return a dictionary where the key is the title and the value is the context
def fetch_donation_sku_details():
    try:
        donation_sku_details = {}
        documents = source_collection.find()
        for document in documents:
            title = document.get('title')
            if title:
                donation_sku_details[title] = document
            else:
                print("Error: Title not found in the document.")
        return donation_sku_details
    except Exception as e:
        print(f"Error fetching donation SKU details: {str(e)}")
        return None

sku_details = fetch_donation_sku_details()
print("----------------------fetch donations TITLE and CONTEXT-----------------------")
print(sku_details)