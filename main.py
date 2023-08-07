from flask import Flask,request,render_template
import cv2
import os
import image_operations as io


app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/edit',methods=['POST'])
def edit():
    image = request.files['imageInput']
    if image:
        filename = os.path.join(app.config['UPLOAD_FOLDER'],image.filename)
        image.save(filename)
        operation = request.form.get('operations')
    
    if operation == "resize":
        io.resize_image(image)

    elif  operation == "blur":
        io.blur_image(image)

    elif operation == "remove background":
        io.remove_background(image)
        
    return "Success"


if __name__ == "__main__":
    app.run(debug=True)