from flask import Flask, request, send_from_directory
from PIL import Image
import os

app = Flask(__name__)

@app.route('/resize', methods=['POST'])
def resize_image():
    if 'image' not in request.files:
        return 'No se ha proporcionado ninguna imagen', 400

    image = request.files['image']
    width = int(request.form.get('width', 800))
    height = int(request.form.get('height', 600))

    try:
        img = Image.open(image)
        img = img.resize((width, height))

        # Guarda la imagen redimensionada en un archivo temporal
        output_path = 'output.jpg'  # Nombre fijo para simplificar
        img.save(output_path)

        # Devuelve la imagen redimensionada como respuesta
        return send_from_directory('.', output_path, mimetype='image/jpeg')

    except Exception as e:
        return f'Error al redimensionar la imagen: {e}', 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
