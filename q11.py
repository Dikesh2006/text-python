import requests
from bs4 import BeautifulSoup
import json

try:
    
    url = "http://quotes.toscrape.com"

   
    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, "html.parser")

        quotes_data = []

       
        quotes = soup.find_all("div", class_="quote")

        print("Albert Einstein Quotes:")
        print("-" * 50)

        for quote in quotes:
            text = quote.find("span", class_="text").get_text()
            author = quote.find("small", class_="author").get_text()

            quotes_data.append({
                "quote": text,
                "author": author
            })

           
            if author == "Albert Einstein":
                print(text)

        
        with open("quotes.json", "w") as file:
            json.dump(quotes_data, file, indent=4)

        print("\nTotal Quotes Scraped:", len(quotes_data))
        print("All quotes saved to quotes.json")

    else:
        print("Failed to access website!")

except Exception as e:
    print("Error:", e)

finally:
    print("Scraping Completed!")