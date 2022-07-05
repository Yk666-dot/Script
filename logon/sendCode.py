import phoneName
import requests
import json
phone = phoneName.phone()
headers = {
    'User-Agent': 'Apipost client Runtime/+https://www.apipost.cn/',
}

data = {
  'phone': phone
}

response = requests.post('https://account.21cp.work/register/api/sendPhoneCode', headers=headers, data=data)
print(json.dumps(json.loads(response.text), ensure_ascii=False, indent=4, separators=(',', ':')))
