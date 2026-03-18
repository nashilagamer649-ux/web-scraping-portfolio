# ==========================================
# Real Estate Property Scraper Project
# Scrapes property-like listing data
# and saves it into an Excel file
# ==========================================

# Import libraries
import requests                     # Website se HTML lene ke liye
from bs4 import BeautifulSoup       # HTML ko readable format me convert karne ke liye
import pandas as pd                 # Excel file banane ke liye

# Website URL (demo practice site)
url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops"

# Send request to website
response = requests.get(url)

# Convert HTML into readable format
soup = BeautifulSoup(response.text, "html.parser")

# Find all listing containers
properties = soup.find_all("div", class_="thumbnail")

# Empty list to store data
all_properties = []

# Loop through each listing
for prop in properties:
    
    # Extract property title
    title = prop.find("a", class_="title").text.strip()
    
    # Extract price
    price = prop.find("h4", class_="price").text.strip()
    
    # Extract description (used as area/details)
    description = prop.find("p", class_="description").text.strip()
    
    # Extract details link
    link = "https://webscraper.io" + prop.find("a", class_="title")["href"]
    
    # Store data in list
    all_properties.append([title, price, description, link])

# Convert into table format
df = pd.DataFrame(all_properties, columns=[
    "Property Title",
    "Price",
    "Details / Area",
    "Property Link"
])

# Save into Excel file
df.to_excel("Real_Estate_Listings.xlsx", index=False)

print("✅ Property data scraped and saved successfully!")