# How to use?

### Simple!

Creating the `Chat` object:
```python
from chat import Chat

string = <KewlUsrnm> # or chat_event.message
txt = Chat(string)
```

Getting attributes:

*assuming `txt = Chat(string)`*
```python
txt.text
txt.user
txt.content
...
```

List of attributes:

*assuming `txt = Chat(string)`*
```python
text -> The entire raw text (aka string). Never None or ""
advancement -> False if not an advancement, otherwise the name of the advancement
user -> The name of the player who sent it
content -> The contents of the message
type -> The type of the message (chat, whisper, terminal, advancement)
prefix -> The prefix (first character) of the content
suffix -> The suffix (last character) of the content
timestamp -> The exact time the Chat object was created
attributes -> A list of all attributes the Chat object has. Never None or []
```

# Custom attributes:
### For when the chat is formatted differently by the server

How to:
*assuming `txt = Chat(string)`*
```python
txt.custom_attributes(template)
```

## Rules of the template:
1. It has to be a list
2. The items must be strings

