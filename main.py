from utils import DiscordUtils
from modules.python import InputModule, LoggerModule
from itertools import product
import time
import random
import sys

user_id_list = []
channel_id_list = []
token_list = []
input_min_delay = 0.0
input_max_delay = 1.0

def load_token():
    global token_list

    with open('data/token.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()

    no_empty_lines = [line.strip() for line in lines if line.strip()]

    with open('data/token.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(no_empty_lines))

    with open('data/token.txt', 'r', encoding='utf-8') as file:
        file.seek(0)
        for line in file:
            token_list.append(line.strip())

    if len(token_list) == 0:
        print("Token is empty")
        time.sleep(5)
        sys.exit()

def input():
    global input_min_delay
    global input_max_delay

    input_user_amount = InputModule.custom_input(int, "User Amount: ")
    input_min_delay = InputModule.custom_input(float, "Min Delay: ")
    if input_min_delay < 0.0:
        input_min_delay = 0.0

    while True:
        input_max_delay = InputModule.custom_input(float, "Max Delay: ")
        if input_max_delay >= input_min_delay:
            break

    global user_id_list
    for i in range(input_user_amount):
        input_user_id = InputModule.custom_input(int, f"User ID ({i}): ")
        user_id_list.append(input_user_id)

    input_all_channel = InputModule.custom_input(bool, "All Channel (True/False): ")

    global channel_id_list
    if input_all_channel == True:
        input_server_id = InputModule.custom_input(int, "Server ID: ")

        channel_id_list = DiscordUtils.get_all_channels(
            token=token_list[0],
            guild_id=input_server_id
        )
    else:
        input_channel_amount = InputModule.custom_input(int, "Channel Amount: ")

        for i in range(input_channel_amount):
            input_channel_id = InputModule.custom_input(int, "Channel ID: ")
            channel_id_list.append(input_channel_id)

def ghost_ping():
    global channel_id_list
    global user_id_list
    global token_list

    pt = product(channel_id_list, user_id_list, token_list)
    for channel_id, user_id, token in pt:
        delay = random.uniform(input_min_delay, input_max_delay)

        res_send = DiscordUtils.send(
            message=f"<@{user_id}>",
            token=token,
            channel_id=channel_id
        )
        LoggerModule.log(f"Send: {res_send.status_code}")

        message_id = res_send.json()['id']

        res_delete = DiscordUtils.delete(
            token=token,
            channel_id=channel_id,
            message_id=message_id
        )
        LoggerModule.log(f"Delete: {res_delete.status_code}")

        time.sleep(delay)

def main():
    load_token()
    input()
    ghost_ping()

if __name__ == "__main__":
    main()