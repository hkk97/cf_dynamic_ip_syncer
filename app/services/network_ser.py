import urllib.request


class _NetworkSer:
    def __init__(self): pass

    def hasNetwork(self) -> bool:
        try:
            urllib.request.urlopen('http://google.com')
            return True
        except:
            return False


networkSer = _NetworkSer()
