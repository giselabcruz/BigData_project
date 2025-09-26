from crawlerModule.services.http_client import HttpClient


def link_generator(id: int | str) -> str:
    if isinstance(id, bool):
        raise TypeError("id must be an int or a numeric string (only digits)")
    if id == 0:
        raise TypeError("Id must be a positive integer greater than zero")
    if isinstance(id, int):
        if id < 0:
            raise TypeError("Id must be a positive integer greater than zero")
        iid = id
    elif isinstance(id, str) and id.isdigit():  # type: ignore
        iid = int(id)
    else:
        raise TypeError("id must be an int or a numeric string (only digits)")
    return f"https://www.gutenberg.org/cache/epub/{iid}/pg{iid}.txt"


def fetch_page_as_text(client: HttpClient, url: str) -> str:
    return client.get_as_text(url)


def fetch_page_as_json(client: HttpClient, url: str):
    return client.get_as_json(url)


def extract_current_ammount_of_books() -> int:
    url = "https://gutendex.com/books"
    client = HttpClient()
    response = fetch_page_as_json(client, url)
    return response["count"]
