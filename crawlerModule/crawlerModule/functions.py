def link_generator(id):
    if isinstance(id, bool):
        raise TypeError("id must be an int or a numeric string (only digits)")
    if isinstance(id, int):
        iid = id
    elif isinstance(id, str) and id.isdigit():
        iid = int(id)
    else:
        raise TypeError("id must be an int or a numeric string (only digits)")
    return f"https://www.gutenberg.org/cache/epub/{iid}/pg{iid}.txt"
