# browserstack-elpais-assignment
# BrowserStack - ElPais Articles Load Test

This repository contains the solution for the technical assignment given by the BrowserStack Customer Engineering team.

The project demonstrates the use of:
- Web scraping using **Selenium**
- **Translation API** usage
- **Text analysis**
- Execution on **BrowserStack Automate** across multiple browsers and devices



##  Tech Stack

- **Language:** Python 3
- **Automation:** Selenium WebDriver
- **Translation API:**  Google Translate
- **Browsers/Devices:** Chrome (Windows 11), Safari (macOS Monterey), Edge (Windows 10), Samsung Galaxy S22 (Android), iPhone 14 (iOS)



##  Features

- Scrapes the first 5 articles from the [El País Opinion Section](https://elpais.com/opinion/)
- Prints article **title and content** (in Spanish)
- Downloads **cover image** if available
- Translates titles to **English**
- Identifies **repeated words** across translated headers
- Runs test on **5 parallel browser sessions** on BrowserStack



##  Links

-  **BrowserStack Automate Build:** [View Build](https://automate.browserstack.com/projects/Default+Project/builds/ElPais+Articles+Load/2?tab=tests&testListView=spec)
-  **Screenshot of Build Running:** [Google Drive Screenshot](https://drive.google.com/file/d/1S0ia8RUdg0g9dJ2ez9fzNWbuMlMaX9gz/view?usp=sharing)


##  How to Run Locally

###  Install Dependencies


pip install -r requirements.txt
