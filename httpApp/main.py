import boto3
import json
from flask import Flask, request
from flask.templating import render_template
app = Flask(__name__)


@app.route('/')
def home():
    s3 = boto3.client('s3',aws_access_key_id='AKIATJZDC6CLCYPTDHHK',aws_secret_access_key='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')
    response = s3.list_objects(Bucket="helmrepo")
    data = json.dumps(response, indent=4,sort_keys=True, default=str)
    return render_template('search.html', data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
