from utils import TlsClientUtils

def get_all_channels(token: str, guild_id: int):
    session = TlsClientUtils.get_new_session("chrome120", True)

    header = {
        'authorization': token
    }

    res = session.get(
        f'https://discord.com/api/v9/guilds/{guild_id}/channels',
        headers=header
    )

    channel_id_list = []
    valid_channel_id_list = []

    if res.status_code == 200:
        channels = res.json()
        for data in channels:
            channel_id = data['id']
            channel_id_list.append(channel_id)

        for id in channel_id_list:
            res_typing = typing(token=token, channel_id=id)

            if res_typing.status_code == 204:
                valid_channel_id_list.append(id)
    
    return valid_channel_id_list

def typing(token: str, channel_id: int):
    session = TlsClientUtils.get_new_session("chrome120", True)

    header = {
        'authorization': token
    }

    res = session.post(
        f"https://discord.com/api/v9/channels/{channel_id}/typing",
        headers=header
    )

    return res

def send(message: str, token: str, channel_id: int):
    session = TlsClientUtils.get_new_session("chrome120", True)

    header = {
        "authorization": token
    }

    payload = {
        "content": message
    }

    res = session.post(
        f"https://discord.com/api/v9/channels/{channel_id}/messages",
        headers=header,
        json=payload
    )

    return res

def delete(token: str, channel_id: int, message_id: int):
    session = TlsClientUtils.get_new_session("chrome120", True)

    header = {
        "authorization": token
    }

    res = session.delete(
        f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}",
        headers=header
    )

    return res