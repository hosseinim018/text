# Description
This Python module provides functions for adding markup tags to text. It can be used with other frameworks to enhance the formatting of text. The module includes functions for adding tags such as bold, italic, underline, strikethrough, and creating links. It also provides functions for adding hashtags and mentions, as well as formatting sections in INI format.
# Examples
Here are some examples of how to use the functions provided by this module:
```python
from text import Spoiler, Mono, Bold, Italic, Hashtag, Underline, CreateLink, Strikethrough,Mention, inlineMention, INIsection

tagged_text = add_tags('<b>', 'Hello, world!')
# Output: '<b>Hello, world!<b>'

spoiler_text = Spoiler('This is a spoiler')
# Output: '<tg-spoiler>This is a spoiler<tg-spoiler>'

bold_text = Bold('This is bold text')
# Output: '<b>This is bold text<b>'

italic_text = Italic('This is italic text')
# Output: '<i>This is italic text<i>'

mono_text = Mono('This is monospaced text')
# Output: '<pre>This is monospaced text<pre>'

strikethrough_text = Strikethrough('This is strikethrough text')
# Output: '<s>This is strikethrough text<s>'

underline_text = Underline('This is underlined text')
# Output: '<u>This is underlined text<u>'

link = CreateLink('OpenAI', 'https://openai.com')
# Output: '<a href="https://openai.com">OpenAI<a>'

hashtag_text = Hashtag('AI')
# Output: '#AI'

mention_text = Mention('JohnDoe')
# Output: '@JohnDoe'

inline_mention_text = inlineMention('JohnDoe', 1234)
# Output: '<a href="tg://user?id=1234">JohnDoe<a>'

ini_section = INIsection('Section1', 'This is section 1')
# Output: '[Section1]\nThis is section 1'

tags: dict[str, str] = {
    "Profile": Bold(str(Mahdi Hosseini)),
    "username": Mono(Bold(Mention(str(username)))),
    "id": Mono(Bold(str(1234556789))),
    "mention": Bold(inlineMention(Mahdi Hosseini, 123456789)),
}
text = 'This Python module provides functions for adding markup tags to text. It can be used with other frameworks to enhance the formatting of text.'
msg = INIsection('message', text)
userInfo = INIsection('userInfo', [key+': '+val for key, val in tags.items()])
msg = userInfo + '\n' + msg
# Output in telegram:
# [userInfo]
# Profile: Mahdi Hosseini
# username: @username
# id: 1234556789
# mention: Mahdi Hosseini
# [message]
# This Python module provides functions for adding markup tags to text. 
# It can be used with other frameworks to enhance the formatting of text.
```
# Note on Usage with Telegram Bot libraries
When using Telegram bot libraries to generate text, it is important to parse the text using HTML parsing mode. This is necessary in order to properly render the formatting tags. In the code snippet provided, which is part of a telethon bot, please pay attention to the usage of `await bot.send_message(event.chat_id, msg, parse_mode="html")`  
```python
@bot.on(events.NewMessage(pattern="/start"))
async def handler(event):
        user = await bot.get_entity(event.chat_id)
        tags: dict[str, str] = {
            "Profile": Bold(str(user.first_name)),
            "username": Mono(Bold(Mention(str(user.username)))),
            "id": Mono(Bold(str(event.chat_id))),
            "mention": Bold(inlineMention(user.first_name, event.chat_id)),
        }
        text = 'This Python module provides functions for adding markup tags to text. It can be used with other frameworks to enhance the formatting of text.'
        msg = INIsection('message', text)
        userInfo = INIsection('userInfo', [key+': '+val for key, val in tags.items()])
        msg = userInfo + '\n' + msg
        await bot.send_message(event.chat_id, msg, parse_mode="html")
```
# Functions
* add_tags(tag, text): Adds opening and closing tags around a text
* Bold(text): Returns text wrapped in `<b>` tags
* Italic(text): Returns text wrapped in `<i>` tags
* Mono(text): Returns text wrapped in `<pre>` tags
* Strikethrough(text): Returns text wrapped in `<s>` tags
* Underline(text): Returns text wrapped in `<u>` tags
* CreateLink(text, link): Returns text as a hyperlink
* Hashtag(text): Returns text prefixed with `#`
* Mention(text): Returns text prefixed with `@`
* inlineMention(text, id): Returns text as inline mention with id
* INIsection(section, description): Returns formatted INI section

# Contributing
If you would like to contribute to this project, please feel free to submit a pull request. Make sure to follow the coding style and include tests for any new functionality.

# License
This module is licensed under the MIT License.
