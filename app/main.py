import time
from datetime import datetime
from services.cf_ser import cfSer
from services.ip_ser import ipSer
from services.network_ser import networkSer
from services.record_ser import recordSer


modified_on, cf_ip = cfSer.dns()
public_ip = ipSer.ip()

while True:
    if networkSer.hasNetwork():
        public_ip = ipSer.ip()
        if (cf_ip == public_ip):
            print(f"[{datetime.now()}]:[IP SYNCED]")
        else:
            print(f"[{datetime.now()}]:[IP DOES NOT SYNCED] ---> [Sync IP]")
            modified_on, cf_ip = cfSer.dns()
            cfSer.update_ip(new_ip=public_ip)
            recordSer.update(cf_ip=cf_ip, public_ip=public_ip)
    else:
        print(f"[{datetime.now()}]:[DOES NOT HAVE NETWORK]")
    time.sleep(60)
