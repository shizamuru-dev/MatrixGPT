import json
import g4f
import nest_asyncio
import simplematrixbotlib as botlib

from Config import cfg

nest_asyncio.apply()

config = botlib.Config()
config.encryption_enabled = True
config.emoji_verify = True
config.ignore_unverified_devices = False
config.store_path = './crypto_store/'

creds = botlib.Creds(cfg.homeServer, cfg.botID, cfg.botPassword)
bot = botlib.Bot(creds,config)

def get_provider(name: str):
    if name == "DeepAi":
        return g4f.Provider.DeepAi
    elif name == "Bing":
        return g4f.Provider.Bing
    elif name == "OpenAssistant":
        return g4f.Provider.OpenAssistant
    elif name == "You":
        return g4f.Provider.You
    elif name == "ChatgptAi":
        return g4f.Provider.ChatgptAi

def change_json_provider(room_id: str, provider: g4f.Provider.AsyncProvider):
    storage = open('Storage/data.json', 'r')
    data = json.load(storage)
    data[room_id]['provider'] = provider.__name__
    modify = data

    json_object = json.dumps(modify, indent=4)
    storage.close()
    with open("Storage/data.json", "w") as outfile:
        outfile.write(json_object)
        outfile.close()


def get_json_provider(room_id: str):
    storage = open('Storage/data.json', 'r')
    data = json.load(storage)
    return data[str(room_id)]['provider']

def add_json_room(room_id, gpt, user):
    storage = open('Storage/data.json', 'r')
    data = json.load(storage)
    modify = data | {f"{room_id}": {"dialog": f"promt:{user} answer:{gpt}", "cout": 0}, "provider": "bing"}
    json_object = json.dumps(modify, indent=4)
    storage.close()
    with open("Storage/data.json", "w") as outfile:
        outfile.write(json_object)
        outfile.close()


def check_json_room(room_id):
    storage = open('Storage/data.json', 'r')
    data = json.load(storage)
    try:
        _ = data[room_id]
        return True
    except:
        return False


def modify_json_room(room_id, gpt, user):
    storage = open('Storage/data.json', 'r')
    data = json.load(storage)
    if data[room_id]['cout'] > 20:
        data[room_id]['dialog'] = f" promt: {user} answer: {gpt}"
        data[room_id]['cout'] = 0
    else:
        dialog_old = data[room_id]['dialog']
        data[room_id]['dialog'] = dialog_old + f" promt: {user} answer: {gpt}"
        cout_old = data[room_id]['cout']
        data[room_id]['cout'] = cout_old + 1
    modify = data

    json_object = json.dumps(modify, indent=4)
    storage.close()
    with open("Storage/data.json", "w") as outfile:
        outfile.write(json_object)
        outfile.close()


def get_json_room(room_id):
    storage = open('Storage/data.json', 'r')
    data = json.load(storage)
    return data[room_id]['dialog']


def clear_json_room(room_id):
    storage = open('Storage/data.json', 'r')
    data = json.load(storage)
    data[room_id]['cout'] = 0
    data[room_id]['dialog'] = ""
    json_object = json.dumps(data, indent=4)
    storage.close()
    with open("Storage/data.json", "w") as outfile:
        outfile.write(json_object)
        outfile.close()


@bot.listener.on_message_event
async def clear(room, message):
    match = botlib.MessageMatch(room, message, bot, cfg.PREFIX)
    print(match.prefix())
    if not check_json_room(room.room_id):
        add_json_room(room.room_id, "", "")

    if (not match.prefix()) and (match.is_not_from_this_bot()):
        user_message = match.command() + " " + " ".join(arg for arg in match.args())

        provider = get_provider(get_json_provider(room.room_id))
        history = get_json_room(room.room_id)
        answer = g4f.ChatCompletion.create(
            provider=provider,
            model=g4f.models.gpt_4,
            messages=[{"role": "user",
                       "content": f"{history}      (you should answer as in a normal dialog without, for example, \"Answer:....\", and if you are asked to write code, wrap it in codeblock from markdown)Current issue:{user_message}"}]
        )

        modify_json_room(room.room_id, answer, user_message)
        await bot.api.send_markdown_message(room.room_id, answer.replace("Answer: ", ''))
    elif (match.prefix()) and (match.is_not_from_this_bot() and (match.command("clear"))):
        clear_json_room(room.room_id)
        await bot.api.send_markdown_message(room.room_id, "Message history cleared")
    elif (match.prefix()) and (match.is_not_from_this_bot() and (match.command("deepai"))):
        change_json_provider(str(message.channel.id), g4f.Provider.DeepAi)
        await bot.api.send_markdown_message(room.room_id, "The provider has been successfully changed to: **DeepAI**")
    elif (match.prefix()) and (match.is_not_from_this_bot() and (match.command("bing"))):
        change_json_provider(str(message.channel.id), g4f.Provider.Bing)
        await bot.api.send_markdown_message(room.room_id, "The provider has been successfully changed to: **Bing**")
    elif (match.prefix()) and (match.is_not_from_this_bot() and (match.command("openassistant"))):
        change_json_provider(str(message.channel.id), g4f.Provider.OpenAssistant)
        await bot.api.send_markdown_message(room.room_id, "The provider has been successfully changed to: **OpenAssistant**")
    elif (match.prefix()) and (match.is_not_from_this_bot() and (match.command("you"))):
        change_json_provider(str(message.channel.id), g4f.Provider.You)
        await bot.api.send_markdown_message(room.room_id, "The provider has been successfully changed to: **You**")
    elif (match.prefix()) and (match.is_not_from_this_bot() and (match.command("chatgptai"))):
        change_json_provider(str(message.channel.id), g4f.Provider.ChatgptAi)
        await bot.api.send_markdown_message(room.room_id, "The provider has been successfully changed to: **ChatgptAi**")
bot.run()
