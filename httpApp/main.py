import boto3
from flask import jsonify
from flask import Flask, request
from flask.templating import render_template
app = Flask(__name__)


@app.route('/')
def home():
    s3_client = boto3.client('s3')
    response = s3_client.list_objects(
        Bucket='helmrepo')
    #data = response['Body'].read()
    return render_template('search.html', data=response)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
