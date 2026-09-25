import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://www.mediamarkt.de/de/brand/apple/iphone/iphone-18-pro"

response = requests.get(url, headers=headers)
print(f"Response status: {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all(
    "article",
    attrs={"data-test": "mms-product-card"}
)

data = []

for product in products:
    name = product.find(
        "h3",
        attrs={"data-test": "product-title"}
    )

    price_div = product.find(
        "div",
        attrs={"data-test": "mms-price"}
    )

    price = price_div.find(
        "span",
        attrs={"aria-hidden": "true"}
    ) if price_div else None

    # Add data only if both name and price are found
    if name and price:
        data.append({
            "Name": name.get_text(strip=True),
            "Price": price.get_text(strip=True)
        })

df = pd.DataFrame(data)

print(df)

# Save to an Excel file
if not df.empty:
    file_name = "iphone_prices.xlsx"
    df.to_excel(file_name, index=False)
    print(f"Data successfully saved to file: {file_name}")
else:
    print("No data found to save.")


