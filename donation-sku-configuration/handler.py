from donations.app.modules.fetch_donation_titles_and_details.operations import fetch_donation_sku_details
from donations.app.modules.fetch_site_titles.operations import fetch_donation_details_by_site

def process(event, context):
    fetch_donation_details_by_site
    fetch_donation_sku_details
