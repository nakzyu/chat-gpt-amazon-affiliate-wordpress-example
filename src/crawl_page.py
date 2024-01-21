from bs4 import BeautifulSoup
from get_selenium_driver import get_selenium_driver


def crawl_page(url: str):
    driver = get_selenium_driver()

    # Navigate to the URL
    driver.get(url)

    # Perform any interactions or get page source
    page_source = driver.page_source
    driver.quit()
    soup = BeautifulSoup(page_source, "html.parser")

    return [soup.find("h1").text, soup.get_text(strip=True)]
