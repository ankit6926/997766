import asyncio
import contextlib
import random
import os
import os
import asyncio
import json
import time
import importlib
import sys
import requests
from highrise import ResponseError
import requests 
import curses
import discord
import contextlib
import random
from typing import Any, Dict, Union
from keep_alive import keep_alive

keep_alive()

from highrise import (
    BaseBot,
    ChatEvent,
    Highrise,
    __main__,
    UserJoinedEvent,
    UserLeftEvent,
    AnchorPosition,
    BaseBot,
    Position,
    Reaction,
    ResponseError,
    User,
    CurrencyItem,
    GetMessagesRequest,
    Item,
)
from highrise.models import (
    AnchorPosition,
    ChannelEvent,
    ChannelRequest,
    ChatEvent,
    ChatRequest,
    CurrencyItem,
    EmoteEvent,
    EmoteRequest,
    Error,
    FloorHitRequest,
    GetRoomUsersRequest,
    GetWalletRequest,
    IndicatorRequest,
    Item,
    Position,
    Reaction,
    ReactionEvent,
    ReactionRequest,
    SessionMetadata,
    TeleportRequest,
    TipReactionEvent,
    User,
    UserJoinedEvent,
    UserLeftEvent,
)
{
}
from json import load, dump
from time import time
from math import sqrt
from highrise import BaseBot, User, Position, AnchorPosition


moderators = ['its_me_aaru__","Moye___']


