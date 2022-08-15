from hashlib import new
import os.path
from config.app_config import appConfig
import json
from datetime import datetime


class IPRecord:
    def __init__(self, cf_ip, public_ip):
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.cf_ip = cf_ip
        self.public_ip = public_ip

    def dict(self):
        return {
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
            "cfIP": self.cf_ip,
            "publicIP": self.public_ip,
        }


class _RecordSer:
    def __init__(self): pass

    def update(self, cf_ip, public_ip):
        if os.path.isfile(appConfig.file_name()):
            is_empty = True
            json_data = {}
            with open(appConfig.file_name(), 'r+', encoding='utf-8') as _file:
                json_data = _file.read()
                if len(json_data) == 0:
                    json_data = {}
                    json_data.setdefault(
                        "ips", [IPRecord(cf_ip=cf_ip, public_ip=public_ip).dict()])
                    json.dump(json_data, _file, indent=4,
                              sort_keys=True, default=str)
                else:
                    is_empty = False

            if is_empty is False:
                dict_data = eval(json_data)
                ref_ip_record = dict_data['ips'][-1]
                if ref_ip_record['cfIP'] != cf_ip or ref_ip_record['publicIP'] != public_ip:
                    with open(appConfig.file_name(), 'w', encoding='utf-8') as _file:
                        dict_data['ips'].append(
                            IPRecord(cf_ip=cf_ip, public_ip=public_ip).dict())
                        json.dump(dict_data, _file, indent=4,
                                  sort_keys=True, default=str)
                else:
                    pass
        else:
            with open(f"{appConfig.file_name()}", "w",) as _file:
                json_data = {}
                json_data.setdefault(
                    "ips", [IPRecord(cf_ip=cf_ip, public_ip=public_ip).dict()])
                json.dump(json_data, _file, indent=4,
                          sort_keys=True, default=str)


recordSer = _RecordSer()
