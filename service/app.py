from flask import Flask, jsonify, request
from keras.models import load_model
import numpy as np
import cv2
import io
from PIL import Image


app = Flask(__name__)

# Carrega o modelo e os rótulos
model = load_model("keras_Model.h5", compile=False)
class_names = open("labels.txt", "r").readlines()


def process_image(image):
    # Redimensiona a imagem para 224x224 e converte para numpy array
    image = cv2.resize(image, (224, 224), interpolation=cv2.INTER_AREA)
    image = np.asarray(image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normaliza a imagem
    image = (image / 127.5) - 1

    # Realiza a predição
    prediction = model.predict(image)
    index = np.argmax(prediction)
    class_name = class_names[index].strip()  # Remove espaços em branco
    confidence_score = prediction[0][index]

    # Retorna a classe e a confiança
    return class_name, confidence_score


@app.route("/detecta-fungo", methods=["POST"])
def detect_fungo():
    if "file" not in request.files:
        return jsonify({"error": "Nenhuma imagem foi enviada"}), 400

    file = request.files["file"]
    if file.filename == "":
        return jsonify({"error": "O nome do arquivo está vazio"}), 400

    # Carrega a imagem recebida
    image = Image.open(io.BytesIO(file.read())).convert("RGB")
    image = np.array(image)

    # Processa a imagem e realiza a predição
    class_name, confidence_score = process_image(image)

    # Prepara a resposta
    result = {
        "class": class_name,
        "confidence": f"{confidence_score * 100:.2f}%",
    }
    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
