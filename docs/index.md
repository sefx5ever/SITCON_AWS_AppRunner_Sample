# SITCON AWS AppRunner DEMO
### Speaker
1. Nick Chao - 2020 AWS Educate Student Ambassador @AWS 
2. Wyne Tan - 2020 AWS Educate Student Ambassador @AWS 
### Pre-requirements
1. Install [aws-cli](https://aws.amazon.com/tw/cli/) 
2. Set up your aws configuration(AWS_ACCESS_KEY_ID,AWS_SECRET_ACCESS_KEY,AWS_DEFAULT_REGION, etc.)
3. Your github repo or FORK my [sample code](https://github.com/sefx5ever/SITCON-AWS-AppRunner-Sample)

### Reminder
* AWS AppRunner is a new service and it's not available to use promotion credits or AWS Educate to lauch service.

### Hands-on Lab
* Deployed from GitHub
```
- STEP 0: Click "Create service" Button
- STEP 1: Source and deployment
    - Source
        * Repository type : Source code repository
        * Connect to GitHub
            1. Connection Name : <CONNECTION NAME>
            2. Repository : <GITHUB REPOSITORY NAME>
            3. Branch : <PRODUCTION BRANCH>
    - Deployment settings
        * Deployment trigger : Automatic
- STEP 2: Configure build
    - Build settings
        * Configuration file : Configure all settings here
        * Runtime : Python 3
        * Build command : pip install -r requirements.txt
        * Start command : flask run --host=0.0.0.0 --port=8080
        * Port : 8080
- STEP 3: Configure service
    - Service settings
        * Service name : <SERVICE NAME>
        * Virtual CPU & memory : default setting
        * Environment variables
            1. FLASK_APP : <YOUR FLASK MAIN FILENAME>
    - Auto scaling(default setting)
    - Health check(default setting)
    - Security(default setting)
    - Tags(default setting)
- STEP 4: Review and create
- STEP 5: DONE!
```

* Deploy an application as a Docker Image
```
- STEP 0(Amazon ECR): Click "Create repository" Button
- STEP 1: Click "View push commands" and finish the following steps.
- STEP 2: Click "Create service" Button
- STEP 3: Source and deployment
    - Source
        * Repository type : Container registry
        * Provider : Amazon ECR
        * Container image URI : <SELECT YOUR IMAGE AND IMAGE TAG THAT YOU CREATE IN AMAZON ECR>
    - Deployment settings
        * Deployment trigger : Automatic
        * ECR access role : Create new service role
- STEP 4: Configure service
    - Service settings
        * Service name : <SERVICE NAME>
        * Virtual CPU & memory : default setting
        * Port : 80
    - Auto scaling(default setting)
    - Health check(default setting)
    - Security(default setting)
    - Tags(default setting)
- STEP 5: Review and create
- STEP 6: DONE!
```

* Deploy an application to App Runner that integrates with DynamoDB
```
- STEP 0: Click "Create service" Button
- STEP 1: Source and deployment
    - Source
        * Repository type : Source code repository
        * Connect to GitHub
            1. Connection Name : <CONNECTION NAME>
            2. Repository : <GITHUB REPOSITORY NAME>
            3. Branch : <PRODUCTION BRANCH>
    - Deployment settings
        * Deployment trigger : Automatic
- STEP 2: Configure build
    - Build settings
        * Configuration file : Configure all settings here
        * Runtime : Python 3
        * Build command : pip install -r requirements.txt
        * Start command : python main.py
        * Port : 8080
- STEP 3: Configure service
    - Service settings
        * Service name : <SERVICE NAME>
        * Virtual CPU & memory : default setting
        * Environment variables
            1. AWS_ACCESS_KEY_ID : <YOUR AWS ACCESS KEY ID>
            2. AWS_SECRET_ACCESS_KEY : <YOUR AWS SECRET ACCESS KEY>
            3. AWS_DEFAULT_REGION : <YOUR AWS DEFAULT REGION>
    - Auto scaling(default setting)
    - Health check(default setting)
    - Security(default setting)
    - Tags(default setting)
- STEP 4: Review and create
- STEP 5: DONE!
```
### Resources
- [Powerpoint](https://docs.google.com/presentation/d/1MLeWx8w1lDIWftah77KnyZmNYlgGncNf/edit?usp=sharing&ouid=103956914666503291022&rtpof=true&sd=true)
- [SITCON-AWS-AppRunner-Sample-Code](https://github.com/sefx5ever/SITCON-AWS-AppRunner-Sample)
### Power By: AWS Educate
![AWS Educate](https://d1.awsstatic.com/WWPS/AWS_Educate_Logo2.914df33100523a7d60c9c897d79d1cec23cc7e0c.png)
