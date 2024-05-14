import http.client
import mimetypes
from codecs import encode

conn = http.client.HTTPSConnection("prod-vortexapi.zephyr4jiracloud.com")
dataList = []
boundary = 'wL36Yn8afVp8Ag7AmP8qZ0SA4n1v9T'
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=jobName;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("01.日本語管理者が管理画面にログインする"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=jobDescription;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode(""))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=automationFramework;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("JUNIT"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=projectKey;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("GPT"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=versionName;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("SP76 laMonto automation"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=cycleName;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("05.Basic Settings"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=createNewCycle;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("false"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=appendDateTimeInCycleName;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("false"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=folderName;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("01.日本語管理者が管理画面にログインする"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=createNewFolder;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("false"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=appendDateTimeInFolderName;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("false"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=assigneeUser;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("623454e08c349300687d5f43"))
dataList.append(encode('--' + boundary))
dataList.append(encode('Content-Disposition: form-data; name=file; filename={0}'.format('TESTS-admin.basic.5B_A01.xml')))

fileType = mimetypes.guess_type('/Users/kentamiyachi/Desktop/TESTS-admin.basic.5B_A01.xml')[0] or 'application/octet-stream'
dataList.append(encode('Content-Type: {}'.format(fileType)))
dataList.append(encode(''))

with open('/Users/kentamiyachi/Desktop/TESTS-admin.basic.5B_A01.xml', 'rb') as f:
    dataList.append(f.read())
    dataList.append(encode('--' + boundary))
    dataList.append(encode('Content-Disposition: form-data; name=mandatoryFields;'))

dataList.append(encode('Content-Type: {}'.format('text/plain')))
dataList.append(encode(''))

dataList.append(encode("Fupi"))
dataList.append(encode('--'+boundary+'--'))
dataList.append(encode(''))
body = b'\r\n'.join(dataList)
payload = body
headers = {
    'accessKey': 'ZDM1ZDY5NTQtMmNmNS0zMmQ5LWEzM2QtYTljMGQyMzU0MDdiIDYyMzQ1NGUwOGMzNDkzMDA2ODdkNWY0MyBVU0VSX0RFRkFVTFRfTkFNRQ',
    'jwt': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI2MjM0NTRlMDhjMzQ5MzAwNjg3ZDVmNDMiLCJxc2giOiI3OGYwMzY3M2NhYzM0NTEyNzk0MDlhMjJiOGZhZWI2MWE0NDUzNDMwMWI0NWE0MDQ0YjY4OWY2ZTU2NDAzNDNkIiwiaXNzIjoiWkRNMVpEWTVOVFF0TW1ObU5TMHpNbVE1TFdFek0yUXRZVGxqTUdReU16VTBNRGRpSURZeU16UTFOR1V3T0dNek5Ea3pNREEyT0Rka05XWTBNeUJWVTBWU1gwUkZSa0ZWVEZSZlRrRk5SUSIsImV4cCI6MTcxNTQ0NDgyMiwiaWF0IjoxNzE1NDA4ODIyfQ.5jubLGAH29eYNOx3UYGz7WR1ROTEgR8RCk5DSH65Ja0',
    'Content-type': 'multipart/form-data; boundary={}'.format(boundary)
}
conn.request("POST", "/api/v1/automation/job/saveAndExecute", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))