from pprint import pprint
from typing import Optional

from notion_client import Client
from notion_client.errors import APIResponseError
from collections import namedtuple

API_TOKEN = "secret_YDI7evb9vJGHG46JMalnuy9FoC3cGCQ9FK3xzVQ0RbF"
DATABASE_ID = "fdd0105ce747400cbb80c1be62fa1cee"
notion = Client(auth=API_TOKEN)
ToDoItem = namedtuple("ToDoItem", "title")


def column_exists(column: str) -> bool:
    response = notion.databases.retrieve(database_id=DATABASE_ID)
    options = response['properties']['Status']['select']['options']
    column_names = [option['name'] for option in options]
    return column in column_names


def get_db_column(column: str) -> list[ToDoItem]:
    if not column_exists(column):
        raise KeyError(f"Column '{column}' does not exist in the db")
    response = notion.databases.query(database_id=DATABASE_ID, **{"filter": {"property": "Status", "select": {"equals": column}}})
    return [ToDoItem(page['properties']['Name']['title'][0]['plain_text']) for page in response["results"]]
