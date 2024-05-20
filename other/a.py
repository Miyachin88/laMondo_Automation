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

jobID_list = ['3329EB4E583E20643FFDB2BECB77B8501D65D37AEABCCB22A083B0E9277DB54D', 
                'CF09DDD8798FA338DD7F7677B4B4DFD49BFF65874916EE0B453CC3EB6CE9F277',
                '9EB4C59EA42E6B07362E8EEB9991DAAB0CB952A3C74439208D367D6BED4E9C41', 
                '9A95825F3B2F587950127D890A32F1D031C858865C24717CDAB652371A644F91']
jobName_list = ['6W_A01', '6W_A02', '6W_A03', '6W_A04']
folderName_list = ['01.ウィジェットの新規作成', '02.新規ウィジェット作成①', '03.新規ウィジェット作成②', '04.新規ウィジェット作成③']

def updatjob(jobID_listN, jobName_listN, folderName_listN):
    job_ID = jobID_listN
    job_Name = jobName_listN
    folder_Name = folderName_listN
    
    conn = http.client.HTTPSConnection("prod-vortexapi.zephyr4jiracloud.com")
    dataList = []
    boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=jobId;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("{{job_ID}}"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=jobName;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("{{job_Name}}"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=automationFramework;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("JUNIT"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=cycleName;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("06.Widget Settings"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=folderName;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("{{folder_Name}}"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=versionName;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("SP77 laMonto automation"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=cycleStartingDate;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("2024-05-14"))
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=cycleEndingDate;'))

    dataList.append(encode('Content-Type: {}'.format('text/plain')))
    dataList.append(encode(''))

    dataList.append(encode("2024-05-28"))
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
    dataList.append(encode('Content-Disposition: form-data; name=file; filename={0}'.format('TESTS-admin.widget.6W_A01.xml')))

    fileType = mimetypes.guess_type('/Users/kentamiyachi/Desktop/untitled folder/result/TESTS-admin.widget.6W_A01.xml')[0] or 'application/octet-stream'
    dataList.append(encode('Content-Type: {}'.format(fileType)))
    dataList.append(encode(''))

    with open('/Users/kentamiyachi/Desktop/untitled folder/result/TESTS-admin.widget.6W_A01.xml', 'rb') as f:
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
        'jwt': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2MjM0NTRlMDhjMzQ5MzAwNjg3ZDVmNDMiLCJxc2giOiI3OGYwMzY3M2NhYzM0NTEyNzk0MDlhMjJiOGZhZWI2MWE0NDUzNDMwMWI0NWE0MDQ0YjY4OWY2ZTU2NDAzNDNkIiwiaXNzIjoiWkRNMVpEWTVOVFF0TW1ObU5TMHpNbVE1TFdFek0yUXRZVGxqTUdReU16VTBNRGRpSURZeU16UTFOR1V3T0dNek5Ea3pNREEyT0Rka05XWTBNeUJWVTBWU1gwUkZSa0ZWVEZSZlRrRk5SUSIsImV4cCI6MTcxNTgwNjI3NSwiaWF0IjoxNzE1NzcwMjc1fQ.HoQlcgygouc1yP7qq6bE_fN6HXlwdFx6NpWj2cUrT5k',
        'accessKey': 'ZDM1ZDY5NTQtMmNmNS0zMmQ5LWEzM2QtYTljMGQyMzU0MDdiIDYyMzQ1NGUwOGMzNDkzMDA2ODdkNWY0MyBVU0VSX0RFRkFVTFRfTkFNRQ',
        'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
    }
    conn.request("PUT", "/api/v1/automation/job/update", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    print(job_ID)
    print(job_Name)

# 配列の長さ分繰り返す
for i in range(len(jobID_list)):
    updatjob(jobID_list[i], jobName_list[i],folderName_list[i])