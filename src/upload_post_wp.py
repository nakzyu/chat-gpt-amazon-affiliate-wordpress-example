import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import os


load_dotenv()


def upload_post_wp(title: str, content: str):
    # API Endpoint
    url = "https://" + os.getenv("WP_DOMAIN") + "/wp-json/wp/v2/posts"

    # Auth
    username = os.getenv("WP_USERNAME")
    password = os.getenv("WP_PASSWORD")

    # Post data
    post = {
        "title": title,
        "content": content,
        "status": "publish",
    }

    # API Rquest
    response = requests.post(url, json=post, auth=HTTPBasicAuth(username, password))

    return response
