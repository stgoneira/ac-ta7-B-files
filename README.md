# Proyecto Redimensión de Imágenes

Realizado con:

- Python (probado con versión 3.9)
- Librería Pillow
- Framework Flask

Ejecute el siguiente comando para instalar las librerías:

```
pip install -r requirements.txt
```

Por defecto utiliza el puerto 5000 al ejecutar.

```
python app.py
```

Puede probar el programa con curl de la siguiente manera, reemplazando "imagen.jpg" por el nombre de su archivo y modificando las dimensiones por las deseadas. 

```
curl -X POST -F "image=@imagen.jpg" -F "width=800" -F "height=600" 127.0.0.1:5000/resize
```
