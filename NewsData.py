# -*- coding: utf-8 -*-

import requests, IO


def get_data():
    if IO.exists("data/update_news"):
        page = requests.get("http://www.nbcnews.com/").text
        __get_headlines(page)
        IO.delete("data/update_news")
        IO.create("data/news_done")


def __get_headlines(page):
    pages = page.split("<")
    news_storage=""
    for curr in pages:
        if curr.__contains__("item-heading item-heading_"):
            title=curr.split(">")[1]
            title = title.replace("&#x27;","'").replace("&amp;","&").strip()
            if not news_storage.__contains__(title):
                if len(title.split(" ")) < 10 and len(title.split(" ")) > 5:
                    news_storage+=title+"\n"
    IO.write("data/news", news_storage)
