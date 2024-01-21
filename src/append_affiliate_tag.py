import os
from dotenv import load_dotenv

load_dotenv()


def append_affiliate_tag(url):
    tag = os.getenv("AFFILIATE_TAG")
    if "amazon.com" not in url:
        raise ValueError("URL is not an Amazon URL")

    if "?" in url:
        return url + "&tag=" + tag
    else:
        return url + "?tag=" + tag
