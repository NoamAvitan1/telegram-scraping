from dotenv import load_dotenv
import os
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
import pandas as pd

load_dotenv()

api_id = os.getenv("api_id")
api_hash = os.getenv("api_hash")

title = input("Enter a Channel Name ")
word = input("Enter a word you want to search ")
limit = None

while True:
    try:
        limit = int(input("Enter numbers of messages "))
        break
    except ValueError:
        print("Invalid number of messages, pleaee enter again ")

with TelegramClient('name', api_id, api_hash) as client:
    messages = client.get_messages(title, limit=limit)
    messages_dict = {"content": [], "id": []}
    for message in messages:
        if message.message is not None and word in message.message:
            messages_dict["content"].append(message.message)
            messages_dict["id"].append(message.id)

    df = pd.DataFrame(messages_dict)
    df.to_excel('output.xlsx', index=False)
    df_read = pd.read_excel('output.xlsx')
