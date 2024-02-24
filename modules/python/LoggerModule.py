from datetime import datetime

def log(obj: object):
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    print(f"[{hour}:{minute}:{second}] {obj}")