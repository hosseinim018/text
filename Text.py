from typing import Union, List

def add_tags(tag: str, text: str) -> str:
    """
    Adds a specified tag at the start and end of the given text.

    Parameters:
    tag (str): The tag to be added. It should be a string.
    text (str): The text to be tagged. It should be a string.

    Returns:
    str: The tagged text, with the specified tag added at the start and end.

    Example:
    >>> add_tags('<i>', 'Python')
    '<i>Python<i>'
    """
    return f"<{tag}>{text}</{tag}>"

def Spoiler(text: str) -> str:
    return add_tags('tg-spoiler', text)

def Bold(text: str) -> str:
    return add_tags('b', text)
