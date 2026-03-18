# ==========================================
# Job Listings Scraper Project
# Scrapes job data and saves into Excel file
# ==========================================

# Import libraries
import requests                     # Website se data lene ke liye
from bs4 import BeautifulSoup       # HTML ko readable banane ke liye
import pandas as pd                 # Excel file banane ke liye

# Website URL
url = "https://realpython.github.io/fake-jobs/"

# Send request to website
response = requests.get(url)

# Convert HTML into readable format
soup = BeautifulSoup(response.text, "html.parser")

# Find all job cards
jobs = soup.find_all("div", class_="card-content")

# Empty list to store jobs data
all_jobs = []

# Loop through each job
for job in jobs:
    
    # Extract job title
    title = job.find("h2", class_="title").text.strip()
    
    # Extract company name
    company = job.find("h3", class_="company").text.strip()
    
    # Extract location
    location = job.find("p", class_="location").text.strip()
    
    # Extract job link
    link = job.find("a")["href"]
    
    # Store data in list
    all_jobs.append([title, company, location, link])

# Convert into table format
df = pd.DataFrame(all_jobs, columns=[
    "Job Title",
    "Company",
    "Location",
    "Apply Link"
])

# Save to Excel
df.to_excel("Job_Listings_Data.xlsx", index=False)

print("✅ Job data scraped and saved successfully!")