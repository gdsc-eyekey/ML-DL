from flask import Flask, jsonify, request, render_template, send_file
import os
import base64
import MLDL_model

UPLOAD_FOLDER = './files' # 파일 저장할 경로
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','mp3']) # 허용할 파일 확장자 모음
 

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload')
def upload_file():
    return render_template('13_upload.html') # 테스트용 폼 (multipart/form-data)

@app.route('/uploader', methods=['GET','POST'])
def uploader_file():
    if request.method == 'POST':
        file1 = request.files['file1']
        filename1 = file1.filename
        file1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1)) 
        file_dir1 = UPLOAD_FOLDER+'/'+filename1

        file2 = request.files['file2']
        filename2 = file2.filename
        file2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2)) 
        file_dir2 = UPLOAD_FOLDER+'/'+filename2

        print(file_dir1)
        print(file_dir2)

        # return send_file(MLDL_model.run_model(os.path.abspath(file_dir)))
        MLDL_model.run_model()
        return send_file(file_dir1)
        