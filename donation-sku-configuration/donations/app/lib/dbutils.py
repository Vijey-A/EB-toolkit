from pymongo import MongoClient
from donations.app.lib.constants import DEV_DB_URL

client = MongoClient(DEV_DB_URL)

source_db = client.playground_eddiebauer
destination_db = client.atomic_pim
source_collection = source_db.donation_sku
destination_collection = destination_db.productvariants