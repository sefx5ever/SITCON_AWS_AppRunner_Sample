# sitcon-aws-apprunner-demo
## STEP 1 : Set up the environment variable on the AppRunner configuration section
```
KEY -> FLASK_APP
VALUE -> main
```

## STEP 2 : Set the start code as below
```
flask run --host=0.0.0.0 --port=8080
```

```
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 274251673384.dkr.ecr.us-east-1.amazonaws.com
waitress-serve --call "main:create_app"
```
