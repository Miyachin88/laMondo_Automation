import http.client
import mimetypes
from codecs import encode
import requests

#Update
"""
①JWTトークンを取得
"""

# Postリクエストを送信するためのデータ
data = {
	"accessKey":"ZDM1ZDY5NTQtMmNmNS0zMmQ5LWEzM2QtYTljMGQyMzU0MDdiIDYyMzQ1NGUwOGMzNDkzMDA2ODdkNWY0MyBVU0VSX0RFRkFVTFRfTkFNRQ",
	"secretKey":"gMRMlA5lmhDuTF_Mfpv9kg7j2bFir_QE2PV8v5L1pMU",
	"accountId":"623454e08c349300687d5f43"
}

# Postリクエストを送信するURL
url = "https://prod-vortexapi.zephyr4jiracloud.com/api/v1/jwt/generate"

# ヘッダーを定義
headers = {
    "Content-Type": "application/json",
    "Content-Length": "<calculated when request is sent>"
}

# Postリクエストを送信
response = requests.post(url, json=data, headers=headers)

# レスポンスのステータスコードおよびレスポンスボディを表示
#print("Response status code:", response.status_code)
print("Response body:", response.text)


#Update
import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPSConnection("prod-vortexapi.zephyr4jiracloud.com")
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=jobId;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("519618E8E5C22C46014A595BF9E5030CC8D41A9EF2EE286862C51C0728054100"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=jobName;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("5B_A01"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=automationFramework;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("JUNIT"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=cycleName;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("05.Basic Settings"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=folderName;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("01.日本語管理者が管理画面にログインする"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=versionName;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("SP76 laMonto automation"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=cycleStartingDate;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("2024-05-01"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=cycleEndingDate;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("2024-05-14"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=createNewCycle;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("false"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=createNewFolder;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("false"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=file; filename={0}'.format('TESTS-admin.basic.5B_A01.xml')))

fileType = mimetypes.guess_type('/Users/kentamiyachi/Desktop/untitled folder/result/TESTS-admin.basic.5B_A01.xml')[0] or 'application/octet-stream'
dataList.append(encode('Content-Type: {}'.format(fileType)))
dataList.append(encode(''))

with open('/Users/kentamiyachi/Desktop/untitled folder/result/TESTS-admin.basic.5B_A01.xml', 'rb') as f:
    dataList.append(f.read())
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=assigneeUser;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("623454e08c349300687d5f43"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=jobDescription;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode(""))
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
headers = {
'jwt': response.text,
'accessKey': 'ZDM1ZDY5NTQtMmNmNS0zMmQ5LWEzM2QtYTljMGQyMzU0MDdiIDYyMzQ1NGUwOGMzNDkzMDA2ODdkNWY0MyBVU0VSX0RFRkFVTFRfTkFNRQ',
'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
}
conn.request("PUT", "/api/v1/automation/job/update", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))



#Exetute
"""
①JWTトークンを取得2
"""

# Postリクエストを送信するためのデータ
data = {
	"accessKey":"ZDM1ZDY5NTQtMmNmNS0zMmQ5LWEzM2QtYTljMGQyMzU0MDdiIDYyMzQ1NGUwOGMzNDkzMDA2ODdkNWY0MyBVU0VSX0RFRkFVTFRfTkFNRQ",
	"secretKey":"gMRMlA5lmhDuTF_Mfpv9kg7j2bFir_QE2PV8v5L1pMU",
	"accountId":"623454e08c349300687d5f43"
}

# Postリクエストを送信するURL
url = "https://prod-vortexapi.zephyr4jiracloud.com/api/v1/jwt/generate"

# ヘッダーを定義
headers = {
    "Content-Type": "application/json",
    "Content-Length": "<calculated when request is sent>"
}

# Postリクエストを送信
response2 = requests.post(url, json=data, headers=headers)

# レスポンスのステータスコードおよびレスポンスボディを表示
# print("Response status code:", response.status_code)
# print("Response body:", response2.text)


conn = http.client.HTTPSConnection("prod-vortexapi.zephyr4jiracloud.com")
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=jobId;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("519618E8E5C22C46014A595BF9E5030CC8D41A9EF2EE286862C51C0728054100"))
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
jwttoken2 = response2.text

headers = {
    'accessKey': 'ZDM1ZDY5NTQtMmNmNS0zMmQ5LWEzM2QtYTljMGQyMzU0MDdiIDYyMzQ1NGUwOGMzNDkzMDA2ODdkNWY0MyBVU0VSX0RFRkFVTFRfTkFNRQ',
    'jwt': jwttoken2,
    'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
}
conn.request("POST", "/api/v1/automation/job/execute", payload, headers)
res = conn.getresponse()
data = res.read()
#print(data.decode("utf-8"))