
from lib.dbutils import destination_collection

def fetch_donation_details():
    document = destination_collection.find_one({"productVariantId": "sku30042"})
    donation_details = document.get('donationDetails', {})
    com_data = donation_details.get('com')
    ca_data = donation_details.get('ca')
    outlet_data = donation_details.get('outlet-com')
    return com_data, ca_data, outlet_data

# com, ca, outlet = fetch_donation_details()
# print("COM Data:")
# print(com)
# print("CA Data:")
# print(ca)
# print("Outlet Data:")
# print(outlet)
