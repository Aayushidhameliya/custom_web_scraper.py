import os
import requests
from bs4 import BeautifulSoup

def scrape_products(html_file_path):
    try:
        # Load the HTML file
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()

        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        # Locate the elements containing the data you want
        products = []
        for product in soup.find_all('div', class_='product'):
            # Extract relevant information (e.g., name, price, description)
            name = product.find('h2', class_='product-name').text.strip()
            price = product.find('span', class_='product-price').text.strip()
            description = product.find('p', class_='product-description').text.strip()

            # Store the data in a dictionary
            products.append({
                'name': name,
                'price': price,
                'description': description
            })

        return products

    except FileNotFoundError:
        print(f"Error: File '{html_file_path}' not found.")
        return None

# Example usage:
if __name__ == "__main__":
    # Get the directory path of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the HTML file (assuming index.html is in the same directory)
    html_file_path = os.path.join(script_dir, 'index.html')

    products = scrape_products(html_file_path)
    if products:
        for product in products:
            print(product)
    else:
        print("Failed to retrieve product data.")
