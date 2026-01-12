import system.lib.minescript as minescript
import re
import time
import random
from chat import Chat

minescript.echo("§6[Chat Games] §dScript Started!")

WORDS = {
    "water", "wonderland", "star", "andesite", "granite", "diorite", "stone", "cobblestone", "white", "zombie", "skeleton", "creeper",
    "spider", "black", "red", "orange", "green", "gray", "wood", "leather", "sheep", "cow", "crate", "lava", "bucket", "pig",
    "villager", "village", "iron", "gold", "diamond", "netherite", "shulker", "easy", "normal", "hard", "hardcore", "survival", "creative",
    "grass", "dirt", "gravel", "pickaxe", "shovel", "hoe", "axe", "sword", "bow", "arrow", "trident", "potion", "dispenser", "dropper",
    "observer", "piston", "redstone", "lapis", "golem", "oak", "birch", "mangrove", "spruce", "cherry", "crimson", "warped", "portal",
    "nether", "end", "root", "roots", "ladder", "carpet", "glass", "peaceful", "nightmare", "enchant", "elytra", "phantom", "membrane",
    "dragon", "enderman", "brewing", "barrel", "hopper", "day", "night", "warden", "stronghold", "shears", "fishing", "crossbow", "chunk",
    "fortress", "witch", "furnace", "leggings", "boots", "chestplate", "helmet", "shield", "ender", "pearl", "smite", "lightning", "turtle",
    "axolotl", 'experience', "command", "explore", "realms", "sprint", "sneak", "sit", "swim", "acacia", "emerald", "coal", "copper",
    "beacon", "firework", "fireworks", "rocket", "enderchest", "chest", "shulkerbox", "horse", "donkey", "mule", "dolphin", "block",
    "adventure", "wolf", "cat", "ocelot", "rank", "mana", "cauldron", "anvil", "grindstone", "smelt", "recipie", "leaves", "strider",
    "bedrock", "pegasus", "trade", "wither", "poppy", "dandelion", "orchid", "blue", "respawn", "spawn", "swarm", "beehive", "bee",
    "click", "item", "painting", "quartz", "obsidian", 'bamboo', "clay", "brick", "rabbit", "build", "sand", "minecart", "bell",
    "blaze", "ghast", "frost", "mango", "lemon", "apple", "slime", "music", "campfire", "lantern", "torch", "villain", "guard", "moss",
    "dripstone", "amethyst", "tuff", "deepslate", "candle", "rails", "noteblock", "sculk", "trapdoor", "button", "glowstone", "gold block",
    "yellow", "haybale"
    }

with minescript.EventQueue() as event_queue:
    event_queue.register_chat_listener()
    while True:
        event = event_queue.get()
        if event.type == minescript.EventType.CHAT:
            message = Chat(event.message).custom_attributes(["[dummy]","[dummy]"])
            if message.dummy is None:
                delay = random.uniform(0.3, 0.7)
                time.sleep(delay + (len(message.content)/40))

                if re.search(r"The first (person|player)? ?to solve",message.content):
                    minescript.echo("§6[Chat Games] §dSolve trigger activated")
                    match = re.search(r"'([^']*)'", message.content)

                    if not match:
                        match = re.search(r"solve\s+([0-9+\-*/().\s]+)", message.content)

                    if match:
                        expression = match.group(1)

                        try:
                            result = eval(expression)
                            if result == int(result):
                                result = int(result)
                            minescript.chat(str(result))

                        except Exception as e:
                            minescript.echo(f"§6[Chat Games] §dEval failed: {e}")

                if re.search(r"The first (person|player)? ?to type",message.content):
                    minescript.echo("§6[Chat Games] §dType trigger activated")
                    match = re.search(r"'([^']*)'", message.content)

                    if not match:
                        match = re.search(r"type\s+(.*?)\s+wins", message.content, re.IGNORECASE)

                    if match:
                        answer = match.group(1).strip()
                        minescript.chat(answer)

                if re.search(r"The first (person|player)? ?to unreverse",message.content):
                    minescript.echo("§6[Chat Games] §dUnreverse activated")
                    match = re.search(r"'([^']*)'", message.content)

                    if not match:
                        match = re.search(r"unreverse\s+(.*?)\s+wins", message.content, re.IGNORECASE)

                    if match:
                        text = match.group(1).strip()
                        reversed_text = text[::-1]
                        minescript.chat(reversed_text)


                if re.search(r"The first (person|player)? ?to unscramble",message.content):
                    minescript.echo("§6[Chat Games] §dUnscramble trigger activated")
                    match = re.search(r"'([^']+)'", message.content)
                    if not match:
                        match = re.search(r"unscramble\s+(.*?)\s+wins", message.content, re.IGNORECASE)

                    if match:
                        scrambled = match.group(1).strip().lower()
                        possible = []

                        for word in WORDS:
                            if len(word) == len(scrambled) and sorted(word) == sorted(scrambled):
                                possible.append(word)

                        if possible:
                            minescript.chat(possible[0])