from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import requests
from bs4 import BeautifulSoup
import os
from translate import Translator
from collections import Counter
import re

article_urls = [
    "https://elpais.com/opinion/2025-08-05/mazon-y-la-nada.html",
    "https://elpais.com/opinion/2025-08-05/trump-despide-al-mensajero.html",
    "https://elpais.com/opinion/2025-08-05/migrantes-somos-todos.html",
    "https://elpais.com/opinion/2025-08-05/hacerse-el-fuerte-hacerse-el-debil.html",
    "https://elpais.com/opinion/2025-08-05/nepoliticos.html"
]

os.makedirs("cover_images", exist_ok=True)

# Set your ChromeDriver path
service = Service("C:/Users/Anusha/Downloads/chromedriver-win64/chromedriver-win64/chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument("--headless")
driver = webdriver.Chrome(service=service, options=options)

spanish_titles = []

# Scraping logic

for i, url in enumerate(article_urls, 1):
    driver.get(url)
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")

    title_tag = soup.find("h1")
    title = title_tag.text.strip() if title_tag else "No title found"
    spanish_titles.append(title)

    content_tags = soup.find_all("p")
    content = "\n".join(p.text.strip() for p in content_tags if p.text.strip())

    img_tag = soup.find("img")
    if img_tag and img_tag.get("src"):
        img_url = img_tag["src"]
        try:
            img_data = requests.get(img_url).content
            with open(f"cover_images/article_{i}.jpg", "wb") as f:
                f.write(img_data)
            image_status = f"Image saved: cover_images/article_{i}.jpg"
        except:
            image_status = "Failed to download image"
    else:
        image_status = "No image found"

    print(f"\n--- ARTICLE {i} ---")
    print(f"Title: {title}")
    print(f"Content (first 300 chars): {content[:300]}...")
    print(image_status)

driver.quit()


# Translation Step

print("\n=== TRANSLATED TITLES (via MyMemory) ===")
translator = Translator(from_lang="es", to_lang="en")
translated_titles = []

for title in spanish_titles:
    try:
        translated = translator.translate(title)
        translated_titles.append(translated)
        print(f"Spanish: {title}")
        print(f"English: {translated}\n")
    except Exception as e:
        print(f" Error translating: {title}")
        print(f"Error: {e}\n")


# Word Frequency Analysis

print("\n=== REPEATED WORDS IN TRANSLATED TITLES (more than 2 times) ===")
all_words = " ".join(translated_titles).lower()
words = re.findall(r'\b\w+\b', all_words)
word_counts = Counter(words)

for word, count in word_counts.items():
    if count > 2:
        print(f"{word}: {count}")
