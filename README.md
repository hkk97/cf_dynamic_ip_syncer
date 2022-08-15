# CF Dynamic IP Syncer
CloudFlare Dynamic IP Syncer, was writteen by python. It aims to sync the local public IP address with [CloudFlare](https://www.cloudflare.com/zh-tw/)'s CDN setting solving the invalid IP issues because of frequently changed IP and record the change of public ip with [CloudFlare](https://www.cloudflare.com/zh-tw/) saving as [ip_records.json](app/ip_records.json).

This script has used the API of [CloudFlare](https://www.cloudflare.com/zh-tw/) to fetch the latest public and fetch the public IP based on internet status.

<p align="center">
     <a href="https://github.com/flutter/flutter/tree/2.10.5" alt="Python">
        <img src="https://img.shields.io/badge/Python-v3.9.7 (stable)-4BC51D.svg?style=flat" /></a>
     <a href="https://github.com/dart-lang/**sdk**/tree/2.16.2" alt="PyCharm">
        <img src="https://img.shields.io/badge/PyCharm-v2021.3.2 (stable)-4BC51D.svg?style=flat" /></a>
     <a alt="VS Code">
        <img src="https://img.shields.io/badge/VS Code-v1.66.2-4BC51D.svg?style=flat" /></a>
</p>

### Project Environment Config on [.env](app/.env)
```python
CF_AUTH_EMAIL: {CloudFlare Auth Email}
DOMAIN_NAME: {Domain Name}
CF_AUTH_KEY: {Your CloudFlare Auth Key}
CF_ZONE_ID: {Your Cloudflare Zone ID}
CF_DNS_ID: {Your DNS ID} 
FILE_PATH: {The file store the ip info}
```

### Environment SETUP
##### Create Python Virtual Environment
```bash
cf_dynamic_ip_tracker$ python3 -m venv .virt
```
###### Activate Virtual Environment
```bash
cf_dynamic_ip_tracker$ source .virt/bin/activate
```
```bash
(.virt)/cf_dynamic_ip_tracker$ python3 -m pip install -r requirements.txt
```
###### Deactivate Virtual Environment
```bash
(.virt) cf_dynamic_ip_tracker$ deactivate
```
###### Records An Environment's Current Package list into requirements.txt
```bash
(.virt) cf_dynamic_ip_tracker$ pip freeze > requirements.txt
```

### [IP Log Records](app/ip_records.json)
#### Format will as below
```python
ips: [] // The List of ip records
cfIP: "" // The IP Address referenced from CloudFlare 
publicIP: "" // The Public Address of Local Network
updatedAt: "" // The Last Updated Time
```

#### ip_records.json
```python
{
    "ips": [
        {
            "cfIP": "180.219.9.52",
            "createdAt": "2022-08-04 20:36:00.159571",
            "publicIP": "182.152.69.229",
            "updatedAt": "2022-08-04 20:36:00.159583"
        },
        {
            "cfIP": "182.152.69.229",
            "createdAt": "2022-08-04 20:36:16.374694",
            "publicIP": "182.152.69.229",
            "updatedAt": "2022-08-04 20:36:16.374707"
        },
    ]
}
```
