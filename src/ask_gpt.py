from openai import OpenAI
from dotenv import load_dotenv
import json

load_dotenv()

client = OpenAI()


def build_promt(product_code: str, tokens: str):
    type_of_content = (
        "Analyze the text, and give a specifications of the product in English."
    )
    result_should_be_json = "Please format it in JSON with 'title' and 'content' sections. it should be valid json format."
    add_keywords_for_seo = "and it should include nice keywords for seo."
    content_must_be_html = "and content must be written in html format."

    ############################### IMPORTANT #########################################
    # According to Amazon Affiliate rules, care must be taken when displaying product information:
    # 1. Do not include any customer reviews. Including these may violate Amazon's customer review policies.
    # 2. Never include product pricing information. As per Amazon's pricing policy, showing prices can be a violation due to potential discrepancies with real-time price fluctuations.
    do_not_include_customer_reviews = "be sure not to include any customer's reviews."
    do_not_include_price = "and never include product price."
    ############################### IMPORTANT #########################################

    do_include_product_code = " and product code should always have to be included. and never mention Amazon. product code is "
    declare_token_entry = "----- rest text is here:"

    prompts = [
        type_of_content,
        result_should_be_json,
        add_keywords_for_seo,
        content_must_be_html,
        do_not_include_customer_reviews,
        do_not_include_price,
        do_include_product_code,
        product_code,
        declare_token_entry,
        tokens,
    ]

    return " ".join(prompts)


async def ask_gpt(str: str, link: str, product_code: str):
    res = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": build_promt(product_code, str),
            }
        ],
    )

    text = res.choices[0].message.content

    try:
        data = json.loads(text)

        product_link = (
            "<p>As an Amazon Associate, I earn from qualifying purchases made through this link, at no extra cost to you.</p><h4><a href="
            + link
            + ">Discover More About This Product</a></h4>"
        )
        return {
            "title": data["title"],
            "content": data["content"] + product_link,
        }
    except:
        return {
            "title": None,
            "content": None,
        }
