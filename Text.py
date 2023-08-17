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

def Italic(text: str) -> str:
    return add_tags('i', text)

def Mono(text: str) -> str:
    # return f'<pre>{text}</pre>'
    return add_tags('pre', text)

def Strikethrough(text: str) -> str:
    return add_tags('s', text)
def Underline(text: str) -> str:
    return add_tags('u', text)

def CreateLink(text: str, link: str) -> str:
    """
    Creates a hyperlink by combining the given text and link.

    Parameters:
    text (str): The text to be displayed for the hyperlink.
    link (str): The URL or link to be associated with the text.

    Returns:
    str: The formatted hyperlink.

    Example:
    >>> CreateLink('OpenAI', 'https://openai.com')
    '[OpenAI](https://openai.com)'
    """
    return f'<a href="{link}">{text}</a>'

