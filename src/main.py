# -*- coding: utf-8 -*-
from __future__ import print_function

from email.message import Message
import os
import random
import uuid
import time
from random import randint
from pathlib import Path
from environs import Env
from pyrogram import Client, filters
from pyrogram.raw.functions.account import ReportPeer
from pyrogram.raw.types import InputPeerChannel, InputReportReasonSpam
from googleapiclient import discovery
from googleapiclient.errors import HttpError

from __version__ import __version__

env = Env()

env.read_env()  # read .env file, if it exists

api_id = env.int('API_ID')
api_hash = env.str('API_HASH')
session_path = Path('session')

MAX_REPORT_AMOUNT = 30

print(f"ВЕРСІЯ: {__version__}")

def main():
    try:
        service = discovery.build('sheets', 'v4', discoveryServiceUrl=
        'https://sheets.googleapis.com/$discovery/rest?version=v4',
        developerKey='AIzaSyBuJc3ghYiaLuV3nlWMDYIb8g0DMOejy-Q')
        result = service.spreadsheets().values().get(spreadsheetId='1ovusoIost6DZt5dwGWWMPRndtLWe-7zoAsbdeo9aK5A', range='Telegram!A1:A').execute()
        values = result.get('values', [])
        ids=[]
        if not values:
            print('No data found.')
            return ids
       
        for row in values:
            ids.append(row[0])
        return ids
    except HttpError as err:
        print(err)

def on_start():
    try:
        if session_path.exists():
            with open(session_path) as file:
                session_string = file.read()

            if not session_string:
                os.remove(session_path)
                print("The old configuration has been removed")
                print("Restart the program to start using")
                exit()
            return Client(session_string, api_id, api_hash)

        else:
            with Client(uuid.uuid4().hex, api_id, api_hash) as tmp_app:
                with open(session_path, 'w') as file:
                    session_string = tmp_app.export_session_string()
                    file.write(session_string)  # noqa

        print("The program is configured")
        print("Restart the program to start using")
        input("press enter to close")
        exit()
    except Exception as e:
        exit()
        

app = on_start()

def cmd_report(client, message):#
    print("Export feed file ...")
    client.send_message("me", "Exporting feed file ...")

    print("💁‍♂️ Starting Bot")
    client.send_message("me", "💁‍♂️ Starting Bot")
    ids = main()

    random.shuffle(ids)  # Shuffle the channel list
    limited_ids = ids[:MAX_REPORT_AMOUNT]  # We take the first 30 channels from the shuffled list
    length = len(limited_ids)

    for _, i in enumerate(limited_ids, start=1):
        try:
            randS = randint(8,16) 
            peer: InputPeerChannel =  client.resolve_peer(i)
            response =  client.send(data=ReportPeer(peer=peer, reason=InputReportReasonSpam(), message="Тероризм (Terrorism)"))
            print(f"[{_}/{length}] Channel {i} received a complaint, {response}")
            client.send_message("me", f"[{_}/{length}] Channel {i} received a complaint, {response}, sleeping... {randS}s")

        except Exception as exc:
            print(exc)
            #input("10")

        finally:
            print(f"sleeping... {randS}s") 
            time.sleep(randS)
             
    app.disconnect()
    exit()


app.connect()
cmd_report(app.session.client,message='')


#app.quit()
#app.run()

