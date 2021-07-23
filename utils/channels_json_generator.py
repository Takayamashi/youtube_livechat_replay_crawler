from bs4 import BeautifulSoup
import requests
import json
import sys


def main():
    url = 'https://comment2434.com/comment/'
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    options = soup.find_all("option")
    channel_list = []

    for option in options:
        channel = {"channel_id": option.get("value"),
                   "name": option.get_text()}
        channel_list.append(channel)

    with open('./data/channels.json', 'w') as f:
        json.dump({"channel_list": channel_list},
                  f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
