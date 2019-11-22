import requests
import json
import datetime
import random
import string


print("Chuong trinh buff Data Warp+ VPN")
referrer = input("Nhap ID Warp+ Can buff: ")
timesToLoop = int(input("Nhap so GB can buff (nhap 0 lap vo han): "))
retryTimes = 0.5


def genString(stringLength):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


url = 'https://api.cloudflareclient.com/v0a745/reg'


def run():
    install_id = genString(11)
    body = {"key": "{}=".format(genString(42)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "referrer": referrer,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
            "type": "Android",
            "locale": "zh-CN"}

    bodyString = json.dumps(body)

    headers = {'Content-Type': 'application/json; charset=UTF-8',
               'Host': 'api.cloudflareclient.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.12.1'
               }

    r = requests.post(url, data=bodyString, headers=headers)
    return r



if(timesToLoop == 0):
	i = 0
	while (True):
		    result = run()
		    if result.status_code == 200:
		        print("Da tang {}GB cho ID: {}".format(i+1,referrer))
		    else:
		        print(i + 1, "Error")
		        for r in range(retryTimes):
		            retry = run()
		            if retry.status_code == 200:
		                print(i + 1, "Retry #" + str(r + 1), "OK")
		                break
		            else:
		                print(i + 1, "Retry #" + str(r + 1), "Error")
		                if r == retryTimes - 1:
		                    exit()
		    i += 1
elif(timesToLoop != 0):
	for i in range(0, timesToLoop):
		    result = run()
		    if result.status_code == 200:
		        print("Da tang {}GB cho ID: {}".format(i+1,referrer))
		    else:
		        print(i + 1, "Error")
		        for r in range(retryTimes):
		            retry = run()
		            if retry.status_code == 200:
		                print(i + 1, "Retry #" + str(r + 1), "OK")
		                break
		            else:
		                print(i + 1, "Retry #" + str(r + 1), "Error")
		                if r == retryTimes - 1:
		                    exit()
