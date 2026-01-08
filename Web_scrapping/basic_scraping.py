'''
Step 1: Install required libraries
pip install requests beautifulsoup4
used for web scraping.
'''

# Import requests library to send HTTP requests to websites
import requests

# Import BeautifulSoup class to parse HTML content
from bs4 import BeautifulSoup

# Website URL that we want to scrape
url = "https://example.com"

# Send GET request to the website and store the response
response = requests.get(url)

# Convert the HTML content of the response into text
html_content = response.text

# Create a BeautifulSoup object to parse the HTML
soup = BeautifulSoup(html_content, "html.parser")

# Extract the title of the webpage
page_title = soup.title.text

# Print the webpage title
print("Page Title:", page_title)

# Find all paragraph (<p>) tags on the page
paragraphs = soup.find_all("p")

# Loop through each paragraph tag
for p in paragraphs:
    # Print the text inside each paragraph
    print(p.text)
    
    
    
    '''
    What This Program Teaches

Sending HTTP requests

Parsing HTML

Extracting text from tags

Basic looping

Clean beginner-friendly structure
'''



# save json and csv files

# Import requests to send HTTP requests to the website
import requests

# Import BeautifulSoup to parse HTML content
from bs4 import BeautifulSoup

# Import json module to save data in JSON format
import json

# Import csv module to save data in CSV format
import csv

# URL of the website to scrape (safe demo website)
url = "https://example.com"

# Send a GET request to the website
response = requests.get(url)

# Get HTML content from the response
html_content = response.text

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Extract the page title
title = soup.title.text

# Extract all paragraph (<p>) tags
paragraphs = soup.find_all("p")

# Create a list to store scraped data
data = []

# Loop through each paragraph tag
for p in paragraphs:
    # Append extracted data as dictionary
    data.append({
        "page_title": title,
        "paragraph": p.text.strip()
    })

# -------------------------------
# SAVE DATA TO JSON FILE
# -------------------------------

# Open a JSON file in write mode
with open("scraped_data.json", "w", encoding="utf-8") as json_file:
    # Write data to JSON file with formatting
    json.dump(data, json_file, indent=4)

# -------------------------------
# SAVE DATA TO CSV FILE
# -------------------------------

# Open a CSV file in write mode
with open("scraped_data.csv", "w", newline="", encoding="utf-8") as csv_file:
    # Define column names for CSV
    fieldnames = ["page_title", "paragraph"]
    
    # Create CSV writer object
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    # Write header row
    writer.writeheader()
    
    # Write data rows
    writer.writerows(data)

# Print success message
print("Data scraped and saved to JSON and CSV files successfully!")
