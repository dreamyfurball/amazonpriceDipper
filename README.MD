# 📉 Amazon Price Dipper 🛒

## 🎯 Why I Built This
This project was created to explore **web scraping, automation, and email notifications**.  
It simulates **real-world software applications** by integrating API calls, automated tracking,  
and notifications—all crucial skills in modern software development.

Through this project, I learned:
- How to use `BeautifulSoup` for web scraping
- How to handle HTTP requests with `requests`
- How to automate emails using `smtplib`
- How to store credentials securely using `.env`

A Python script that tracks the price of a product on Amazon and **sends an email notification** when the price drops below a set threshold.

## 🚀 Features
✅ Scrapes Amazon for product prices  
✅ Sends **email alerts** when the price drops  
✅ Uses `BeautifulSoup` for web scraping  
✅ Secure **.env** file for storing credentials  

## 🔧 Setup Instructions

### 1️⃣ Clone This Repository

git clone https://github.com/dreamyfurball/amazonpriceDipper.git
cd amazonpriceDipper


# Want To use it ?

## 📧 Sender & Recipient Email Setup

This script requires **two email addresses**:
1️⃣ **Sender Email** – The email that sends the price alert (Must be a Gmail account)  
2️⃣ **Recipient Email** – The email that receives the price alert (Can be any email: Gmail, Yahoo, Outlook, etc.)

### **🔧 How to Set Up Sender & Recipient Emails**
1. **Use a Gmail account as the sender** (email that sends alerts).
   - You must generate an **App Password** for this sender email.  
   - Follow the [App Password setup guide](https://myaccount.google.com/apppasswords).
   
2. **The recipient email can be any valid email.**
   - If you want alerts sent to yourself, use your **personal email** as the recipient.
   - If you want to send alerts to multiple emails, modify the `to_addrs` field in the script.

3. **Update Your `.env` File**  
   Add both emails inside your `.env` file:






