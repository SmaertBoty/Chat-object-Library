import re
from time import time, perf_counter
class Chat:
    def __init__(self, s:str) -> object:
        if not isinstance(s, str):
            raise TypeError(f"expected str, not {type(s).__name__}")
        elif s == "":
            raise ValueError("Cannot convert empty string into a Chat object")
        self.text = s
        self.custom = False
        self.advancement = False
        self.attributes = []
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
            causes = r"(was slain by|was shot by|was blown up by|was killed(?: by)?|was fireballed by|was roasted in dragon breath(?: by)?|tried to swim in lava(?: to escape)?|walked into fire whilst fighting|burned to death|went up in flames|drowned(?: whilst trying to escape)?|suffocated in a wall(?: while fighting)?|hit the ground too hard(?: whilst trying to escape)?|fell from a high place|fell off (?:a ladder|some vines|some twisting vines|some weeping vines)|experienced kinetic energy(?: while trying to escape)?|starved to death(?: whilst fighting)?|was pricked to death|was stabbed by a sweet berry bush(?: while trying to escape)?|was impaled on a stalagmite|was struck by lightning(?: whilst fighting)?|froze to death(?: while trying to escape)?|withered away(?: whilst fighting)?|died from poison(?: while fighting)?|fell out of the world|didn't want to live in the same world as|died|blew up)"
            match = re.match(fr"(.*?) {causes} (.*?)(?: using (.*))?$", self.text)
            if match is not None:
                self.user = match.group(1)
                try: self.reason = match.group(2)
                except: self.reason = None
                try: self.causer = match.group(3)
                except: self.causer = None
                try: self.item = match.group(4)
                except: self.item = None
                self.type = "death"
            else:
                self.user = "server"
                self.content = self.text
                self.type = "terminal"
        try: self.words = self.content.split(" ")
        except: self.words = None
        try: self.prefix = re.match(r".",self.content).group()
        except: self.prefix = ""
        try: self.suffix = self.content[-1]
        except: self.suffix = ""
        self.timestamp = time()
        for i in self.__dict__:
            self.attributes.append(i)
            if getattr(self,i) == "":
                setattr(self,i,None)
    
    def remove_prefix(self) -> object:
        """Remove the prefix from self.content and self.words if not custom"""
        if not self.custom:
            self.content = re.match(fr"{self.prefix}(.*)",self.content).group(1)
            self.words = self.content.split(" ")
        return self
    
    def strip(self) -> object:
        """Remove all attributes from the object, except self.text and self.custom"""
        attributes = self.attributes
        for i in attributes:
            if hasattr(self, i) and i != "text":
                self.__dict__.pop(i, None)
                self.attributes.remove(i)
        return self
    
    def custom_attributes(self,template:list=None) -> object:
        """Create custom attributes using a template"""
        if template is None or not isinstance(template, list):
            raise TypeError(f"Cannot use {(type(template).__name__)!r} as a template")
        elif template == []:
            raise ValueError(f"Expected a non empty list, but got {template}")
        self.custom = True
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