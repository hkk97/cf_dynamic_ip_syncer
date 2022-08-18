import requests
from config.app_config import appConfig


class _CloudflareSer:
    def __init__(self):
        self._headers = {
            "X-Auth-Email": appConfig.auth_email(),
            "X-Auth-Key": appConfig.auth_key(),
            "Content-Type": "application/json",
        }

    def update_ip(self, new_ip) -> bool:
        response = requests.put(
            f"https://api.cloudflare.com/client/v4/zones/{appConfig.zone_id()}/dns_records/{appConfig.dns_id()}/", headers=self._headers,
            json={
                "type": "A",
                "name": f"{appConfig.domain_name()}",
                "content": f"{new_ip}",
                "proxied": True,
            }
        )
        return True if response.ok else False

    def dns(self) -> set:
        response = requests.get(
            f"https://api.cloudflare.com/client/v4/zones/{appConfig.zone_id()}/dns_records/", headers=self._headers, )
        if response.ok:
            result = response.json()
            for res in result['result']:
                if res['type'] == 'A' and res['name'] == 'spotlight-platform.com' and res['proxied'] == True:
                    return res['modified_on'], res['content']


cfSer = _CloudflareSer()
