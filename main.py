from bs4 import BeautifulSoup
import requests
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials securely
my_email = os.getenv("EMAIL_ADDRESS")
rec_email = os.getenv("RECIPIENT_EMAIL")
password = os.getenv("EMAIL_PASSWORD")
smtp_server = os.getenv("SMTP_ADDRESS")

# Amazon product URL # enter any product url on amazon from your choice
url = "https://www.amazon.com/Microsoft-Xbox-512GB-SSD-Console-S/dp/B0D932YWSZ/"

# Headers to mimic a real browser request
headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

# Send request
response = requests.get(url, headers=headers)

# Parse HTML
soup = BeautifulSoup(response.content, "html.parser")

# Get product title
title_element = soup.find(id="productTitle")
title = title_element.get_text().strip() if title_element else "Unknown Product"

# Get price
price_element = soup.find(class_="a-offscreen")
if price_element:
    price_text = price_element.get_text().strip()
    try:
        price_as_float = float(price_text.replace("$", "").replace(",", ""))
    except ValueError:
        print("Error: Could not parse price.")
        price_as_float = None
else:
    print("Error: Price not found.")
    price_as_float = None

# Set the price threshold for notifications
BUY_PRICE = 290.00

# Check if price is below threshold and send an email
if price_as_float and price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price_text}!\n\nCheck it out here: {url}"

    try:
        with smtplib.SMTP(smtp_server, port=587) as connection:
            connection.starttls()
            connection.login(my_email, password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=rec_email,
                msg=f"Subject: Amazon Price Alert!\n\n{message}".encode("utf-8")
            )
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
else:
    print(f"Price is still above {BUY_PRICE}: {price_as_float}")
