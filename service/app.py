from flask import Flask, request, jsonify, make_response
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import io

app = Flask(__name__)

np.set_printoptions(suppress=True)
model = load_model("converted_keras/keras_model.h5", compile=False)
class_names = open("converted_keras/labels.txt", "r").readlines()


def process_image(image):
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()
    confidence_score = prediction[0][index]
    return class_name, confidence_score


@app.route("/detecta-fungo", methods=["POST"])
def detect_fungo():
    if "file" not in request.files:
        return jsonify({"error": "Nenhuma imagem foi enviada"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "O nome do arquivo está vazio"}), 400

    image = Image.open(io.BytesIO(file.read())).convert("RGB")
    class_name, confidence_score = process_image(image)

    result = {
        "class": class_name[2:],  # Remove o prefixo de índice da classe
        "confidence": f"{confidence_score * 100:.2f}%"
    }

    response = make_response(jsonify(result))
    response.headers["Access-Control-Allow-Origin"] = "*"  # Permite acesso de qualquer origem
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        return "Olá!"
    return "Hello! (GET request)"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
