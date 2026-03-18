# ==========================================
# Lead Generation Scraper Project
# Extracts business contact details
# and saves them into an Excel file
# ==========================================

# Import libraries
import requests                     # Website se data lene ke liye
from bs4 import BeautifulSoup       # HTML ko readable banane ke liye
import pandas as pd                 # Excel file banane ke liye

# Practice website URL
url = "https://webscraper.io/test-sites/e-commerce/static/phones/touch"

# Send request
response = requests.get(url)

# Convert HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all business/listing cards
cards = soup.find_all("div", class_="thumbnail")

# Empty list for storing data
all_leads = []

# Loop through each card
for card in cards:
    
    # Extract company/product name
    name = card.find("a", class_="title").text.strip()
    
    # Extract price (used as contact placeholder for practice)
    price = card.find("h4", class_="price").text.strip()
    
    # Extract description (used as address/info placeholder)
    desc = card.find("p", class_="description").text.strip()
    
    # Extract product/business link
    link = "https://webscraper.io" + card.find("a", class_="title")["href"]
    
    # Store data
    all_leads.append([name, price, desc, link])

# Create table
df = pd.DataFrame(all_leads, columns=[
    "Company Name",
    "Contact / Price",
    "Address / Info",
    "Website Link"
])

# Save Excel file
df.to_excel("Business_Leads_Data.xlsx", index=False)

print("✅ Lead generation data saved successfully!")