import boto3
import json
from flask import Flask, request
from flask.templating import render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search')
def search():
    if request.method == 'GET':
        content = request.args['search']
        s3_client = boto3.client('s3')
        response = s3_client.get_object(
            Bucket='helmrepo', Key=content)
        data = response['Body'].read()
    return render_template('script.html', data=data)


if __name__ == '__main__':
    app.run(host="172.31.37.169", port=8000, debug=True)
