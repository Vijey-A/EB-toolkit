from donations.app.lib.dbutils import find

# in a doctionary where the key is the "Sites" string and the value is where there is only three key "com","ca"and "outlet-com" and the value is donationDetails" field "com","ca","outlet-com" key 
# which is to be fetched from destination_collection where "productVariantId:'sku30042'"
def process(db_url: str):
    try:
        donation_details = {}
        product_variant = find({'productVariantId': 'sku30042'}, db_url, "atomic_pim", "productvariants")
        if product_variant and 'donationDetails' in product_variant:
            donation_details = product_variant['donationDetails']
            for keys in donation_details.items():
                for i in keys:
                    if i == 'com':
                        com_key = i
                    elif i == 'outlet-com':
                        ca_key = i
                    elif i == 'ca':
                        outlet_key = i
            donation_details_by_site = {'Sites': {'com': com_key, 'outlet-com': ca_key, 'ca': outlet_key}}
            return {
            "message": donation_details_by_site,
            "status_code": 200
        }
        else:
            raise ValueError("product_variant does not exist or does not contain the 'donationDetails' field")
    except Exception as e:
        print(f"Error fetching donation details by site: {str(e)}")
        return {"message": "Internal server error", "status_code": 500}