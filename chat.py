import re
from time import time
class Chat:
    def __init__(self, s:str) -> object:
        if not isinstance(s, str):
            raise TypeError(f"expected str, not {type(s).__name__}")
        elif s == "":
            raise ValueError("Cannot convert empty string into a Chat object")
        self.text = s
        self.advancement = False
        if re.search(r".*?<(.*?)>",self.text) is not None:
            self.user = re.match(r".*?<(.*?)>",self.text).group(1)
            self.content = self.text.replace(f"<{self.user}> ","")
            self.type = "chat"
        elif " whispers to you: " in self.text:
            self.user, self.content = re.match(r"(.*) whispers to you: (.*)",self.text).groups()
            self.type = "whisper"
        elif re.search(r"^(.*?) has (made the advancement|completed the challenge|reached the goal) \[(.*)\]",self.text):
            match = re.match(r"(.*?) has (made the advancement|completed the challenge|reached the goal) \[(.*)\]",self.text)
            self.user = match.group(1) 
            self.advancement = match.group(2)
            self.content = ""
            self.type = "advancement"
        else:
            self.user = "server"
            self.content = self.text
            self.type = "terminal"
        self.words = self.content.split(" ")
        try: self.prefix = re.match(r".",self.content).group()
        except: self.prefix = ""
        try: self.suffix = self.content[-1]
        except: self.suffix = ""
        self.timestamp = time()
        self.attributes = ["text","advancement","user","content","type","words","prefix","suffix","timestamp","attributes"]
    
    def remove_prefix(self) -> object:
        """Remove the prefix from self.content and self.words"""
        self.content = re.match(fr"{self.prefix}(.*)",self.content).group(1)
        self.words = self.content.split(" ")
        return self
    
    def strip(self) -> object:
        """Remove all attributes from the object, except self.text"""
        attributes = self.attributes
        for i in attributes:
            if hasattr(self, i) and i != "text":
                self.__dict__.pop(i, None)
        return self
    
    def custom_attributes(self,template:list=None) -> object:
        """Create custom attributes using a template"""
        if template is None or not isinstance(template, list):
            raise TypeError(f"Cannot use {(type(template).__name__)!r} as a template")
        elif template == []:
            raise ValueError(f"Expected a non empty list, but got {template}")
        self.attributes = []
        text = self.text
        for i in template:
            prefix = i[0]
            suffix = i[-1]
            if prefix in r".^$*+?{}[]\|()":
                prefix = fr"\{prefix}"
            if suffix in r".^$*+?{}[]\|()":
                suffix = fr"\{suffix}"

            match = re.match(fr".*?{prefix}(.*?){suffix}.*?",i)
            attribute = match.group(1)
            if prefix == r"\*":
                prefix = ""
            if suffix != r"\*":
                try: value = re.match(fr".*?{prefix}(.*?){suffix}",text).group(1)
                except: value = None
                rplace = re.match(fr"(.*?{prefix}.*?{suffix})",text).group(1)
            else:
                try: value = re.match(fr"{prefix}(.*)",text).group(1)
                except: value = None
                rplace = ""
            text = text.replace(rplace,"")
            setattr(self,attribute,value)
            self.attributes.append(attribute)
        return self