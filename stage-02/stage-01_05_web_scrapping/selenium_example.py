from selenium import webdriver
from selenium.webdriver.common.by import By
import time


url = "https://quotes.toscrape.com/"


driver = webdriver.Chrome()


try:

    driver.get(url)

    time.sleep(2)


    print("=== Browser Information ===")

    print("Page Title:", driver.title)

    print("Current URL:", driver.current_url)



    quotes = driver.find_elements(
        By.CLASS_NAME,
        "text"
    )


    print("\n=== Quotes ===")

    for quote in quotes:

        print(quote.text)


finally:

    driver.quit()