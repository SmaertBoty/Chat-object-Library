# Usage:

msg = Chat("<KewlUsrnm> This is a message sent to the public chat!")

msg = Chat("[KewlUsrnm] This is a message sent to the public chat! But with different brackets!")

msg = Chat("KewlUsrnm whisperes to you: This is a private message!"")

msg = Chat("KewlUsrnm made the advancement [This is an advancement]")

msg = Chat("KewlUsrnm this is a message sent by the server!)


## Realistic usage:

msg = Chat(chat_event.message)


# Attributes:

msg.text -> the whole raw text

print(msg.user) -> the username in the message (server if None)

print(msg.type) -> the type of the message ("chat" for the public chat, "whisper" for whispers, "advancement" for advancements, "terminal" for server messages)

print(msg.content) -> the content of the message (without the user and type)

print(msg.advancement) -> False, if not an advancement, otherwise the name of the advancement

print(msg.words) -> all the words in a list

print(msg.timestamp) -> the exact time the text was converted to Chat object

print(msg.prefix) -> the prefix of the contents. Can be used for detecting custom commands

print(msg.suffix) -> the suffix of the content

# Custom attributes:

string = "`[239] VIP <KewlUsrnm> hello guys`"

txt = Chat(string).strip().custom_attributes(["[level]"," rank ","<user>"," content*"])


print(txt.level) -> 239

print(txt.rank) -> VIP

print(txt.user) -> KewlUsrnm

print(txt.content) -> hello guys