class Bot(BaseBot):
    continuous_emote_tasks: Dict[int, asyncio.Task[Any]] = {}  
    user_data: Dict[int, Dict[str, Any]] = {}
    EMOTE_DICT = {
      "charging"        : "emote-charging",
      "possessedpuppet" : "emote-possessedpuppet",
      "test"            : "dance-anime",
      "partytime"       : "emote-celebrate",
      "creepycute"      : "emote-creepycute",
      "sui"             : "emote-celebrationstep",
      "angry"           : "emoji-angry",
      "ANGRY"           : "emoji-angry",
      "Angry"           : "emoji-angry",
      "gottogo"         : "idle-toilet",
      "airguitar"       : "idle-guitar",
      "AIRGUITAR"       : "idle-guitar",
      "Airguitar"       : "idle-guitar",
      "bow"             : "emote-bow",
      "BOW"             : "emote-bow",
      "Bow"             : "emote-bow",
      "casual"          : "idle-dance-casual",
      "revelation"      : "emote-headblowup",
      "bashful"         : "emote-shy2",
      "CASUAL"          : "idle-dance-casual",
      "Casual"          : "idle-dance-casual",
      "charging"        : "emote-charging",
      "CHARGING"        : "emote-charging",
      "zombiedance"     : "dance-zombie",
      "Charging"        : "emote-charging",
      "jingle"          : "dance-jinglebell",
      "cheerfull"       : "emote-pose5",
      "CHEERFULL"       : "emote-pose5",
      "Cheerfull"       : "emote-pose5",
      "confusion"       : "emote-confused",
      "CONFUSION"       : "emote-confused",
      "Confusion"       : "emote-confused",
      "cursing"         : "emoji-cursing",
      "CURSING"         : "emoji-cursing",
      "Cursing"         : "emoji-cursing",
      "curtsy"          : "emote-curtsy",
      "CURTSY"          : "emote-curtsy",
      "Curtsy"          : "emote-curtsy",
      "cutey"           : "emote-cutey",
      "CUTEY"           : "emote-cutey",
      "Cutey"           : "emote-cutey",
      "celebration"     : "emote-celebrationstep",
      "iceskating"      : "emote-iceskating",
      "nervous"         : "idle-nervous",
      "hyped"           : "emote-hyped",
      "CELEBRATION"     : "emote-celebrationstep",
      "Celebration"     : "emote-celebrationstep",  
      "CREEPYPUPPET"    : "dance-creepypuppet",
      "Creepypuppet"    : "dance-creepypuppet",
      "creepypuppet"    : "dance-creepypuppet",
      "ditzypose"       : "emote-pose9",
      "Ditzypose"       : "emote-pose9",
      "DITZYPOSE"       : "emote-pose9",
      "dont"            : "dance-tiktok2",
      "DONT"            : "dance-tiktok2",
      "Dont"            : "dance-tiktok2",
      "embracing"       : "emote-pose5",
      "EMBRACING"       : "emote-pose5",
      "Embracing"       : "emote-pose5",
      "emotecute"       : "emote-cute",
      "EMOTECUTE"       : "emote-cute",
      "Emotecute"       : "emote-cute",
      "energyball"      : "emote-energyball",
      "ENERGYBALL"      : "emote-energyball",
      "Energyball"      : "emote-energyball",
      "enthused"        : "idle-enthusiastic",
      "ENTHUSED"        : "idle-enthusiastic",
      "Enthused"        : "idle-enthusiastic",
      "fashionista"     : "emote-fashionista",
      "FASHIONISTA"     : "emote-fashionista",
      "Fashionista"     : "emote-fashionista",
      "fashionpose"     : "emote-pose5",
      "FASHIONPOSE"     : "emote-pose5",
      "Fashionpose"     : "emote-pose5",
      "flex"            : "emoji-flex",
      "FLEX"            : "emoji-flex",
      "Flex"            : "emoji-flex",
      "flirtywave"      : "emote-lust",
      "FLIRTYWAVE"      : "emote-lust",
      "Flirtywave"      : "emote-lust",
      "flirtywink"      : "emote-pose1",
      "FLIRTYWINK"      : "emote-pose1",
      "Flirtywink"      : "emote-pose1",
      "float"           : "emote-float",
      "FLOAT"           : "emote-float",
      "Float"           : "emote-float",
      "frog"            : "emote-frog",
      "FROG"            : "emote-frog",
      "Frog"            : "emote-frog",
      "gravedance"      : "dance-weird",
      "GRAVEDANCE"      : "dance-weird",
      "Gravedance"      : "dance-weird",
      "gravity"         : "emote-gravity",
      "GRAVITY"         : "emote-gravity",
      "Gravity"         : "emote-gravity",
      "greedy"          : "emote-greedy",
      "GREEDY"          : "emote-greedy",
      "Greedy"          : "emote-greedy",
      "groovypenguin"  : "dance-pinguin",
      "Groovypenguin"   : "dance-pinguin",
      "GROOVYPENGUIN"   : "dance-pinguin",
      "Penguin"         : "dance-pinguin",
      "penguin"         : "dance-pinguin",
      "hello"           : "emote-hello",
      "HELLO"           : "emote-hello",
      "Hello"           : "emote-hello",
      "hot"             : "emote-hot",
      "HOT"             : "emote-hot",
      "Hot"             : "emote-hot",
      "icecream"        : "dance-icecream",
      "ICECREAM"        : "dance-icecream",
      "Icecream"        : "dance-icecream",
      "ichallengeyou"   : "emote-pose3",
      "ICHALLENGEYOU"   : "emote-pose3",
      "Ichallengeyou"   : "emote-pose3",
      "kiss"            : "emote-kiss",
      "KISS"            : "emote-kiss",
      "Kiss"            : "emote-kiss",
      "kpop"            : "dance-blackpink",
      "KPOP"            : "dance-blackpink",
      "Kpop"            : "dance-blackpink",
      "lambi"           : "emote-superpose",
      "LAMBI"           : "emote-superpose",
      "Lambi"           : "emote-superpose",
      "laugh"           : "emote-laughing",
      "LAUGH"           : "emote-laughing",
      "Laugh"           : "emote-laughing",
      "letsgo"          : "dance-shoppingcart",
      "LETSGO"          : "dance-shoppingcart",
      "Letsgo"          : "dance-shoppingcart",
      "timejump"        : "emote-timejump",
      "maniac"          : "emote-maniac",
      "MANIAC"          : "emote-maniac",
      "Maniac"          : "emote-maniac",
      "model"           : "emote-model",
      "MODEL"           : "emote-model",
      "Model"           : "emote-model",
      "no"              : "emote-no",
      "NO"              : "emote-no",
      "No"              : "emote-no",
      "ogdance"         : "dance-macarena",
      "OGDANCE"         : "dance-macarena",
      "Ogdance"         : "dance-macarena",
      "PENNYDANCE"      : "dance-pennywise",
      "Pennydance"      : "dance-pennywise",
      "pennydance"      : "dance-pennywise",      
      "pose1"           : "emote-pose1",
      "POSE1"           : "emote-pose1",
      "Pose1"           : "emote-pose1",
      "pose2"           : "emote-pose3",
      "POSE2"           : "emote-pose3",
      "Pose2"           : "emote-pose3",
      "pose3"           : "emote-pose5",
      "POSE3"           : "emote-pose5",
      "Pose3"           : "emote-pose5",
      "pose4"           : "emote-pose7",
      "POSE4"           : "emote-pose7",
      "Pose4"           : "emote-pose7",
      "pose5"           : "emote-pose8",
      "POSE5"           : "emote-pose8",
      "Pose5"           : "emote-pose8",
      "punkguitar"      : "emote-punkguitar",
      "PUNKGUITAR"      : "emote-punkguitar",
      "Punkguitar"      : "emote-punkguitar",
      "raisetheroof"    : "emoji-celebrate",
      "RAISETHEROOF"    : "emoji-celebrate",
      "Raisetheroof"    : "emoji-celebrate",
      "readytorumble"   : "emote-boxer",
      "READYTORUMBLE"   : "emote-boxer",
      "Readytorumble"   : "emote-boxer",
      "russian"         : "dance-russian",
      "RUSSIAN"         : "dance-russian",
      "Russian"         : "dance-russian",
      "sad"             : "emote-sad",
      "SAD"             : "emote-sad",
      "Sad"             : "emote-sad",
      "saunteraway"     : "dance-anime",
      "Saunteraway"     : "dance-anime",
      "SAUNTERAWAY"     : "dance-anime",
      "savage"          : "dance-tiktok8",
      "SAVAGE"          : "dance-tiktok8",
      "Savage"          : "dance-tiktok8",
      "sayso"           : "idle-dance-tiktok4",
      "Sayso"           : "idle-dance-tiktok4",
      "SAYSO"           : "idle-dance-tiktok4",
      "shuffle"         : "dance-tiktok10",
      "SHUFFLE"         : "dance-tiktok10",
      "Shuffle"         : "dance-tiktok10",
      "shy"             : "emote-shy",
      "SHY"             : "emote-shy",
      "Shy"             : "emote-shy",
      "singalong"       : "idle_singing",
      "SINGALONG"       : "idle_singing",
      "Singalong"       : "idle_singing",
      "sit"             : "idle-loop-sitfloor",
      "SIT"             : "idle-loop-sitfloor",
      "Sit"             : "idle-loop-sitfloor",
      "snowangel"       : "emote-snowangel",
      "SNOWANGEL"       : "emote-snowangel",
      "Snowangel"       : "emote-snowangel",
      "snowball"        : "emote-snowball",
      "SNOWBALL"        : "emote-snowball",
      "Snowball"        : "emote-snowball",
      "Stargaze"        : "emote-stargazer",
      "stargaze"        : "emote-stargazer",
      "stars"        : "emote-stargazer",
      "surprise"        : "emote-pose6",
      "SURPRISE"        : "emote-pose6",
      "Surprise"        : "emote-pose6",
      "swordfight"      : "emote-swordfight",
      "SWORDFIGHT"      : "emote-swordfight",
      "Swordfight"      : "emote-swordfight",
      "telekinesis"     : "emote-telekinesis",
      "TELEKINESIS"     : "emote-telekinesis",
      "Telekinesis"     : "emote-telekinesis",
      "teleport"        : "emote-teleporting",
      "TELEPORT"        : "emote-teleporting",
      "Teleport"        : "emote-teleporting",
      "thumbsup"        : "emoji-thumbsup",
      "THUMBSUP"        : "emoji-thumbsup",
      "Thumbsup"        : "emoji-thumbsup",
      "tired"           : "emote-tired",
      "TIRED"           : "emote-tired",
      "Tired"           : "emote-tired",
      "tummyache"       : "emoji-gagging",
      "TUMMYACHE"       : "emoji-gagging",
      "Tummyache"       : "emoji-gagging",
      "uwu"             : "idle-uwu",
      "UWU"             : "idle-uwu",
      "Uwu"             : "idle-uwu",
      "viral"           : "dance-tiktok9",
      "VIRAL"           : "dance-tiktok9",
      "Viral"           : "dance-tiktok9",
      "wave"            : "emote-wave",
      "WAVE"            : "emote-wave",
      "Wave"            : "emote-wave",
      "worm"            : "emote-snake",
      "WORM"            : "emote-snake",
      "Worm"            : "emote-snake",
      "wrong"           : "dance-wrong",
      "WRONG"           : "dance-wrong",
      "Wrong"           : "dance-wrong",
      "yes"             : "emote-yes",
      "YES"             : "emote-yes",
      "Yes"             : "emote-yes",
      "zerogravity"     : "emote-astronaut",
      "Zerogravity"     : "emote-astronaut",
      "ZEROGRAVITY"     : "emote-astronaut",
      "zombierun"       : "emote-zombierun",
      "Zombierun"       : "emote-zombierun",
      "ZOMBIERUN"       : "emote-zombierun",  
    }
    continuous_emote_task = None
    def __init__(self):
        super().__init__()
        # Initialize user data dictionary
        self.joined_users = []  # List to store joined user data
        self.user_reactions = {}
        self.command_modules = {}  # A dictionary to store the loader
        self.room_dictionary = {
            "room_1": "646dce94304425f9e19f5c42",
            "room_2": "64c56b3f93191a44cc2aaa53",
        }
        self.developer_usernames = ["its_me_aaru__","mistillusion"]
        self.allowed_usernames = ["its_me_aaru__","mistillusion"]
        self.moderators = ["its_me_aaru__","Amit_Raj","xx_G0D_xx","Moye___","y._.0bito._.z","itz_varun","OWNER_HERE","SINGLEHIT","_itz__mikey","POPPY64089","Spicy_B2B","Zeel_1"]# Add more usernames to this list if needed

    OUTFITS = [
    [
        Item('clothing', 1, 'body-flesh', True, 26),
        Item('clothing', 1, 'eye-n_basic2018malesquaresleepy', False, 7),
        Item('clothing', 1, 'eyebrow-n_basic2018newbrows07', False, 7),
        Item('clothing', 1, 'nose-n_basic2018newnose05', False, 7),
        Item('clothing', 1, 'mouth-basic2018chippermouth', False, 7),
        Item('clothing', 1, 'watch-n_room32019blackwatch', False, 7),
        Item('clothing', 1, 'glasses-n_room12019circleshades', False, 7),
        Item('clothing', 1, 'earrings-n_room12019goldhoops', False, 7),
        Item('clothing', 1, 'hair_back-n_basic2018wavypulledback', False, 7),
        Item('clothing', 1, 'hair_front-n_malenew07', False, 7),
        Item('clothing', 1, 'shirt-n_2016fallblackkknottedtee', True, 7),
        Item('clothing', 1, 'pants-n_room32019highwasittrackshortsblack', False, 7),
        Item('clothing', 1, 'shoes-n_room22019kneehighsblack', False, 7),
    ]
             ]


    async def on_start(self, session_metadata: SessionMetadata) -> None:
        print("BOT IN THE ROOM")
        self.highrise.tg.create_task(
            self.highrise.teleport(
                session_metadata.user_id,
                Position(
                    19.5,
                    0,
                    6.5,
                    "FrontLeft"
                        )
                          )
                                    )

        #await self.highrise.walk_to(Position(18.5, 5.75, 19.5))

    async def on_message(self, user_id: str, conversation_id: str, is_new_conversation: bool) -> None:
        response = await self.highrise.get_messages(conversation_id)
        message = "" 

        if isinstance(response, GetMessagesRequest.GetMessagesResponse):
            if response.messages:
                message = response.messages[0].content
                print(message)

        if message:
            if message.lower() == "Hey":
                commands = [
                "Hey!",
                "Commands...",
                "list",
                "Emotelist"
                  ]
                for command in commands:
                    await self.highrise.send_message(conversation_id, command)

            
            elif message.lower() == "list":
                command_list = [
                "Here is the list of commands...",
                "Emotelist",
                "Poeticrizz",
                "Rizz",
                "Joke",
                "Roastme",
                "Funfact",
                "Deathyear",
                "Lovepercentage",
                "Hatepercentage",
                "Iq",
                "Straightmeter"
                 ]
                for command in command_list:
                    await self.highrise.send_message(conversation_id, command)

                
            elif message.lower() == "emotelist":
                await self.highrise.send_message(conversation_id, "emotelist...")
                await self.highrise.send_message(conversation_id,"angry\nbow\ncasual\nraisetheroof\ncharging\nconfusion\ncursing\ncurtsy\ncutey\ndont\nemotecute\nenergyball\nenthused\nfashionista\nflex\nflirtywave\nfloat\nfrog\ngravedance\ngravity\ngreedy\nhello\nhot\nicecream\nkiss\nkpop\nlambi\nlaugh\nletsgo\nmaniac\nmodel\nno\nogdance\npennydance\npose1\npose2\npose3\npose4\npose5\npunkguitar\nrussian\nsad\nsavage\nshuffle\nshy\nsingalong\nsit\nsnowangel\nsnowball\nswordfight\ntelekinesis\nteleport\nthumbsup\ntired\ntummyache\nviral\nwave\nweird\nworm\nyes\nzombierun")
              
            elif message == "I love you":
                await self.highrise.send_message(conversation_id, "👀")
            elif message == "Join":
                await self.highrise.send_message(conversation_id, "Wait for the RESULT❗\n\nYou Joined❗")
              

              
    async def on_user_join(self, user: User, position: Union[Position, AnchorPosition]) -> None:
      await self.highrise.chat(f"\nWelcome {user.username} to the BHARAT🙏🏻❤🇮🇳 \nType List or Check Bio!! \n\nIf U Want To Rent Bot Message on \nPm: its_me_aaru__\n\nBOT CREATED BY @its_me_aaru__ 💝❤🥀🙂")
      await self.highrise.chat(f"\nType (Join) in pm !! \nget a chance to win 1K GOLD\n\nNOTE: Dont message in room or wisper message only in PM to join! ❤🥀")
      await self.highrise.send_whisper(user.id, f"Try New Emote sleigh")
      
      await self.highrise.send_emote(
        random.choice(['emote-headblowup','emote-shy2','emote-shrink','emote-celebrationstep', 'idle-guitar', 'dance-pinguin', 'emote-roll', 'emote-superpunch', 'emote-kicking', 'idle-floorsleeping2', 'emote-hero', 'idle_layingdown2', 'idle_layingdown', 'dance-sexy', 'emoji-hadoken', 'emote-disappear', 'emote-graceful', 'sit-idle-cute', 'idle-loop-aerobics', 'dance-orangejustice', 'emote-rest', 'dance-martial-artist', 'dance-breakdance', 'emote-astronaut', 'emote-zombierun', 'idle_singing', 'emote- frollicking', 'emote-float', 'dance-creepypuppet', 'emote-ninjarun', 'emote-secrethandshake', 'emote-apart', 'emote-headball', 'dance-floss', 'emote-jetpack', 'emote-ghost-idle', 'dance-spiritual', 'dance-robotic', 'dance-metal', 'idle-loop-tapdance', 'idle-dance-swinging', 'emote-mindblown', 'emote-gangnam', 'emote-harlemshake', 'emote-robot', 'emote-nightfever' ,'emote-dance-singing', 'emote-dance-singing', 'emote-dance-singing', 'emote-dance-singing', 'emote-iceskating', 'emote-dance-sing','emote-timejump']))
      emote_choices = ["emote-headblowup","emote-shy2","dance-blackpink","dance-icecream","dance-macarena","dance-russian","dance-tiktok2","dance-tiktok8","dance-tiktok10","dance-wrong","emoji-gagging","emote-astronaut","emote-boxer","emote-celebrationstep","emote-charging","emote-cutey","emote-energyball","emote-fashionista","emote-float","emote-gravity","emote-maniac","emote-model","emote-pose6","emote-punkguitar","emote-snake","emote-snowangel","emote-snowball","emote-swordfight","emote-telekinesis","emote-teleporting","emote-zombierun","idle_singing","dance-anime","dance-creepypuppet","idle-guitar","dance-pinguin","emote-iceskating","emote-timejump","emote-hyped"]
      emote_choice = random.choice(emote_choices)
      await self.highrise.send_emote(emote_choice, user.id)      
      #print(f"{user.username} joined the room standing at {position}")
      #await self.highrise.send_emote("dance-creepypuppet", user.id)
      await self.send_random_reactions(user.id, num_reactions=1, delay=1.55)
    async def on_tip(self, sender: User, receiver: User, tip: CurrencyItem | Item) -> None:
      
      if tip.amount <= 10:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g - Boooooooooo!!!!!! {sender.username} ")
          tip_message = f" I know am just a bot, but i need gold to survive too u know ,{sender.username}"
          await self.highrise.chat(f"{tip_message}")
    
      elif tip.amount <= 100:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g - Cheapskate!!!{sender.username} ")
          tip_message=f" Damn Tip em more,Tip me too {sender.username}"
          await self.highrise.chat(f"{tip_message}")
        
      elif tip.amount <= 500:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g - Good Grief!!!{sender.username} ")
          tip_message = f" Soooooo you single baby boo ? i need a bf/gf who tips me g too  ,{sender.username}"
          await self.highrise.chat(f"{tip_message}") 
        
      elif tip.amount <= 1000:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g - Dayummmmmmm{sender.username} ")
          tip_message = f"Oh boy !!!! Is this love ?   ,{sender.username}"
          await self.highrise.chat(f"{tip_message}")
        
      elif tip.amount <= 5000:
          print(f"[TIP] {sender.username} tipped {receiver.username} {tip.amount}g -  {sender.username} ")
          tip_message = f"Tip me Daddy,Daddy,Pwease Daddy ,{sender.username}"
          await self.highrise.chat(f"{tip_message}")
        
      elif tip.amount >=10000:
        print(f"[TIP ] {sender.username} tipped {tip.amount} - I think I will call you daddy!")
        tip_message = [f"\n {sender.username} tipped {tip.amount} - I think I will call you daddy! ",
            f"\n  {sender.username} Oh boy !!!! Is this love ?   " ,
            f"\n {sender.username} Daddy ",
            f"\n{sender.username} I can buy my kids baby food tonight yayyyy ",
            f"\n {sender.username} Soooooo you single baby boo ?   "
        ]
        random_word = random.choice(tip_message)
        await self.highrise.chat(f"{random_word}")
        
    async def on_emote(self, user: User, emote_id: str, receiver: User | None) -> None:
      print(f"{user.username} emoted: {emote_id}")
      
    async def on_whisper(self, user: User, message: str) -> None:
     if "out" in message.lower() and user.username in self.moderators:
        try:
            await self.highrise.teleport(f"{user.id}", Position(15, 0, 23.5))
        except Exception as e:
            print("error 3:", e)
     elif "door" in message.lower() and user.username in self.moderators:
        try:
            await self.highrise.teleport(f"{user.id}", Position(18, 0.25, 8))
        except Exception as e:
            print("error 3:", e)
     elif "top" in message.lower():
        try:
            await self.highrise.teleport(f"{user.id}", Position(5, 17, 5))
        except Exception as e:
            print("error 3:", e)
     elif "middle" in message.lower():
        try:
            await self.highrise.teleport(f"{user.id}", Position(5, 10, 2))
        except Exception as e:
            print("error 3:", e)
     elif "tree" in message.lower() and user.username in self.moderators:
        try: 
            await self.highrise.teleport(f"{user.id}", Position(11.5 , 0 ,9.5))
        except Exception as e:
            print("error 3:", e)
     elif "bottom" in message.lower():
        try:
            await self.highrise.teleport(f"{user.id}", Position(1, 0, 10))
        except Exception as e:
            print("error 3:", e)      
     elif "up" in message.lower() and user.username in self.moderators:
        try:
            await self.highrise.teleport(f"{user.id}", Position(15, 17, 30))
        except Exception as e:
            print("error 3:", e)
     elif "get" in message.lower() and user.username in self.moderators:
        try:
            await self.highrise.teleport(f"{user.id}", Position(-5, 0, 3))
        except Exception as e:
            print("error 3:", e)
     elif "end" in message.lower() and user.username in self.moderators:
        try:
            await self.highrise.teleport(f"{user.id}", Position(-5, 0, 18.5))
        except Exception as e:
            print("error 3:", e)
     elif "center" in message.lower():
        try:
            await self.highrise.teleport(f"{user.id}", Position(10.5, 0.25, 11.5))
        except Exception as e:
            print("error 3:", e)
     elif "stair" in message.lower() and user.username in self.moderators:
        try:
            await self.highrise.teleport(f"{user.id}", Position(13.5, 9, 9.5))
        except Exception as e:
            print("error 3:", e)
     elif "air" in message.lower() and user.username in self.moderators:
        try:
            await self.highrise.teleport(f"{user.id}", Position(8.5, 5.75, 13.5))
        except Exception as e:
            print("error 3:", e)
     elif "4" in message.lower() and user.username in self.moderators:
        try: 
            await self.highrise.teleport(f"{user.id}", Position(6.5 , 0.75 ,14.5))
        except Exception as e:
            print("error 3:", e)
     elif "3" in message.lower() and user.username in self.moderators:
        try: 
            await self.highrise.teleport(f"{user.id}", Position(6.5 , 0.75 ,5.5))
        except Exception as e:
            print("error 3:", e)  
     elif "1" in message.lower() and user.username in self.moderators:
        try: 
            await self.highrise.teleport(f"{user.id}", Position(14.5, 0.75, 5.5))
        except Exception as e:
            print("error 3:", e)
     elif "2" in message.lower() and user.username in self.moderators:
        try: 
            await self.highrise.teleport(f"{user.id}", Position(14.5 , 0.75 ,14.5))
        except Exception as e:
            print("error 3:", e)
     elif "water" in message.lower() and user.username in self.moderators:
        try: 
            await self.highrise.teleport(f"{user.id}", Position(18.5 , 20 ,2.5))
        except Exception as e:
            print("error 3:", e)
     elif "gold" in message.lower() and user.username in self.moderators:
        try: 
            await self.highrise.teleport(f"{user.id}", Position(13.5 , 9.75 ,12.5))
        except Exception as e:
            print("error 3:", e)
    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        print(f"{user.username} sended the reaction {reaction} to {receiver.username}")

    async def on_user_move(self, user: User, pos: Position) -> None:
        print(f"{user.username} moved to {pos}")

    async def on_reaction(self, user: User, reaction: Reaction, receiver: User) -> None:
        text_to_emoji = {
        "wink": "😉",
        "wave": "👋",
        "thumbs": "👍",
        "heart": "❤️",
        "clap": "👏",
        }
        #await self.highrise.chat(f"\n{user.username} {text_to_emoji[reaction]} {receiver.username}")
        await self.highrise.send_emote(
        random.choice(['emote-headblowup','emote-shy2','emote-shrink','emote-celebrationstep', 'idle-guitar', 'dance-pinguin', 'emote-roll', 'emote-superpunch', 'emote-kicking', 'idle-floorsleeping2', 'emote-hero', 'idle_layingdown2', 'idle_layingdown', 'dance-sexy', 'emoji-hadoken', 'emote-disappear', 'emote-graceful', 'sit-idle-cute', 'idle-loop-aerobics', 'dance-orangejustice', 'emote-rest', 'dance-martial-artist', 'dance-breakdance', 'emote-astronaut', 'emote-zombierun', 'idle_singing', 'emote- frollicking', 'emote-float', 'dance-creepypuppet', 'emote-ninjarun', 'emote-secrethandshake', 'emote-apart', 'emote-headball', 'dance-floss', 'emote-jetpack', 'emote-ghost-idle', 'dance-spiritual', 'dance-robotic', 'dance-metal', 'idle-loop-tapdance', 'idle-dance-swinging', 'emote-mindblown', 'emote-gangnam', 'emote-harlemshake', 'emote-robot', 'emote-nightfever','emote-iceskating','emote-timejump']))
  
    async def on_user_leave(self, user: User) -> None:
        print(f"{user.username} Left the Room")
        await self.highrise.send_emote(
        random.choice(['emote-headblowup','emote-shy2','emote-shrink','emote-celebrationstep', 'idle-guitar', 'dance-pinguin', 'emote-roll', 'emote-superpunch', 'emote-kicking', 'idle-floorsleeping2', 'emote-hero', 'idle_layingdown2', 'idle_layingdown', 'dance-sexy', 'emoji-hadoken', 'emote-disappear', 'emote-graceful', 'sit-idle-cute', 'idle-loop-aerobics', 'dance-orangejustice', 'emote-rest', 'dance-martial-artist', 'dance-breakdance', 'emote-astronaut', 'emote-zombierun', 'idle_singing', 'emote- frollicking', 'emote-float', 'dance-creepypuppet', 'emote-ninjarun', 'emote-secrethandshake', 'emote-apart', 'emote-headball', 'dance-floss', 'emote-jetpack', 'emote-ghost-idle', 'dance-spiritual', 'dance-robotic', 'dance-metal', 'idle-loop-tapdance', 'idle-dance-swinging', 'emote-mindblown', 'emote-gangnam', 'emote-harlemshake', 'emote-robot', 'emote-nightfever','emote-iceskating','emote-timejump']))
        await self.stop_continuous_emote(user.id)

    async def on_chat(self, user: User, message: str) -> None:
        print(f"{user.username}:{message}")
        if message in self.EMOTE_DICT:
            emote_id = self.EMOTE_DICT[message]
            await self.highrise.send_emote(emote_id, user.id)
            
        if message.startswith("Loop"):
            emote_name = message[5:].strip()
            if emote_name in self.EMOTE_DICT:
                emote_id = self.EMOTE_DICT[emote_name]
                delay = 1
                if " " in emote_name:
                    emote_name, delay_str = emote_name.split(" ")
                    if delay_str.isdigit():
                        delay = float(delay_str)

                if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user.id].cancelled():
                    await self.stop_continuous_emote(user.id)

                task = asyncio.create_task(self.send_continuous_emote(emote_id, user.id,delay))
                self.continuous_emote_tasks[user.id] = task  

        elif message.startswith("Stop"):
            if user.id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user.id].cancelled():
                await self.stop_continuous_emote(user.id)

                await self.highrise.chat("Continuous emote has been stopped.")
            else:
                await self.highrise.chat("You don't have an active loop_emote.")
        elif message.lower().startswith("users"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"There are {len(room_users)} users in the room")
        elif message.startswith("!ban"):
            if user.username.lower() in self.moderators:
                parts = message.split()
                if len(parts) < 2:
                    await self.highrise.chat(user.id, "Usage: !ban @username")
                    return

                mention = parts[1]
                username_to_ban = mention.lstrip('@')  # Remove the '@' symbol from the mention
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]  # Extract the User objects
                user_ids = [user.id for user in users]  # Extract the user IDs

                if username_to_ban.lower() in [user.username.lower() for user in users]:
                    user_index = [user.username.lower() for user in users].index(username_to_ban.lower())
                    user_id_to_ban = user_ids[user_index]
                    await self.highrise.moderate_room(user_id_to_ban, "ban", 3600)  # Ban for 1 hour
                    await self.highrise.chat(f"Banned {mention} for 1 hour.")
                else:
                    await self.highrise.send_whisper(user.id, f"User {mention} is not in the room.")
            else:
                await self.highrise.send_whisper(user.id, "You can't use this command.")

        elif message.lower().startswith("?"):
            wallet = (await self.highrise.get_wallet()).content
            await self.highrise.chat(f"The bot wallet contains {wallet[0].amount} {wallet[0].type}")
        elif message.lower().startswith("Users"):
            room_users = (await self.highrise.get_room_users()).content
            await self.highrise.chat(f"There are {len(room_users)} users in the room")
          
        if message.lower().lstrip().startswith(("anime","fight", "penguin", "flirt", "stars", "gravity", "uwu", "zero","fashion", "icecream", "punk", "wrong", "sayso", "zombie", "cutey", "pose1", "pose3", "pose5", "pose7", "pose8", "dance", "shuffle", "viral", "weird", "russian", "curtsy", "snowball", "sweating", "snowangel", "cute", "worm", "lambi", "celebration", "frog", "energyball", "maniac", "teleport", "float", "telekinesis", "enthused", "confused", "charging", "shopping", "bow", "savage", "kpop", "model", "dont", "pennywise", "flex", "gagging", "greedy", "cursing", "kiss","timejump","gottogo","nervous","jingle","hyped")):
                response = await self.highrise.get_room_users()
                users = [content[0] for content in response.content]
                usernames = [user.username.lower() for user in users]
                parts = message[1:].split()
                args = parts[1:]
        
                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, f"Usage: {parts[0]} <@username>")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, "Invalid user format. Please use '@username'.")
                    return
                elif args[0][1:].lower() not in usernames:
                    await self.highrise.send_whisper(user.id, f"{args[0][1:]} is not in the room.")
                    return
        
                user_id = next((u.id for u in users if u.username.lower() == args[0][1:].lower()), None)
                if not user_id:
                    await self.highrise.send_whisper(user.id, f"User {args[0][1:]} not found")
                    return
        

                if message.lower().lstrip().startswith("fight"):
                        await self.highrise.chat(f"\nLmao \n@{user.username} And @{args[0][1:]}\nBoxers...🌚")
                        await self.highrise.send_emote("emote-boxer", user.id)
                        await self.highrise.send_emote("emote-boxer", user_id)

                elif message.lower().lstrip().startswith("penguin"):
                        await self.highrise.chat(f"\n🫂 @{user.username} And @{args[0][1:]} Both are penguins🐧❤️")
                        await self.highrise.send_emote("dance-pinguin", user.id)
                        await self.highrise.send_emote("dance-pinguin", user_id)

                elif message.lower().lstrip().startswith("flirt"):
                        await self.highrise.chat(f"\n Hey @{user.username} And @{args[0][1:]} Flirting hmmm... 😏❤️")
                        await self.highrise.send_emote("emote-lust", user.id)
                        await self.highrise.send_emote("emote-lust", user_id)

                elif message.lower().lstrip().startswith("stars"):
                        await self.highrise.send_emote("emote-stargazer", user.id)
                        await self.highrise.send_emote("emote-stargazer", user_id)

                elif message.lower().lstrip().startswith("zero"):
                        await self.highrise.send_emote("emote-astronaut", user.id)
                        await self.highrise.send_emote("emote-astronaut", user_id)

                elif message.lower().lstrip().startswith("gravity"):
                        await self.highrise.send_emote("emote-gravity", user.id)
                        await self.highrise.send_emote("emote-gravity", user_id)
                elif message.lower().lstrip().startswith("hyped"):
                        await self.highrise.send_emote("emote-hyped", user.id)
                        await self.highrise.send_emote("emote-hyped", user_id)

                elif message.lower().lstrip().startswith("uwu"):
                        await self.highrise.send_emote("idle-uwu", user.id)
                        await self.highrise.send_emote("idle-uwu", user_id)

                elif message.lower().lstrip().startswith("fashion"):
                        await self.highrise.send_emote("emote-fashionista", user.id)
                        await self.highrise.send_emote("emote-fashionista", user_id)

                elif message.lower().lstrip().startswith("icecream"):
                        await self.highrise.send_emote("dance-icecream", user.id)
                        await self.highrise.send_emote("dance-icecream", user_id)

                elif message.lower().lstrip().startswith("punk"):
                        await self.highrise.send_emote("emote-punkguitar", user.id)
                        await self.highrise.send_emote("emote-punkguitar", user_id)

                elif message.lower().lstrip().startswith("wrong"):
                        await self.highrise.send_emote("dance-wrong", user.id)
                        await self.highrise.send_emote("dance-wrong", user_id)

                elif message.lower().lstrip().startswith("sayso"):
                        await self.highrise.send_emote("idle-dance-tiktok4", user.id)
                        await self.highrise.send_emote("idle-dance-tiktok4", user_id)

                elif message.lower().lstrip().startswith("zombie"):
                        await self.highrise.send_emote("emote-zombierun", user.id)
                        await self.highrise.send_emote("emote-zombierun", user_id)

                elif message.lower().lstrip().startswith("cutey"):
                        await self.highrise.send_emote("emote-cutey", user.id)
                        await self.highrise.send_emote("emote-cutey", user_id)

                elif message.lower().lstrip().startswith("anime"):
                        await self.highrise.send_emote("dance-anime", user.id)
                        await self.highrise.send_emote("dance-anime", user_id)

                elif message.lower().lstrip().startswith("pose3"):
                        await self.highrise.send_emote("emote-pose3", user.id)
                        await self.highrise.send_emote("emote-pose3", user_id)

                elif message.lower().lstrip().startswith("pose1"):
                        await self.highrise.send_emote("emote-pose1", user.id)
                        await self.highrise.send_emote("emote-pose1", user_id)

                elif message.lower().lstrip().startswith("pose7"):
                        await self.highrise.send_emote("emote-pose7", user.id)
                        await self.highrise.send_emote("emote-pose7", user_id)

                elif message.lower().lstrip().startswith("pose8"):
                        await self.highrise.send_emote("emote-pose8", user.id)
                        await self.highrise.send_emote("emote-pose8", user_id)

                elif message.lower().lstrip().startswith("dance"):
                        await self.highrise.send_emote("idle-dance-casual", user.id)
                        await self.highrise.send_emote("idle-dance-casual", user_id)

                elif message.lower().lstrip().startswith("shuffle"):
                        await self.highrise.send_emote("dance-tiktok10", user.id)
                        await self.highrise.send_emote("dance-tiktok10", user_id)

                elif message.lower().lstrip().startswith("weird"):
                        await self.highrise.send_emote("emote-weird", user.id)
                        await self.highrise.send_emote("emote-weird", user_id)

                elif message.lower().lstrip().startswith("viralgroove"):
                        await self.highrise.send_emote("dance-tiktok9", user.id)
                        await self.highrise.send_emote("dance-tiktok9", user_id)
                    
                elif message.lower().lstrip().startswith("cute"):
                        await self.highrise.send_emote("emote-cute", user.id)
                        await self.highrise.send_emote("emote-cute", user_id)

                elif message.lower().lstrip().startswith("frog"):
                        await self.highrise.send_emote("emote-frog", user.id)
                        await self.highrise.send_emote("emote-frog", user_id)

                elif message.lower().lstrip().startswith("lambi"):
                        await self.highrise.send_emote("emote-superpose", user.id)
                        await self.highrise.send_emote("emote-superpose", user_id)

                elif message.lower().lstrip().startswith("celebration"):
                        await self.highrise.send_emote("emote-celebrationstep", user.id)
                        await self.highrise.send_emote("emote-celebrationstep", user_id)

                elif message.lower().lstrip().startswith("worm"):
                        await self.highrise.send_emote("emote-snake", user.id)
                        await self.highrise.send_emote("emote-snake", user_id)

                elif message.lower().lstrip().startswith("bow"):
                        await self.highrise.send_emote("emote-bow", user.id)
                        await self.highrise.send_emote("emote-bow", user_id)
                elif message.lower().lstrip().startswith("nerous"):
                        await self.highrise.send_emote("idle-nervous", user.id)
                        await self.highrise.send_emote("idle-nervous", user_id)

                elif message.lower().lstrip().startswith("energyball"):
                        await self.highrise.send_emote("emote-energyball", user.id)
                        await self.highrise.send_emote("emote-energyball", user_id)

                elif message.lower().lstrip().startswith("maniac"):
                        await self.highrise.send_emote("emote-maniac", user.id)
                        await self.highrise.send_emote("emote-maniac", user_id)

                elif message.lower().lstrip().startswith("teleport"):
                        await self.highrise.send_emote("emote-teleporting", user.id)
                        await self.highrise.send_emote("emote-teleporting", user_id)

                elif message.lower().lstrip().startswith("float"):
                        await self.highrise.send_emote("emote-float", user.id)
                        await self.highrise.send_emote("emote-float", user_id)

                elif message.lower().lstrip().startswith("telekinesis"):
                        await self.highrise.send_emote("emote-telekinesis", user.id)
                        await self.highrise.send_emote("emote-telekinesis", user_id)

                elif message.lower().lstrip().startswith("enthused"):
                        await self.highrise.send_emote("idle-enthusiastic", user.id)
                        await self.highrise.send_emote("idle-enthusiastic", user_id)

                elif message.lower().lstrip().startswith("confused"):
                        await self.highrise.send_emote("emote-confused", user.id)
                        await self.highrise.send_emote("emote-confused", user_id)

                elif message.lower().lstrip().startswith("shopping"):
                        await self.highrise.send_emote("dance-shoppingcart", user.id)
                        await self.highrise.send_emote("dance-shoppingcart", user_id)

                elif message.lower().lstrip().startswith("charging"):
                        await self.highrise.send_emote("emote-charging", user.id)
                        await self.highrise.send_emote("emote-charging", user_id)

                elif message.lower().lstrip().startswith("snowangel"):
                        await self.highrise.send_emote("emote-snowangel", user.id)
                        await self.highrise.send_emote("emote-snowangel", user_id)

                elif message.lower().lstrip().startswith("sweating"):
                        await self.highrise.send_emote("emote-hot", user.id)
                        await self.highrise.send_emote("emote-hot", user_id)

                elif message.lower().lstrip().startswith("snowball"):
                        await self.highrise.send_emote("emote-snowball", user.id)
                        await self.highrise.send_emote("emote-snowball", user_id)

                elif message.lower().lstrip().startswith("curtsy"):
                        await self.highrise.send_emote("emote-curtsy", user.id)
                        await self.highrise.send_emote("emote-curtsy", user_id)

                elif message.lower().lstrip().startswith("russian"):
                        await self.highrise.send_emote("dance-russian", user.id)
                        await self.highrise.send_emote("dance-russian", user_id)

                elif message.lower().lstrip().startswith("pennywise"):
                        await self.highrise.send_emote("dance-pennywise", user.id)
                        await self.highrise.send_emote("dance-pennywise", user_id)

                elif message.lower().lstrip().startswith("dont"):
                        await self.highrise.send_emote("dance-tiktok2", user.id)
                        await self.highrise.send_emote("dance-tiktok2", user_id)

                elif message.lower().lstrip().startswith("kpop"):
                        await self.highrise.send_emote("dance-blackpink", user.id)
                        await self.highrise.send_emote("dance-blackpink", user_id)

                elif message.lower().lstrip().startswith("model"):
                        await self.highrise.send_emote("emote-model", user.id)
                        await self.highrise.send_emote("emote-model", user_id)
                elif message.lower().lstrip().startswith("timejump"):
                        await self.highrise.send_emote("emote-timejump", user.id)
                        await self.highrise.send_emote("emote-timejump", user_id)

                elif message.lower().lstrip().startswith("savage"):
                        await self.highrise.send_emote("dance-tiktok8", user.id)
                        await self.highrise.send_emote("dance-tiktok8", user_id)
                elif message.lower().lstrip().startswith("gottogo"):
                        await self.highrise.send_emote("idle-toilet", user.id)
                        await self.highrise.send_emote("idle-toilet", user_id)

                elif message.lower().lstrip().startswith("flex"):
                        await self.highrise.send_emote("emoji-flex", user.id)
                        await self.highrise.send_emote("emoji-flex", user_id)

                elif message.lower().lstrip().startswith("gagging"):
                        await self.highrise.send_emote("emoji-gagging", user.id)
                        await self.highrise.send_emote("emoji-gagging", user_id)
                elif message.lower().lstrip().startswith("jingle"):
                        await self.highrise.send_emote("dance-jinglebell", user.id)
                        await self.highrise.send_emote("dance-jinglebell", user_id)

                elif message.lower().lstrip().startswith("greedy"):
                        await self.highrise.send_emote("emote-greedy", user.id)
                        await self.highrise.send_emote("emote-greedy", user_id)

                elif message.lower().lstrip().startswith("cursing"):
                        await self.highrise.send_emote("emoji-cursing", user.id)
                        await self.highrise.send_emote("emoji-cursing", user_id)
                  
                elif message.lower().lstrip().startswith("zero"):
                        await self.highrise.send_emote("emote-astronaut", user.id)
                        await self.highrise.send_emote("emote-astronaut", user_id)

                elif message.lower().lstrip().startswith("kiss"):
                        await self.highrise.send_emote("emote-kiss", user.id)
                        await self.highrise.send_emote("eote-kiss", user_id)
          
       #TO_BUY ROOM boost 
          
        if message.lower().startswith("boost") and user.username in self.allowed_usernames:
            response = await self.highrise.buy_room_boost(payment="bot_wallet_only", amount=1)
            print (response)
            await self.highrise.send_whisper(user.id,f"The bot have:\n{response}")

        #to buy room voice

        if message.lower().startswith("voice") and user.username in self.allowed_usernames:
            response = await self.highrise.buy_voice_time(payment="bot_wallet_only")
            print (response)
            await self.highrise.send_whisper(user.id,f"The bot have:\n{response}")
            if message.startswith("heart "):  # تحقق من رسالة تبدأ بـ "heart "
              try:
                  # استخراج العدد المطلوب واسم المستخدم من الرسالة
                  parts = message.split()
                  num_hearts = int(parts[-1])
                  target_username = parts[1].strip('@').lower()
          
                  if 1 <= num_hearts <= 100:
                      for _ in range(num_hearts):
                          target_user = None
                          response = await self.highrise.get_room_users()
                          for user_info in response.content:
                              if user_info[0].username.lower() == target_username:
                                  target_user = user_info[0]
                                  break
                          
                          if target_user:
                              await self.highrise.react("heart", target_user.id)
                          else:
                              await self.highrise.chat(f"the user {target_username} Not available in the room.")
                  else:
                      await self.highrise.chat("1  _ 100  only ")
              except ValueError:
                  await self.highrise.chat("الرجاء إدخال عدد صحيح بعد 'heart @user'.")  

            emote_mapping = {
                "all Float": "emote-float",
                "all Tiktok2": "dance-tiktok2",
                "all pose1": "emote-pose1",
                "all Shopping": "dance-shoppingcart",
                "all russian": "dance-russian",
                "all Sing": "idle_singing",
                "all Enth": "idle-enthusiastic",
                "all Casual": "idle-dance-casual",
                "all Sit": "idle-loop-sitfloor",
                "all Lust": "emote-lust",
                "all Creedy": "emote-greedy",
                "all Bow": "emote-bow",
                "all Curtsy": "emote-curtsy",
                "all Snow": "emote-snowball",
                "all Angel": "emote-snowangel",
                "all Confused": "emote-confused",
                "all Teleport": "emote-teleporting",
                "all Swordfight": "emote-swordfight",
                "all Energy": "emote-energyball",
                "all Tiktok8": "dance-tiktok8",
                "all Blackpink": "dance-blackpink",
                "all Model": "emote-model",
                "all Penny": "dance-pennywise",
                "all Tiktok10": "dance-tiktok10",
                "all Telekinesis": "emote-telekinesis",
                "all Hot": "emote-hot",
                "all Weird": "dance-weird",
                "all Pose7": "emote-pose7",
                "all Pose8": "emote-pose8",
                "all Pose3": "emote-pose3",
                "all Pose5": "emote-pose5"
            }
            
            # تحقق من البداية وقم بإرسال الرقصة المناسبة لجميع المستخدمين في الغرفة
            for key, emote in emote_mapping.items():
                if message.startswith(key) and user.username in ["LiarXD"]:
                    roomUsers = (await self.highrise.get_room_users()).content
                    for roomUser, _ in roomUsers:
                        if isinstance(roomUser, User):
                            await self.highrise.send_emote(emote, roomUser.id)
                        else:
                            print("Ignoring non-User object in roomUsers")
                    break  # لا حاجة للاستمرار بعد العثور على النطاق المناسب
            
            

          
            pass
          
        if message.lower().lstrip().startswith(("!invite", "/invite")) and user.username in self.developer_usernames:
                parts = message[1:].split()
                args = parts[1:]
                _bid = "c7d4244acba626a07a9c57c71e67c480ee6bcc0f45256e3aae71d97d5f14fb68" #Bot user.id here
                id = f"1_on_1:{_bid}:{user.id}"
                idx = f"1_on_1:{user.id}:{_bid}"
                rid = "64e77d88355c4b00c114688f" #Room ID Here

                if len(args) < 1:
                    await self.highrise.send_whisper(user.id, "\nUsage: !invite <@username> This command will send room invite to targeted username. if they ever interact with our bot in past\n • Example: !invite @its_me_aaru__")
                    return
                elif args[0][0] != "@":
                    await self.highrise.send_whisper(user.id, "Invalid user format. Please use '@username'.")
                    return

                url = f"https://webapi.highrise.game/users?&username={args[0][1:]}&sort_order=asc&limit=1"
                response = requests.get(url)
                data = response.json()
                users = data['users']
                
                for user in users:
                    user_id = user['user_id']
                    __id = f"1_on_1:{_bid}:{user_id}"
                    __idx = f"1_on_1:{user_id}:{_bid}"
                    __rid = "64e77d88355c4b00c114688f" #Room ID Here
                    try:
                        await self.highrise.send_message(__id, "Join Room", "invite", __rid)
                    except:
                        await self.highrise.send_message(__idx, "Join Room", "invite", __rid)


        if "List" in message or "list" in message:
            await self.highrise.send_whisper(user.id, "Commands‼️\nEmotes\nLoop (emote-name)\nEmotelist\nLovepercentage\nHatepercentage\nIq\nRoast\nRizz\nPoeticrizz\nJokes\nFunfact")
            await self.highrise.send_whisper(user.id, "more soon...")

       # if "Hi" in message or "Hey" in message or "Hello" in message:
            #await self.highrise.chat(f"\n@{user.username} Hello! How can I help you today?\nAny problem PM: @its_me_aaru__")

        #if "Hru" in message or "How are you" in message or "how are you" in message:
            #await self.highrise.chat(f"\n@{user.username} Thank you for asking! As a computer program, I don't have feelings, but I'm here and ready to assist you.")

        if "Emotelist" in message or "emotes" in message or "Emotes" in message or "emotelist" in message:
            await self.highrise.send_whisper(user.id,
"angry\nbow\ncasual\nraisetheroof\ncharging\nconfusion\ncursing\ncurtsy\ncutey\ndont\nemotecute\nenergyball\nenthused\nfashionista\nflex\nflirtywave\nfloat\nfrog\ngravedance\ngravity\ngreedy\nhello\nhot\nicecream\nkiss\nkpop\nlambi\nlaugh\nletsgo\nmaniac\nmodel\nno\nogdance\n")
            await self.highrise.send_whisper(user.id,"pennydance\npose1\npose2\npose3\npose4\npose5\npunkguitar\nrussian\nsad\nsavage\nshuffle\nshy\nsingalong\nsit\nsnowangel\nsnowball\nswordfight\ntelekinesis\nteleport\nthumbsup\ntired\ntummyache\nviral\nwave\nweird\nworm\nyes\nzombierun")
            await self.highrise.send_whisper(user.id,"\nBoxer\nDitzy\nSurprise\nCelebration\nAirguitar\nPenguin\nrevelation\nbashful\ncreepycute\ngottogo\niceskating\ntimejump\nnervous\njingle\nhyped\nMore emotes Soon...")
          
          
   
        if "Poeticrizz" in message or "poeticrizz" in message:
            poeticrizz = random.choice(["If you carried medusa’s curse, i would stare into your eyes so that my stone would gaze at your beauty for all eternity.", "If every star were a memory, i’d spend an eternity counting them all, just to relieve the moments I’ve spent with you","As the sun comes up, you have no shadow, because there’s nothing that can replicate your beauty","When i can’t be with you, i read your favorite book, listen to your favorite song, watch your favorite movie, because in them i find little bits of you" , "My darkest days are shifted with a slight gaze of your fascinating looks. Your beautiful dark eyes are the last fiber holding my shattered heart." ,"If I could weave a tapestry of our love, it would be a kaleidoscope of colors, each hue a testament to the depth of our affection." , "Your presence is like a sunrise, a radiant glow that banishes the darkness and fills my world with light." , "If I could sail the seas of time, I’d chart a course to the moment we first met, the instant our hearts became entwined.", "Your love is the anchor that holds me steady, a steadfast bond that keeps me grounded and secure.","If I could gather the sands of the desert, I’d create a monument to your beauty, a testament to your enchanting allure.","Your voice is the siren’s call, a mesmerizing melody that lures me into the depths of your love." , "If you’re the moon, i am the tide, for i flow under your command, forever longing for you, as you are my purpose.","If i had to wait my entire life for your love, I would. For when i have withered away, i’d be glad i got to experience heaven before i reached it.","For every star in the sky that went out, i would never know for you outshined them always.","If you were a grain of sand, I’d search every beach and desert looking for you and your beauty no matter how long i’d have to look. ","If you’re the angel of death, I’d be willing to die a million times just to see your beauty." , "If i was blinded the moment i lay my eyes on you, I would not grieve, for in that instance, i truly gazed upon perfection. " , "You are the sun to my sunflower, i will always be glancing at your gorgeous light as i follow you around amidst the bright morning." , "If i were dared to shout to the world how much i love you, i would simply whisper it in your ears." , "Your love is the beacon that guides me through the darkest storms, a lighthouse illuminating my heart’s shore.","If your heart were a canvas, I’d paint it with the colors of a thousand sunsets, each hue a testament to my love for you. " , "Like a rose in full bloom, your beauty captivates me, leaving me breathless and longing for your tender embrace. ","If i had to wait my entire life for your love, i would. When i’ve withered away, I’d be glad i got to experience heaven before i reached it.","If i had a flower for every time i thought of you, I’d have one, because not once have i stopped thinking about the perfection that you are.","If I could rearrange the cosmos, I would replace the sun with you for your beauty shines brighter than any star ever will my dear","The stars were so jealous of how bright you were, they had to make the sun fall just to be seen, yet you outshined them everytime.","Even if i learned every language, i couldn’t find the words to describe how beautiful you are.","Your laughter is the melody that dances through my soul, a symphony of joy that fills the chambers of my heart.","If our love were a river, it would flow endlessly, carving a path through the mountains of time, unstoppable and eternal.","Your eyes are the windows to a world of wonder, a universe of endless possibilities that I long to explore.","If I were a poet, I’d pen a thousand sonnets, each line a tribute to the enchanting spell you’ve cast upon me.","Your touch is like a gentle breeze, caressing my skin and awakening my senses, a testament to the power of your love.","In the garden of my heart, you are the most exquisite flower, a rare and precious bloom that I will cherish forever.","Your love is the compass that guides me, a true north that leads me to the shores of happiness and contentment.","If I could capture the essence of your beauty, I’d bottle it and wear it as a perfume, a fragrant reminder of your enchanting presence.","Your voice is the sweetest lullaby, a soothing balm that calms the tempest of my soul and lulls me into a state of blissful serenity.","If our love were a tapestry, it would be woven with threads of gold and silver, a masterpiece of passion and devotion.","Your smile is the sun that breaks through the clouds, a radiant beam of light that warms my heart and brightens my day.","If I were a sculptor, I’d chisel your likeness in marble, a timeless tribute to the beauty that has captured my heart.","Your love is the key that unlocks the treasure chest of my heart, revealing a bounty of affection and adoration.","Like a butterfly emerging from its cocoon, your love has transformed me, awakening a newfound sense of wonder and joy.","If I could pluck the stars from the sky, I’d arrange them in a constellation that spells your name, a celestial tribute to your radiant beauty.","Your presence is like a warm embrace on a cold winter’s night, a comforting haven that shelters me from the chill of loneliness.","If our love were a symphony, it would be a crescendo of passion and emotion, a masterpiece that resonates through the ages.","Your eyes are like twin galaxies, swirling with the mysteries of the universe, drawing me into their celestial embrace.","If I could harness the power of the wind, I’d send a gentle breeze to whisper my love for you in your ear.","Your love is the flame that ignites my soul, a burning passion that consumes me and sets my heart ablaze.","If I were a painter, I’d create a masterpiece with your beauty as my muse, a portrait of perfection that captures your essence.","Your touch is like a summer rain, a gentle caress that quenches my thirst and soothes my parched heart.","If our love were a dance, it would be a waltz of passion and grace, a timeless expression of our devotion to one another.","Your laughter is the song of angels, a heavenly chorus that lifts my spirits and fills my heart with joy.","If I could pluck the petals of a thousand roses, I’d create a path for you to walk upon, a fragrant tribute to your captivating charm.","Your touch is like a silken caress, a tender embrace that envelops me in a cocoon of warmth and affection.","If our love were a garden, it would be a paradise of vibrant blooms, a sanctuary of peace and tranquility.","Your smile is the rainbow that appears after the storm, a brilliant arc of color that brightens my world.","If I could write a novel, it would be an epic tale of our love, a timeless story of passion and devotion.","Your eyes are the mirrors of my soul, reflecting the depth of my love and the intensity of my desire.","If I could traverse the heavens, I’d pluck the most radiant star and present it to you as a token of my undying love.","Your love is the elixir that breathes life into my weary soul, a potion of passion that rejuvenates my heart.","If I could traverse the depths of the ocean, I’d collect the rarest pearls to adorn you, a symbol of the precious treasure you are to me.","Your embrace is like a warm blanket on a frosty night, enveloping me in a cocoon of comfort and affection.","If our love were a melody, it would be a sultry jazz tune, a seductive dance of passion and desire.","Your eyes sparkle like the finest champagne, intoxicating me with their effervescent allure.","If I could command the elements, I’d summon a gentle rain to caress your skin, each droplet a tender kiss from the heavens.","Your laughter is the chime of windchimes, a delicate symphony that fills the air with enchantment and delight.","If I could weave a spell, I’d conjure a magical realm where we could dance among the stars, our love transcending time and space.","Your touch is like the brush of a master artist, painting my heart with the vibrant hues of passion and desire.","If our love were a flame, it would burn with the intensity of a thousand suns, an inferno of devotion that consumes us both.","Your lips are like the petals of a delicate rose, their softness beckoning me to taste their sweet nectar.","If I could harness the power of the moon, I’d bathe you in its silvery glow, illuminating your ethereal beauty.","Your presence is like the first light of dawn, a radiant beam that dispels the shadows and fills my world with hope.","If I could write a love letter to the universe, I’d pen an ode to your enchanting allure, a testament to the spell you’ve cast upon me.","Your voice is the whisper of the wind, a gentle caress that stirs my soul and awakens my deepest desires.","If our love were a garden, it would be a lush oasis, a sanctuary of passion and pleasure where we could lose ourselves in each other’s embrace.","Your smile is the shimmer of sunlight on water, a dazzling display that captivates me and leaves me breathless.","If I could compose a symphony, I’d dedicate each note to the rhythm of your heartbeat, a musical tribute to our love’s harmony.","If I had a dollar for every mistake you did, I would have only one, because your entire life is a continuous mistake","The sun shines upon your beautiful face from dusk till dawn, but my love outshines the sun from dusk till dawn and far beyond that"])
            await self.highrise.chat(f": {user.username} - {poeticrizz}")
        
        if "Rizz" in message:
            pickuplines = random.choice(["Do you believe in love at first sight, or should I walk by again?","Is your name Google? Because you have everything I've been searching for.","Are you a magician? Whenever I look at you, everyone else disappears.","Do you have a map? I keep getting lost in your eyes.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","I must be a snowflake because I've fallen for you.","Excuse me, but I think you dropped something: my jaw.","Do you have a Band-Aid? Because I just scraped my knee falling for you.","Is your dad a boxer? Because you're a knockout!","Do you have a map? I keep getting lost in your eyes.","Is your name Google? Because you've got everything I've been searching for.","Do you have a name, or can I call you mine?","Are you a magician? Whenever I look at you, everyone else disappears.","Is your name Wi-Fi? Because I'm feeling a connection.","Do you have a sunburn, or are you always this hot?","Excuse me, but I think you dropped something: my jaw.","Is your dad a boxer? Because you're a knockout!","If you were a vegetable, you'd be a cute-cumber.","I must be a snowflake because I've fallen for you.","Is your name Google? Because you've got everything I've been searching for.","Do you have a map? Because I keep getting lost in your eyes.","Are you a magician? Every time I look at you, everyone else disappears.","Do you believe in love at first sight, or should I walk by again?","Excuse me, but I think you dropped something: my jaw.","Is your name Wi-Fi? Because I'm feeling a connection.","If you were a vegetable, you'd be a cute-cumber.","Can I follow you home? Cause my parents always told me to follow my dreams.","Is your dad a boxer? Because you're a knockout!","Do you have a name, or can I call you mine?", "I hope you know CPR, because you just took my breath away!","So, aside from taking my breath away, what do you do for a living?" , " I ought to complain to Spotify for you not being named this week’s hottest single." , "Are you a parking ticket? ‘Cause you’ve got ‘fine’ written all over you.","Is your name Google? Because you've got everything I've been searching for.","Can I follow you home? Cause my parents always told me to follow my dreams.","Do you believe in love at first sight, or should I walk by again?","If you were a vegetable, you'd be a cute-cumber.","Is your dad a boxer? Because you're a knockout!","Are you a magician? Because every time I look at you, everyone else disappears.","Excuse me, but I think you dropped something: my jaw.","If you were a triangle, you'd be acute one.","Can I take you out for coffee, or do you prefer to brew it yourself?","Are you made of copper and tellurium? Because you're Cu-Te.","Are you a camera? Because every time I look at you, I smile.","Do you have a name, or can I call you mine?","Do you have a map? Because I keep getting lost in your eyes.","I must be a snowflake because I've fallen for you.","I must be a magician because every time I look at you, everyone else disappears.","Do you have a Band-Aid? I just scraped my knee falling for you.","Are you a Wi-Fi signal? Because I'm feeling a connection.","Do you believe in fate? Because I think we were meant to meet.","Are you a time traveler? Because I can see you in my future.","Do you have a name, or can I call you mine?","Can I borrow a kiss? I promise I'll give it back.","I must be a snowflake because I've fallen for you.","If you were a vegetable, you'd be a cute-cumber.","Are you a campfire? Because you're hot and I want s'more.","Can I take you out for coffee, or do you prefer to brew it yourself?","Is your dad a boxer? Because you're a knockout!","Is your name Ariel? Because we mermaid for each other!","I'm not a photographer, but I can picture us together.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","If you were a fruit, you'd be a fine-apple.","Do you have a map? Because I keep getting lost in your eyes.","Do you believe in love at first sight, or should I walk by again?","I must be a snowflake because I've fallen for you.","Is your dad a boxer? Because you're a knockout!","Are you a magician? Because whenever I look at you, everyone else disappears.","Can I follow you home? Cause my parents always told me to follow my dreams.","Do you have a name, or can I call you mine?","Are you an interior decorator? When I saw you, the entire room became beautiful.","If you were a vegetable, you'd be a cute-cumber.","Do you believe in love at first sight, or should I walk by again?","Are you a Wi-Fi signal? Because I'm feeling a connection.","Are you a time traveler? Because I can see you in my future.","Do you have a map? Because I keep getting lost in your eyes.","Can I borrow a kiss? I promise I'll give it back.","If you were a triangle, you'd be acute one.","I must be a magician because every time I look at you, everyone else disappears.","Do you have a Band-Aid? I just scraped my knee falling for you.","Are you a campfire? Because you're hot and I want s'more.","Can I take you out for coffee, or do you prefer to brew it yourself?","Is your dad a boxer? Because you're a knockout!","Is your name Ariel? Because we mermaid for each other!","I'm not a photographer, but I can picture us together.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","If you were a fruit, you'd be a fine-apple.","Do you have a map? Because I keep getting lost in your eyes.","Do you believe in love at first sight, or should I walk by again?","I must be a snowflake because I've fallen for you.","Is your dad a boxer? Because you're a knockout!","Are you a magician? Because whenever I look at you, everyone else disappears.","Can I follow you home? Cause my parents always told me to follow my dreams.","Do you have a name, or can I call you mine?","Are you an interior decorator? When I saw you, the entire room became beautiful.","If you were a vegetable, you'd be a cute-cumber.","Do you believe in love at first sight, or should I walk by again?","Are you a Wi-Fi signal? Because I'm feeling a connection.","Are you a time traveler? Because I can see you in my future.","Do you have a map? Because I keep getting lost in your eyes.","Can I borrow a kiss? I promise I'll give it back.","If you were a triangle, you'd be acute one.","I must be a magician because every time I look at you, everyone else disappears.","Do you have a Band-Aid? I just scraped my knee falling for you.","Are you a campfire? Because you're hot and I want s'more.","Can I take you out for coffee, or do you prefer to brew it yourself?","Is your dad a boxer? Because you're a knockout!","Is your name Ariel? Because we mermaid for each other!","I'm not a photographer, but I can picture us together.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","Do you believe in love at first sight, or should I walk by again?","Are you a Wi-Fi signal? Because I'm feeling a connection.","Are you a time traveler? Because I can see you in my future.","Do you have a map? Because I keep getting lost in your eyes.","Can I borrow a kiss? I promise I'll give it back.","If you were a triangle, you'd be acute one.","I must be a magician because every time I look at you, everyone else disappears.","Do you have a Band-Aid? I just scraped my knee falling for you.","Are you a campfire? Because you're hot and I want s'more.","Can I take you out for coffee, or do you prefer to brew it yourself?","Is your dad a boxer? Because you're a knockout!","Is your name Ariel? Because we mermaid for each other!","I'm not a photographer, but I can picture us together.","Do you have a name, or can I call you mine?","If you were a vegetable, you'd be a cute-cumber.","If you were a fruit, you'd be a fine-apple.","Do you have a map? Because I keep getting lost in your eyes.","Do you believe in love at first sight, or should I walk by again?","I must be a snowflake because I've fallen for you.","Is your dad a boxer? Because you're a knockout!","If you hate me don't read this...Ok done it means you love me and I love you too congratulations we are in relationship...","i may not be a dentist but...I'll surely take care of that smile of yours","I don't have many pick up lines because I'm not trynna pick you up but pin you down","i love people with humor but i love hu-mor (humor rizz)","Are you a piano? Because I wanna use my fingers to play with you until you make beautiful noise!!!!!!!","Texting isn't enough I need you sitting on My lap facing me","Are you other peoples opinion? Cause I can't stop thinking about you (Social anxiety rizz)","Are u lamp of Aladin bcoz i wanna rub u down there and get all my wishes complete","Im glad you dad didn't pull out you're kinda Cool","The word of the day is 'LEGS' So why don't you come over and we can spread the word","I just wish I had more money instead of this massive cock.","Do yk the difference between history and you? History is the past & you are my future (History Rizz)","Are u the clock at school? Because I be lookin at u all day. (School clock rizz)","Are you a painting? Because i'd like to pin you against my wall (artist rizz)","Are you a box of chocolates? Cause I want to take your top off and eat you all night.","Math is incorrect they keep talking about x and y instead of u and i (algebraic rizz)","Why does everything have to be a relationship, We can't kiss and be friends?","In honor of pride month maz How about you let me She/Them T!ddies","I just say 'night' because if it was goodnight you'd be in my bed","You look kinda ill, you must be suffering from a lack of 'Vitamin ME'","Did you know that sleeping next to the person you like helps you fall asleep faster, reduces depression and makes you live longer so why aren't you here every night?"])
            await self.highrise.chat(f": {user.username} - {pickuplines}")
          
        if "Joke" in message or "joke" in message:
            joke = random.choice(["Yo mama's so fat, when she goes camping, the bears hide their food.", "Your mama's so fat she falls both sides of the bed" , "I wont tell ya lol", "Your mama's so stupid she studied for COVID test","Your mama so ugly when she goes to the dentist they make her lay face down","Your mama's so stupid she used a ruler to see how long she slept","Your mama's so fat her belt size is the size of the equator","Your mama's so ugly when she falls of the car, the driver gets arrested for littering" , "I told my wife she was drawing her eyebrows too high. She looked surprised.","Why don't scientists trust atoms? Because they make up everything.","What do you call fake spaghetti? An impasta.","Why don't skeletons fight each other? They don't have the guts.","I used to play piano by ear, but now I use my hands.","I'm on a whiskey diet. I've lost three days already.","What do you call a bear with no teeth? A gummy bear.","I told my wife she was drawing her eyebrows too low. She looked surprised.","The early bird might get the worm, but the second mouse gets the cheese.","Parallel lines have so much in common. It's a shame they'll never meet.","Why don't seagulls fly over the bay? Because then they'd be bagels.","How do you organize a space party? You planet.","Did you hear about the kidnapping at the playground? They woke up.","My boss told me to have a good day, so I went home.","Joke? Your whole life","i just found out if two girls are close, their period dates can change to be at the same time, tf kinda bluetooth is that","Remember if there's ever a person you like and are talking to, you should just cut off contact and block them because it's never gonna work","Nah cuz why tf do girls make code names for boys. Like who tf is 'Pineapple'"])
            await self.highrise.chat(f": {user.username} - {joke}")
          
        if "Funfact" in message or "funfact" in message:
            funfact = random.choice(["Honey never spoils. Archaeologists have found edible honey in ancient Egyptian tombs over 3,000 years old.","Bananas are berries, while strawberries are not technically berries but aggregate fruits.","The Eiffel Tower can grow up to 6 inches taller during the summer due to thermal expansion.","Humans and giraffes have the same number of neck vertebrae—seven.","Octopuses have three hearts.","The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted just 38 minutes.","The Great Wall of China is not visible from space with the naked eye.","The Hawaiian alphabet has only 12 letters: A, E, I, O, U, H, K, L, M, N, P, and W.","A group of flamingos is called a 'flamboyance.'","The tongue is the only muscle in the human body that is attached at only one end.","The average person will spend six months of their life waiting for red lights to turn green.","A group of crows is called a 'murder.'","The world's oldest known recipe is for beer and dates back over 4,000 years.","A day on Venus is longer than a year on Venus. It takes about 243 Earth days for Venus to complete one rotation but only 225 Earth days to orbit the Sun.","The shortest war in history was between Britain and Zanzibar on August 27, 1896. It lasted just 38 minutes.","The word 'nerd' was first coined by Dr. Seuss in his book 'If I Ran the Zoo.'","The unicorn is the national animal of Scotland.","The average person will walk the equivalent of three times around the world in their lifetime.","Cows have best friends and get stressed when they are separated.","The longest time between two twins being born is 87 days.","Astronauts cannot burp in space due to the absence of gravity.","A hummingbird weighs less than a penny.","The electric chair was invented by a dentist.","The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.","Slugs have four noses.","Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.","The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.","The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.","The first alarm clock could only ring at 4 a.m.","A crocodile's tongue is attached to the roof of its mouth and cannot move.","Sea otters hold hands while sleeping to avoid drifting apart.","The electric chair was invented by a dentist.","The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.","Slugs have four noses.","Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.","The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.","The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.","The first alarm clock could only ring at 4 a.m.","A crocodile's tongue is attached to the roof of its mouth and cannot move.","Sea otters hold hands while sleeping to avoid drifting apart.","The electric chair was invented by a dentist.","The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.","Slugs have four noses.","Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.","The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.","The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.","The first alarm clock could only ring at 4 a.m.","A crocodile's tongue is attached to the roof of its mouth and cannot move.","Sea otters hold hands while sleeping to avoid drifting apart.","The electric chair was invented by a dentist.","The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.","Slugs have four noses.","Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.","The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.","The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.","The first alarm clock could only ring at 4 a.m.","A crocodile's tongue is attached to the roof of its mouth and cannot move.","Sea otters hold hands while sleeping to avoid drifting apart.","The electric chair was invented by a dentist.","The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.","Slugs have four noses.","Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.","The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.","The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.","The first alarm clock could only ring at 4 a.m.","A crocodile's tongue is attached to the roof of its mouth and cannot move.","Sea otters hold hands while sleeping to avoid drifting apart.","The electric chair was invented by a dentist.","The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.","Slugs have four noses.","Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.","The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.","The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.","The first alarm clock could only ring at 4 a.m.","A crocodile's tongue is attached to the roof of its mouth and cannot move.","Sea otters hold hands while sleeping to avoid drifting apart.","The electric chair was invented by a dentist.","The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.","Slugs have four noses.","Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.","The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.","The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.","The first alarm clock could only ring at 4 a.m.","A crocodile's tongue is attached to the roof of its mouth and cannot move.","Sea otters hold hands while sleeping to avoid drifting apart.","The electric chair was invented by a dentist.","The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.","Slugs have four noses.","Baby elephants suck their trunks for comfort, similar to how human babies suck their thumbs.","The Statue of Liberty was a gift from France to the United States and was assembled in New York City in 1886.","The largest known organism on Earth is a fungus located in Oregon's Malheur National Forest. It covers 2.4 square miles.","The first alarm clock could only ring at 4 a.m.","A crocodile's tongue is attached to the roof of its mouth and cannot move.","Sea otters hold hands while sleeping to avoid drifting apart.","The electric chair was invented by a dentist.","The oldest known customer service complaint dates back to ancient Babylon, around 1750 BC.","Some people can unfocus their eyesight (or make their eyesight blurry) on command","Making fun of a short girls height is indirectly telling her that you are in love with her 😭","No matter how wrong she is, if she is short, forgive her. She is just a baby","If you see my typing for to long, just gimme time cuz I'm either tryna find a emoji or spell a word correctly.","you know your friendship elite if it started with 'when I first met you i didn't like you' ","Life is too short to argue just blame your sister for everything and move on","If you are dead inside, go outside ","If she has strict parents,back problems,stays on her phone all day,and gets mad and jealous over the little things and she's 5'0-5'6ft ,Wife her asap","Girls will never admit they like u lol either they text u all day, call you sir or bro, or post stuff on their story hoping you'll slide up","Never trust girls, they screenshot your messages and laugh at u with their friends","Instead of typing 'lol' or 'lmao' imma start using 'salts' which stands for Smiled A Little Then Stopped. It's way more accurate","When i say 'I hate drama' I mean I hate being involved in drama. Other people's drama On the other hand? Huge fan","If a boy cries for you keep him. But if a girl cries for you, it doesn't matter, she always cries","Girls need to realize that if they make the first move they have a 99,9% success rate"])
            await self.highrise.chat(f": {user.username} - {funfact}")
            
        if "Roastme" in message or "roastme" in message:
            roastme = random.choice(["Oh, look who finally decided to show up on time! Did you have to invent a new way of setting your alarm?" , "I heard you attempted cooking last night. How many smoke alarms did you set off this time?", "You're always talking about how organized you are, but have you seen your desk? It's a masterpiece of chaos!" , "Are you wearing sunglasses indoors because you're a celebrity, or is it just to hide those tired eyes?" , "I can't believe how much you love coffee. Is it your lifeline, or did you just marry a coffee machine?" , "You know, I envy your ability to take naps anywhere. I'm starting to think you might be part cat." , "I heard you tried singing in the shower again. Next time, let me know so I can bring some earplugs!" , "Your texting speed is impressive – I'm pretty sure your thumbs have their own gym membership." , "I think your fashion sense is ahead of its time. It's like you're living in the year 3010!" , "You have such a great sense of direction. As long as we're not trying to get somewhere, we'll be fine!" , "If genius skips a generation, your children will be brilliant." , "Whatever doesn’t kill you, disappoints me." , "You’re my favorite person… besides every other person I’ve ever met. " , "I hope your wife brings a date to your funeral." , "You’re about as useful as a screen door on a submarine." , "If you were an inanimate object, you’d be a participation trophy." , "I can’t wait to spend my whole life without you." , "Take my lowest priority and put yourself beneath it." , "You are what happens when women drink during pregnancy.", "I don’t hate you, but if you were drowning, I would give you a high five." , "Were you born on the highway? That is where most accidents happen." , "Unless your name is Google, stop acting like you know everything!" , "I didn’t mean to offend you… but it was a huge plus." , "There is someone out there for everyone. For you, it’s a therapist." , "Sorry I can’t think of an insult dumb enough for you to understand." , "You are the sun in my life… now get 93 million miles away from me." , "I would smack you, but I’m against animal abuse." , "I don’t know what makes you so stupid, but it works." , "That sounds like a you problem." , "I believed in evolution until I met you." , "Whoever told you to be yourself, gave you a bad advice." , "You have such a beautiful face… But let’s put a bag over that personality.","I envy people who have never met you." , "If I throw a stick, will you leave me too?" , "I don’t have the time or the crayons to explain this to you." , "You’re impossible to underestimate.", "People like you are the reason God doesn’t talk to us anymore." , "When I look at you, I wish I could meet you again for the first time… and walk past.", "You are a pizza burn on the roof of the world’s mouth.", "You're so ugly Santa goes ho ho holy shit!","You're so ugly Bob the builder took one look and said we can't fix that" , "You're so ugly that when you were born the doctor slapped both your parents","You're so ugly your birth certificate is just an apology","You're like the end the end pieces of a loaf of bread,Everybody touches you but nobody wants you ", "I hope you loose weight so there'll be less of youWhere is your off button?","I know you don't like me, and that implies you need better taste.","I'm no an astronomer, but I'm pretty sure the Earth revolves around the sun… not you.","I'd give you a nasty look, but it seems like you've already got one.","Your birth certificate should be rewritten as a letter of apology ", "You haven't changed since the last time I saw you. You really should. " , "Your bad personality is the reason I prefer animals to humans." ," You hear that? It's the sound of me not caring. ","I might be fully vaccinated, but I'm still not going to hang out with you.","You're so annoying, you could make a Happy Meal cry." , "Oh, sorry, did the middle of my sentence interrupt the beginning of yours?" , "You know, you're just not pretty enough to have such an ugly personality.","You just might be why the middle finger was invented in the first place." , "You have a face that makes onions cry." , "Have a nice day… somewhere else." , "You do realize we're just tolerating you, right? " , "Were you born this stupid or did you take lessons?" ,"It's really fun watching you try to understand everything that's being said about you.", "You are even more useless than the 'ueue' in queue." , "The real heroes in this world are the ones who have to live with you." , "Somewhere out there a tree is producing oxygen for you. What a shame." , "Everyone is allowed to act stupid once in a while, but you're really abusing the privilege." , "If you're going to be two-faced, at least make one of them pretty." , "I was today years old when I realized I didn't like you." , "I'm not a nerd; I'm just smarter than you." , " If I had a dollar every time you shut up, I would give it back as a thank you." , "I didn't mean to offend you… but I'll take it as an additional perk." , "I don't want to rain on your parade. I want to summon a typhoon." , "You can't imagine how much happiness you can bring… by leaving the room. " , "I've been called worse things by better men." , "I didn't mean to push your buttons, I was just looking for mute." , "I forgot the world revolves around you. My apologies! How silly of me." , "I'd rather treat a baby's diaper rash than have lunch with you." , "I would smack you, but I'm against animal abuse." , "I gave out all my trophies a while ago, but here's a participation award." , "It's all about balance… you start talking, I stop listening.","You're the reason this country has to put directions on shampoo bottles." , "How many licks 'till I get to the interesting part of this conversation?" , "When you start talking, I stop listening." , "I'm listening. I just need a minute to process so much stupid information at once." , "You are like a software update. Every time I see you, I immediately think 'not now." ,"Don't worry… the first 40 years of childhood are always the hardest." , "It's impossible to underestimate you." , "I like the way you comb your hair. It's impressive how you're able to hide the horns." , "If I throw a stick, will you chase it? I really want out of this conversation.","You're the reason gene pools need lifeguards.","I don't know what makes you so stupid, but it's really doing the job.","The truth will set you free. You're the worst. OK, you're free to go.","Do you think your parents realize that they're living proof that two wrongs don't make a right?" ,"Give me a minute; I'm trying to think of an insult simple enough for you to understand!","I know our son got his brains from you because, well, I still have mine.","I've heard a smarter statement come out in a fart.","I look at you and think… two billion years of evolution for this?","I told my therapist about you. She didn't believe me.","Don't be ashamed of who you are. That's a job for your parents.","When I listen to you, I think you really are going to go far. I hope you stay there.","When I see you coming, I get pre-annoyed. I figure it's smart to give myself a head start.","Whoever told you to be yourself gave you bad advice.","I think you just need a high five… in the face… with a chair.","When I look at you, I think to myself where have you been my whole life? And can you go back there?","Light travels faster than sound. It explains why you seemed smart… until I finally heard you speak.","Your secrets are always safe with me. I don't even listen when you share them.","When God made you, you must have been on the bottom of his 'to-do' list.","Everyone brings happiness to a room. I bring happiness when I walk in, and you bring happiness when you leave.","Sweetheart, the only thing bothering me is that thing between your ears.","Your face is fine, but you really should put a bag over that personality.","I would call you an idiot, but it would be an insult to stupid people.","Are you at a loss for words, or did you exhaust your entire vocabulary?","Accidents happen; the proof is sitting right there.","You bring everyone so much joy… when you leave the room.","You're not simply a drama queen. You're the whole royal family.","You're like a gray sprinkle on a rainbow cupcake." ," You are more disappointing than an unsalted pretzel. " , "I can't wait to spend my whole life without you." , "Rolling your eyes isn't going to help you find your brain. ", "It’s not that you’re annoying; it’s just that I’d linken you to the human version of period cramps.","You are gay,go back to your default setting","Roses are red Voilets are blue,Faces like yours Belong in the zoo,Don't be mad I'll be there too,Not in the cage But laughing at you..","Even potatoes are getting smashed but you're not"])
            await self.highrise.chat(f": {user.username} - {roastme}")
          
        if "Deathyear" in message or "deathyear" in message:
            death_year = random.randint(2023, 2100)
            await self.highrise.chat(f" {user.username} IDK when you would die but maybe around: {death_year}")

        if "weddingyear" in message or "Weddingyear" in message:
            wedding_year = random.randint(2023, 2040)
            await self.highrise.chat(f"{user.username} IDK when will the wedding take place but maybe around: {wedding_year} Enjoy🌚")

        if "Iq" in message or "iq" in message:
            iq = random.randint(0, 100)
            if iq <= 10:
               await self.highrise.chat(f" @{user.username} your iq is {iq}% ,Bro you are dumb asf ,lol ")
            elif iq >= 90:
               await self.highrise.chat(f" @{user.username} your iq is {iq}% ,You are clever than most of other dumb bitches in this room")
            elif iq >10 and iq <90:              
               await self.highrise.chat(f"Your ( {user.username} ) iq is : {iq}%")

        if "Lovepercentage" in message or "lovepercentage" in message:
            love_percentage = random.randint(0, 100)
            if love_percentage == 100:
                await self.highrise.chat(f" {user.username} {love_percentage}% Everyone loves ya")
            elif love_percentage == 0:
                await self.highrise.chat(f" {user.username} {love_percentage}% No one loves ya,Go cry in that corner ")
            elif love_percentage <100 or love_percentage >0:
                await self.highrise.chat(f" {user.username} Only {love_percentage}% People loves ya!!")
          
        if "Hatepercentage" in message or "hatepercentage" in message:
            hate_percentage = random.randint(0, 100)
            if hate_percentage == 0:
                await self.highrise.chat(f" {user.username} {hate_percentage}% No one hates ya")
            elif hate_percentage == 100:
                await self.highrise.chat(f" {user.username} {hate_percentage}% Everyone hates ya,Go cry in that corner ")
            elif hate_percentage < 100 or hate_percentage > 0:
                await self.highrise.chat(f" {user.username} Only {hate_percentage}% people hates ya")
          
        if "Straightmeter" in message or "straightmeter" in message:
            straight_metre = random.randint(0,100)
            if straight_metre <=10:
                await self.highrise.chat(f"{user.username} {straight_metre}% Why are you Gay?? ")
            elif straight_metre <50:
                await self.highrise.chat(f"{user.username} {straight_metre}%  YOU ARE GAY!!!")
            elif straight_metre ==50:
                await self.highrise.chat(f"{user.username} {straight_metre}%  OMG,YOU ARE Bi!!!")
            elif straight_metre <=90:
                await self.highrise.chat(f"{user.username} {straight_metre}%  You are at default setting ")
            elif straight_metre > 90  :
                await self.highrise.chat(f"{user.username} {straight_metre}% You are straighter than my programming code ")
  
    async def stop_continuous_emote(self, user_id: int):
        if user_id in self.continuous_emote_tasks and not self.continuous_emote_tasks[user_id].cancelled():
            task = self.continuous_emote_tasks[user_id]
            task.cancel()
            with contextlib.suppress(asyncio.CancelledError):
                await task
            del self.continuous_emote_tasks[user_id]

    async def send_continuous_emote(self, emote_id: str, user_id: int, delay: float):
        try:
            while True:
                await self.highrise.send_emote(emote_id, user_id)
                await asyncio.sleep(delay)
        except ConnectionResetError:
            print(f"Failed to send continuous emote to user {user_id}. Connection was reset.")
        except asyncio.CancelledError:
            print(f"Continuous emote task for user {user_id} was cancelled.")
        except ResponseError as error:
            if str(error) == "Target user not in room":
                print(f"User {user_id} is not in the room.")
            else:
                raise  # Re-raise the exception if it's not the one we're handling.
    async def send_random_reactions(self, user_id: str, num_reactions: int = 1, delay: float = 1.1) -> None:
        reactions = ["wave","clap","heart","thumbs","wink"]
        for _ in range(num_reactions):
            reaction = random.choice(reactions)
            await self.highrise.react(reaction, user_id)
            await asyncio.sleep(delay)  # Add a delay between reactions

    async def on_user_move(self, user: User, pos: Position) -> None:
        """On a user moving in the room."""
        if user.username == "liarXD":
            await self.highrise.send_emote(
        random.choice(['dance-anime']))
            print(pos)
            # التعامل مع حالة عدم وجود نص في pos
            facing = pos.facing
            print(type(pos))
            x = pos.x
            y = pos.y
            z = pos.z
            facing = pos.facing
            await self.highrise.walk_to(Position(x - 1, y, z - 1, facing))
            print(user.username, pos)
          
