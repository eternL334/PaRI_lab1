from flask import Flask
from flask import render_template, redirect
from flask import request, url_for
from flask import send_file
from waitress import serve
from werkzeug.utils import secure_filename
import os   
import numpy as np
import cv2 as cv
from algorithm import get_components, get_mask

app = Flask(__name__)
UPLOAD_FOLDER = 'src/static'
n = 0

def make_prediction(lower, upper, size):
    image = cv.imread(os.path.join(UPLOAD_FOLDER, "image.png"))
    mask = get_mask(image, lower, upper)
    n, mask = get_components(mask, size)

    cv.imwrite(os.path.join(UPLOAD_FOLDER, "mask.png"), mask)

    return n 

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/", methods=['POST'])
def index_post():
    global n
    try:
        file = request.files['image']
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        image = cv.imread(os.path.join(UPLOAD_FOLDER, filename))
        os.remove(os.path.join(UPLOAD_FOLDER, filename))
        cv.imwrite(os.path.join(UPLOAD_FOLDER, "image.png"), image)

        lower = np.array([
            request.form.get("lowhue"),
            request.form.get("lowsaturation"),
            request.form.get("lowvalue"),
        ], dtype=np.uint8)

        upper = np.array([
            request.form.get("highhue"),
            request.form.get("highsaturation"),
            request.form.get("highvalue"),
        ], dtype=np.uint8)

        size = int(request.form.get("size"))

        print(lower, upper, size)

        n = make_prediction(lower, upper, size)

        return redirect(url_for('predict'))
    except Exception as e:
        app.logger.warning(f"{e}")
        return redirect(url_for('index'))

@app.route("/predict")
def predict():
    global n
    return render_template("predict.html", n=n)

if __name__ == '__main__':
    app.run(debug=True)
    # serve(app, host='0.0.0.0', port='5000')