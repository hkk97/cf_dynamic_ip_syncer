from os import environ, path
from dotenv import load_dotenv


class _AppConfig:
    def __init__(self):
        print("[AppConfig]:[__init__]")
        base_dir = path.abspath(path.dirname(__file__))
        load_dotenv(path.join(base_dir, '../.env'))
        self._auth_email = environ.get('CF_AUTH_EMAIL')
        self._auth_key = environ.get('CF_AUTH_KEY')
        self._zone_id = environ.get('CF_ZONE_ID')
        self._dns_id = environ.get('CF_DNS_ID')
        self._file_name = environ.get('FILE_PATH')
        self._domain_name = environ.get('DOMAIN_NAME')

    def auth_email(self): return self._auth_email
    def auth_key(self): return self._auth_key
    def zone_id(self): return self._zone_id
    def dns_id(self): return self._dns_id
    def file_name(self): return self._file_name
    def domain_name(self): return self._domain_name


appConfig = _AppConfig()
