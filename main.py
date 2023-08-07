from flask import Flask,request,render_template
import cv2


app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/edit',methods=['POST'])
def edit():
    image = request.form.get('imageInput')
    operation = request.form.get('operations')
    print(image)
    print(operation)
    return "Success"


if __name__ == "__main__":
    app.run(debug=True)