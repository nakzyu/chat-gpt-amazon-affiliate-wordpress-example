## Purpose

This example demonstrates a method that combines Chat GPT API, WordPress information, and your Amazon Affiliate link ID to automatically post content.

## How to Use

### 1. Create a .env file and fill it with the following details:

- `OPENAI_API_KEY`
  - Your API key for Chat GPT, obtainable from OPENAI.
- `AFFILIATE_TAG`
  - Your key issued from the Amazon Affiliate site.
- `WP_USERNAME`
  - Username for WordPress API requests.
- `WP_PASSWORD`
  - Password for the user for WordPress API requests.
- `WP_DOMAIN`
  - Your WordPress domain.

### 2. Create a file named `a.json` and insert links to Amazon product lists, not individual product detail pages.

Example:

```json
[
  "https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A172541&page=6&qid=1705632068&ref=sr_pg_2",
  "https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A172541&page=7&qid=1705632068&ref=sr_pg_2",
  "https://www.amazon.com/s?i=electronics-intl-ship&bbn=16225009011&rh=n%3A16225009011%2Cn%3A172541&page=8&qid=1705632068&ref=sr_pg_2"
]
```

### 3. Install packages with `pip install -r requirements.txt` and Run with `python ./src/main.py`
