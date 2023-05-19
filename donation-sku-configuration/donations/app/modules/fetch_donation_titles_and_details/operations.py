# # to fetch the details from source collection and return a dictionary where the key is the title and the value is the context
from donations.app.lib.dbutils import find

def process(db_url: str):
    try:
        donation_sku_details = {}
        documents = find({}, db_url, "playground_eddiebauer", "donation_sku")
        for document in documents:
            title = document.get('title')
            if title:
                donation_sku_details[title] = document
            else:
                print("Error: Title not found in the document.")
        return {
            "message": donation_sku_details,
            "status_code": 200
        }
    except Exception as e:
        print(f"Error fetching donation SKU details: {str(e)}")
        return {"message": "Internal server error", "status_code": 500}