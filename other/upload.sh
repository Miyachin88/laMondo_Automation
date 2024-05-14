
######################################################################
#  This .sh file demonstrates how to create or update an automation task in Zephyr for Jira Cloud, run this task, and publish test results to Zephyr.
#  Author: SmartBear Software
######################################################################

######################################################################
#  Zephyr base URL.
#  DON'T CHANGE THE CONSTANT BELOW. KEEP IT AS IT IS.
######################################################################
zephyrBaseUrl="https://prod-api.zephyr4jiracloud.com/connect"

#######################################################################
#  Access and secret keys, and user id needed for connection to Zephyr for Jira. 
#  Replace the constants below with values relevant to your project and account.
#######################################################################

# The accessKey and secretKey to access your project. You can find them in your Jira project: Zephyr > API Keys.
accessKey="ZDM1ZDY5NTQtMmNmNS0zMmQ5LWEzM2QtYTljMGQyMzU0MDdiIDYyMzQ1NGUwOGMzNDkzMDA2ODdkNWY0MyBVU0VSX0RFRkFVTFRfTkFNRQ"
secretKey="gMRMlA5lmhDuTF_Mfpv9kg7j2bFir_QE2PV8v5L1pMU"
# Id of the user who will create the automation task. You can find it in Jira.
accountId="557058:623454e08c349300687d5f43"   

#######################################################################
#  Create a JSON Web Token  (required to access Zephyr for Jira).
#  Keep this section as it is.
#######################################################################
echo "Generating a JSOM Web Token ... \n"
curl -o headers -s -d '{  "accessKey": "'"$accessKey"'"  , "secretKey": "'"$secretKey"'" ,"accountId": "'"$accountId"'","zephyrBaseUrl": "'"$zephyrBaseUrl"'","expirationTime":360000}' -H "Content-Type: application/json" -XPOST https://prod-vortexapi.zephyr4jiracloud.com/api/v1/jwt/generate
jwt="$(cat  headers | head -n 1)"
echo "The generated token: \n"
echo $jwt




#######################################################################
#  Define properties of the automation task.
#  Replace the values below with data relevant to your project.
#######################################################################

# Task info
taskName="5B_A01"
taskId="519618E8E5C22C46014A595BF9E5030CC8D41A9EF2EE286862C51C0728054100"                     
taskDescription=""
automationFramework="JUNIT"  
projectKey="GPT"
versionName="SP76 laMonto automation"

# Cycle info
cycleName="05.Basic Settings"
createNewCycle="false"
appendDateTimeInCycleName="false"

# Folder info
folderName="01.日本語管理者が管理画面にログインする"
createNewFolder="false"
appendDateTimeInFolderName="false"
assigneeUser=""

# Name of the test result file
resultPath="TESTS-admin.basic.5B_A01.xml"

mandatoryFields=""

#######################################################################
#  Create an automation task, run it, send test results to Zephyr.
#  Keep this section as it is.
#######################################################################
echo "Creating and running an automation task ..."
curl -o headers -s -v -H "accessKey: $accessKey" -H "jwt: $jwt" -H "Content-Type: multipart/form-data" -H "Content-Type: application/json" -F "jobId=$taskId" -F"jobName=$taskName" -F "jobDescription=$taskDescription" -F "automationFramework=$automationFramework" -F "projectKey=$projectKey" -F "versionName=$versionName" -F "cycleName=$cycleName" -F "createNewCycle=$createNewCycle" -F "appendDateTimeInCycleName=$appendDateTimeInCycleName" -F "folderName=$folderName" -F "createNewFolder=$createNewFolder" -F "appendDateTimeInFolderName=$appendDateTimeInFolderName" -F "assigneeUser=$assigneeUser" -F "file=$resultPath"  -F "mandatoryFields=$mandatoryFields"-XPOST https://prod-vortexapi.zephyr4jiracloud.com/api/v1/automation/job/saveAndExecute
result="$(cat  headers | head -n 1)"
echo "Test results: \n"
echo $result
# END of the "Create task" code