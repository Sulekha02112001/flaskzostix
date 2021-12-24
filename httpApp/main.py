import boto3
from flask import jsonify
from flask import Flask, request
from flask.templating import render_template
app = Flask(__name__)


@app.route('/')
def home():
    s3_client = boto3.client('s3', aws_access_key_id='AKIATJZDC6CLFZY4R56Q',
                             aws_secret_access_key='/ 5xxf+KQxngou8wXx/RJIOPCPipb+8mif+RBh5/R',)
    response = s3_client.get_object(
        Bucket='helmrepo', Key='charts/index.yaml')
    data = response['Body'].read()
    return render_template('search.html', data=data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
