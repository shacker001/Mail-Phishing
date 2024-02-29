import re
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta
from tld import get_tld
from tld.exceptions import TldDomainNotFound
from email.header import decode_header
import ssl
from sklearn.features_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Function to extract features from a URL
def extract_url_features(url):
    parsed_url = urlparse(url)
    url_length = len(url)
    domain_age = get_domain_age(parsed_url.netloc)
    return [url_length, domain_age]

# Function to get domain age
def get_domain_age(domain):
    try: 
        creation_date = get_tld(f"http://www.{domain}", as_object=True).creation_date
        if creation_date:
            age = (datetime.now() - creation_date).days
            return age
    except TldDomainNotFound:
        pass
    return None

# Function to check URL against a blacklist
def is_blacklisted(url):
    # Implement your blacklist checking logic here
    return False

# Function to analyze email content using a simple Naive Bayes classifier
def is_phishing_email(email_content):
    model = make_pipeline(CountVectorizer(), MultinomialNB())

    # Train the model with your phishing and non-phishing emaildatasets

    # For simplicity, you've trained your model
    trained_mmodel = train_model() # Implement this function
    return trained_mmodel.predict([email_content])[0]

# Function to check SSL/TLS certificate validity
def is_valid_certificate(url):
    try:
        ssl_info = ssl.get_server_certificate(urlparse(url).hostname, 443) # Implement your SSL/TLS certificate validation logic here
        return True #Replace with actual validation

    except Exception as e:
        return False

# Functio to analyze webpage content for phishing elements
def analyze_webpage_content(html_content):
    soup = BeautifulSoup(html_content,'html.parser')
    # Emplement your content analysis logoc here
    # Check for phoshing elements in the THML like fake forms, logos, etc.
    return False     # Replace with actual analysis

# Example usage
url_to_check = "http://example.com"
email_content_to_check = "Suspicious email content here"
html_content_to_check = requests.get(url_to_check).text

# URL Analysis
url_features = extract_url_features(url_to_check)
if is_blacklisted(url_to_check):
    print("URL is blacklisted!")

# Email Analysis
if is_phishing_email(email_content_to_check):
    print("Phishing email detected!")

# SSL/TLS Certificate check
if is_valid_certificate(url_to_check):
    print("Valid SSL/TLS Certificate!")

else:
    print("Invalid SSL/TLS certificate or unable to check.")

# Content inspection
if analyze_webpage_content(html_content_to_check):
    print("Phishig elements detected in the webpage!")