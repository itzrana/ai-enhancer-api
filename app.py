from flask import Flask, request, send_file
from PIL import Image, ImageEnhance
import io

app = Flask(__name__)

@app.route('/')
def home():
    return 'AI Image Enhancer API is running!'

@app.route('/enhance', methods=['POST'])
def enhance():
    file = request.files['image']
    image = Image.open(file.stream)

    # Simple enhancement: contrast + sharpness
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.5)

    sharpness = ImageEnhance.Sharpness(image)
    image = sharpness.enhance(2.0)

    img_io = io.BytesIO()
    image.save(img_io, 'JPEG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
