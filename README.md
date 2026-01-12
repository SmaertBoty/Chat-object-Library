# How to use?

### Simple!

Creating the `Chat` object:
```py
from chat import Chat

string = "<KewlUsrnm>" # or chat_event.message
txt = Chat(string)
```

Getting attributes:

*assuming `txt = Chat(string)`*
```py
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
type -> The type of the message (chat, whisper, terminal, advancement, death)
prefix -> The prefix (first character) of the content
suffix -> The suffix (last character) of the content
timestamp -> The exact time the Chat object was created
attributes -> A list of all attributes the Chat object has. Never None or []
words -> All the words of "content" as a list
custom -> Wether the object was created with custom attributes (True) or not (False)
causer -> The player / entity who caused the death (only for death messages)
reason -> The reason the player / entity died (only for death messages)
item -> The item that caused the death (only for death messages)
```

# Custom attributes:
### For when the chat is formatted differently by the server

How to:

*assuming `txt = Chat(string)`*
```py
txt.custom_attributes(template)
```

## Rules of the template:
1. It has to be a list
2. The items must be strings

### What does the template do?
It tells the script, what slice of the text, is what attribute.

It looks at each item of the provided list, and gets their prefix, and suffix.

Then, it searches the text, for that prefix and suffix, and gets everything inbetween them (excludes the prefix, and suffix)
```python
template = "<custom_attribute>" # A TEMPLATE MUST BE A LIST, THIS IS JUST A PLACEHOLDER
string = "<KewlUsrnm>"
txt.custom_attribute -> KewlUsrnm
```
Almost any* character can be used as prefix and suffix
```python
<> ✓
[] ✓
" " (space) and " " (space) ✓
G= ✓
15 ✓
** ✕
```
### PATTERNS CANNOT SHARE CHARACTERS
### ALL UNMATCHED CHRACTERS WILL BE SKIPPED
*Except `*` (asterisk aka star)

The `*` signs functionality is based on if its a prefix, or suffix:
1. If its a prefix, it represents an "" (empty) string. Usefull when the text has no prefix
2. If its a suffix, it represents "everything from now on". Usefull specifically for "content" attribute
```python
string = "hello world blah blah blah"
template = ["*word1 "," word2 "] -> word1 = "hello" ; word2 -> None (they share a space)
template = ["word1 ","*word2 "] -> word1 = Not an attribute (the "w" gets used up for the search, thus making the attribute be called "ord1". ord1 -> "orld") ; word2 -> "blah"
template = ["*word1 ","*words*"] -> word1 = "hello" ; words = "world blah blah blah"
```
### What if there are multiple objects with the same prefix and suffix?
```py
string = "[One] [Two]"
template = ["[two]"] -> two = "One" (The " " (space) is not matched)
# use a dummy attribute
template = ["[dummy]","[two]"] -> two = "Two" (The " " (space) is not matched)
```

### Helper functions
```py
.strip() -> remove all attributes except text and custom
.remove_prefix() -> Remove the prefix from content and words, if its not custom
```

# Example usage:
```py
# Basic example:
string = "<KewlUsrnm> hello guys!"
txt = Chat(string)
print(txt.user)
print(txt.content)

# Custom attribute example:
string = "[239] VIP <KewlUsrnm> hello guys"
template = ["[level]"," rank ","<user>"," content*"]
txt = Chat(string).custom_attributes(template)

print(txt.rank)
print(txt.content)
```
