from lib.dbutils import source_collection
from lib.dbutils import destination_collection

# to update the "product_variant" document in "atomic_pim" database based on "com", "ca", and "outlet".
def replace_document():
    title = input("Enter the 'title' of the document to be replaced from(title field of the document) : ")
    target_key = input("Enter the target key (com, ca, or outlet-com) where the document should be replaced: ")
    document = source_collection.find_one({"title": title})
    if document:
        destination_document = destination_collection.find_one({"productVariantId": "sku30042"})
        if destination_document:
            destination_document['donationDetails'][target_key] = document
            destination_collection.replace_one({"productVariantId": "sku30042"}, destination_document)
            print("Document Updated successfully.")
        else:
            print("No document found in the 'atomic_pim' collection where productVariantId = 'sku30042'")
    else:
        print(f"No document found with the TITLE {title} in the 'donation_sku' collection")