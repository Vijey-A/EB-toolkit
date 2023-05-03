from lib.dbutils import source_collection

# to add a new donation sku document to the "donation_sku" collection
def add_donation(content, image, sku_name, title):
    sku = source_collection.find_one({"sku_name": sku_name})
    if sku:
        print("Error: SKU name already exists.")
    else:
        source_collection.insert_one({ "content": content, "image": image,"sku_name": sku_name, "title": title})
        print("Donation SKU added successfully.")

# to manually add the elements,
def add_donation_runtime():
    sku_name = input("Enter SKU name: ")
    title = input("Enter title: ")
    content = input("Enter content: ")
    image = input("Enter image path: ")
    document = {
        "content": content,
        "image": image,
        "skuName": sku_name,
        "title": title,
    }
    source_collection.insert_one(document)
    print("Donation SKU added successfully.")