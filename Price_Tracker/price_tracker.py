# ================================
# E-commerce Price Tracker Project
# Scrapes book data from multiple pages
# and saves it into an Excel file
# ================================

# Import required libraries
import requests                     # Website se HTML lene ke liye
from bs4 import BeautifulSoup       # HTML ko readable format me convert karne ke liye
import pandas as pd                 # Data ko Excel me save karne ke liye

# Empty list to store all books data
all_books = []

# Loop through multiple pages (1 se 5 tak)
for page in range(1, 6):

    # Website URL (page number automatically change hoga)
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    
    # Send request to website
    response = requests.get(url)
    
    # Convert HTML into readable format
    soup = BeautifulSoup(response.text, "html.parser")
    
    # Find all book containers
    books = soup.find_all("article", class_="product_pod")
    
    # Loop through each book
    for book in books:
        
        # Extract book name
        name = book.h3.a["title"]
        
        # Extract price and remove currency symbol
        price = book.find("p", class_="price_color").text.replace("£", "")
        
        # Extract rating (stored as class name)
        rating = book.p["class"][1]
        
        # Append data into list
        all_books.append([name, price, rating])


# Create DataFrame (table format)
df = pd.DataFrame(all_books, columns=["Book Name", "Price (£)", "Rating"])

# Save data to Excel file
df.to_excel("Book_Price_Data.xlsx", index=False)

print("✅ Scraping completed! Excel file saved successfully.")