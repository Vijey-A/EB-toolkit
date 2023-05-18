from donations.app.lib.dbutils import destination_collection

# in a doctionary where the key is the "Sites" string and the value is where there is only three key "com","ca"and "outlet-com" and the value is donationDetails" field "com","ca","outlet-com" key 
# which is to be fetched from destination_collection where "productVariantId:'sku30042'"
def fetch_donationDetails_sites():
    try:
        donation_details = {}
        product_variant = destination_collection.find_one({'productVariantId': 'sku30042'})
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
            return donation_details_by_site
        else:
            raise ValueError("product_variant does not exist or does not contain the 'donationDetails' field")
    except Exception as e:
        print(f"Error fetching donation details by site: {str(e)}")
        return None
donation_details_by_site = fetch_donationDetails_sites()
print("----------------------GET SITE TITLES-----------------------")
print (donation_details_by_site)