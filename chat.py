import re
from time import time
class Chat:
    def __init__(self, s:str):
        if not isinstance(s, str):
            raise TypeError(f"expected str, not {type(s).__name__}")
        elif s == "":
            raise ValueError("Cannot convert empty string into a Chat object")
        self.text = s
        self.advancement = False
        if re.search(r"<.*>",self.text) is not None:
            self.user = re.match(r"<(.*?)>",self.text).group(1)
            self.content = self.text.replace(f"<{self.user}> ","")
            self.type = "chat"
        elif re.search(r"\[.*\]",self.text) is not None:
            self.user = re.match(r"\[(.*?)\]",self.text).group(1)
            self.content = self.text.replace(f"[{self.user}] ","")
            self.type = "chat"
        elif " whispers to you: " in self.text:
            self.user, self.content = re.match(r"(.*) whispers to you: (.*)",self.text).groups()
            self.type = "whisper"
        elif " has made the advancement " in self.text:
            self.user, self.advancement = re.match(r"(.*) has made the advancement \[(.*)\]",self.text).groups(1)
            self.content = ""
            self.type = "advancement"
        else:
            self.user = "server"
            self.content = self.text
            self.type = "terminal"
        self.words = self.content.split(" ")
        self.prefix = re.match(r".",self.content).group()
        self.suffix = self.text[-1]
        self.timestamp = time()
    
    def remove_prefix(self) -> str:
        """Remove the prefix from self.content and self.words"""
        self.content = re.match(fr"{self.prefix}(.*)",self.content).group(1)
        self.words = self.content.split(" ")