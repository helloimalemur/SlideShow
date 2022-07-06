from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__)

@app.route('/')
def upload_page():
    return render_template('index.html')


@app.route('/images', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('images/' + f.filename)
        #f.save( secure_filename(f.filename))
        return 'file uploaded successfully'


if __name__ == '__main__':
    #app.run(debug=True)
    pass