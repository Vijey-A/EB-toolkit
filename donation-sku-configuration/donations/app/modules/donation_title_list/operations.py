from lib.dbutils import source_collection

def fetch_donation_sku_titles():
    titles = []
    documents = source_collection.find()
    for doc in documents:
        title = doc.get('title')
        if title:
            titles.append(title)
    return titles


titles = fetch_donation_sku_titles()
# for title in titles:
#     print(title)