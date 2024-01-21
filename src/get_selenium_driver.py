from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_selenium_driver():
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Ensures the browser window doesn't open
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # change user agent to avoid being detected as a bot
    # chrome_options.add_argument("user-agent=Mozilla/5.0 (X11; CrOS x86_64 8172.45.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.64 Safari/537.36")

    # Initialize the WebDriver with the specified options
    driver = webdriver.Chrome(options=chrome_options)

    return driver
