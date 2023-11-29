import requests
from bs4 import BeautifulSoup
from email_sender import EmailSender  # Ensure this module/class is correctly imported

# Define request headers and the URL of the product page
header = {
    'Accept-Language': 'en-US,en;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36'
}
url = 'https://www.amazon.com/dp/B097BR2TDJ/ref=sspa_dk_detail_4?psc=1&pd_rd_i=B097BR2TDJ&pd_rd_w=tUd0m&pf_rd_p=b9951ce4-3bd8-4b04-9123-0fda35d6155e&pd_rd_wg=PT620&pf_rd_r=JYQP3N5M6NBNAGBJ06TZ&pd_rd_r=da9f1b78-8faf-4be7-97ea-3c119142937b&s=pc&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzQ0hJTUZRMFpPQTJEJmVuY3J5cHRlZElkPUEwNzY1MzIwM0dRRlA2Wko2WkZaTSZlbmNyeXB0ZWRBZElkPUExMDE0MDM0MUY3TjBRVktKM1FaVCZ3aWRnZXROYW1lPXNwX2RldGFpbCZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

# Send a GET request to the product URL with specified headers
response = requests.get(url, headers=header)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the element containing the price
price_element = soup.find(name='span', class_='apexPriceToPay')

# Check if the price element exists
if price_element:
    # Extract all span tags within the price element
    span_tags = price_element.find_all(name='span')

    # Check if enough span tags are found within the price element
    if len(span_tags) > 1:
        # Extract the text containing the price
        price = span_tags[1].getText()

        # Check if the extracted text starts with '$'
        if price.startswith('$'):
            # Convert the price to a float after removing the '$' symbol
            price = float(price[1:])

            # Specify the maximum price threshold
            max_price = 40

            # Compare the extracted price with the maximum threshold
            if price < max_price:
                # Send an email alert if the price is below the threshold
                email = EmailSender()
                msg = f'Subject: Price Drop Alert\n\nThe price is below your stipulated max value. The price is now ${price}'
                email.send(msg, 'hndzarma@gmail.com')
                print('Email sent!')
            else:
                print(f'Price (${price}) is not below the threshold of ${max_price}')
        else:
            print('Price could not be extracted properly.')
    else:
        print('The price element does not contain enough span tags.')
else:
    print('The price element was not found on the page.')
