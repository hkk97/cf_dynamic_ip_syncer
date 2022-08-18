import requests


class _IPSer:
    def __init__(self): print("[IPTracker]:[__init__]")

    @staticmethod
    def ip() -> str:
        response = requests.get(f"https://ifconfig.co/json")
        if response.ok:
            res = response.json()
            return res['ip']


ipSer = _IPSer()
