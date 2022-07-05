# -*- coding: utf-8 -*-
import requests
import json
import phoneName
import sendCode
from requests.packages.urllib3.exceptions import InsecureRequestWarning


headers = {'Content-Type': 'application/json'}
data = {
    "corpName": phoneName.company(),
    "contactName": phoneName.name(),
    "phone": sendCode.phone,
    "corpIdentities": "",
    "password": "a000000",
    "confirmPassword": "a000000",
    "code": "666666"
}
url = 'https://account.21cp.work/register/api/saveRegisterCorp'
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
response = requests.post(url=url, headers=headers, json=data, verify=False)
print(json.dumps(json.loads(response.text), ensure_ascii=False, indent=4, separators=(',', ':')))
