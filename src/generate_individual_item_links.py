from get_selenium_driver import get_selenium_driver


def generate_individual_item_links(url: str):
    driver = get_selenium_driver()

    js_file_path = "gather-href-links.js"

    # Read the JavaScript file
    with open(js_file_path, "r") as file:
        js_code = file.read()

    # Open a webpage
    driver.get(url)

    # Execute the JavaScript code
    result = driver.execute_script(js_code)

    # Close the browser
    driver.quit()
    return result
