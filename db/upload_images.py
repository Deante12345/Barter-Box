import os
from flask import Flask, request, jsonify
import boto3
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()
s3_client = boto3.client(
    's3',
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key=os.getenv('AWS_SECRET_KEY'),
    region_name='us-east-2'
    )
BUCKET_NAME = 'barterboxbucket'

ALLOWED_EXTENSIONS = {'png', 'jpeg', 'jpg', 'heic', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower()in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload_image():
    if "file" not in request.files:
        return 'Np file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(filename)

        #upload the file to s3
        s3_client.upload_file(filename, BUCKET_NAME, filename)
        file_url = f'https://{BUCKET_NAME}.s3.amazonaws.com/{filename}'

        return jsonify({'url': file_url})
if (__name__) == '__main__':
    app.run(debug=True, host = '127.0.0.1', port=5000)
