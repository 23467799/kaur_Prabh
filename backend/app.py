from flask import Flask, request, jsonify
from google.cloud import storage
import os

app = Flask(__name__)

   # Set up Google Cloud Storage
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'inclassproject-424621-7918814364bd.json'
client = storage.Client()
bucket = client.get_bucket('prabh_bucket1')

@app.route('/upload', methods=['POST'])
def upload_file():
   file = request.files['file']
   if not file:
       return 'No file found', 400

   blob = bucket.blob(file.filename)
   blob.upload_from_string(file.read(), content_type=file.content_type)

   return jsonify({'message': 'File uploaded successfully', 'filename': file.filename})

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0')
