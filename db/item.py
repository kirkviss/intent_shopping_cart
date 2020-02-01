import json
import os
from functools import lru_cache
# pull all the content from the json file and then convert it to a json object
def getAllItems():
    with open ( f'{os.path.dirname(os.path.abspath(__file__))}/items.json', 'r') as cartFile:
        return json.loads(cartFile.read())

@lru_cache(maxsize=None)
def getItem(itemId):
    items = getAllItems()
    for item in items:
        if item['id'] == itemId:
            return item
    return None
