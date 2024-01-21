import asyncio
from append_affiliate_tag import append_affiliate_tag
from ask_gpt import ask_gpt
from crawl_page import crawl_page
from generate_individual_item_links import generate_individual_item_links
from preprocess_crawled_page import preprocess_crawled_page
import json
from upload_post_wp import upload_post_wp


amaozn_links_json_file_path = "a.json"


async def run(link: str):
    [product_code, html] = crawl_page(link)
    preprocessed_data = preprocess_crawled_page(html)
    print(link)

    res = await ask_gpt(preprocessed_data, link, product_code)
    if res["title"] is None:
        return
    upload_post_wp(res["title"], res["content"])


async def main():
    with open(amaozn_links_json_file_path, "r") as file:
        data = json.load(file)
        for str in data:
            print(str)
            list = generate_individual_item_links(str)
            for str2 in list:
                await run(append_affiliate_tag("https://amazon.com" + str2))


if __name__ == "__main__":
    asyncio.run(main())
