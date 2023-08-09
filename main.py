from flask import Flask,request,render_template, send_file
import cv2
import os
import image_operations as io


app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = 'processed'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/edit',methods=['POST'])
def edit():
    processed_filename = None
    image = request.files['imageInput']
    if image and allowed_file(image.filename):
        filename = os.path.join(app.config['UPLOAD_FOLDER'],image.filename)
        image.save(filename)
        operation = request.form.get('operations')
    
        if operation == "resize":
            processed_image = io.resize_image(filename)

        elif  operation == "blur":
            processed_image = io.blur_image(filename)

        elif operation == "remove background":
            processed_image = io.remove_background(filename)

        processed_filename = os.path.join(app.config['PROCESSED_FOLDER'],'processed_' + image.filename)
        cv2.imwrite(processed_filename, processed_image)
        os.remove(filename)
        
    return render_template('index.html', processed_filename=os.path.basename(processed_filename))


@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    processed_filename = os.path.join(app.config['PROCESSED_FOLDER'], filename)
    if os.path.exists(processed_filename):
        return  send_file(processed_filename, as_attachment=True)
    else:
        return "File not found"


if __name__ == "__main__":
    app.run(debug=True)