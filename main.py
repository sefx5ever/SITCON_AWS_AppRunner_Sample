from flask import request,Flask
from waitress import serve
import boto3
import os

app = Flask(__name__)

@app.route("/",methods=['GET'])
def hello_world():
    return """
        <h1>AWS AppRunner</h1>
        <h4>大規模生產型 Web 應用程式簡化開發人員的工作</h4>
        <p>AWS App Runner 是一項全受管的服務，可讓開發人員輕鬆快速地大規模部署容器化 Web 應用程式和 API，而無需事先具備基礎設施經驗。從原始程式碼或容器映像開始。App Runner 會自動建置和部署 Web 應用程式，並透過加密來負載平衡流量。App Runner 還會自動擴展或縮減以滿足您的流量需求。藉助 App Runner，您不必考慮伺服器或擴展性，而可以將更多時間專注于應用程式。</p>
        <a href="https://aws.amazon.com/tw/apprunner/">AWS AppRunner 官方網站</a>
    """

@app.route("/checkIn",methods=['GET'])
def check_in():
    dynamodb = boto3.resource(
        'dynamodb',
        aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID'],
        aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
    )
    table = dynamodb.Table('sitcon-aws-apprunner-wyne-db')

    datetime = request.args.get('datetime')
    name = request.args.get('name')

    response = table.put_item(
        Item={
            'datetime': int(datetime),
            'name': str(name)
        }
    )
    return response

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8080)