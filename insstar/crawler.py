# -*- coding: UTF-8 -*-
from insstar.cursor_page import get_page_by_cursor
from insstar.save_db import down_index, down_page
from insstar.image import down_pic

def single_crawler(cursor):
    data = get_page_by_cursor(cursor)
    print(data)
    next = down_index(data)
    if data.get("top_posts"):
        down_page(data["id"], data["top_posts"])
    return next

def insstar_crawler():
    next = "212927650"
    while next:
        next = single_crawler(next)
        if not isinstance(next, str):
            next = str(next)
        print("next: ", next)
