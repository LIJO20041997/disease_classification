from fastapi import FastAPI, File, UploadFile
import uvicorn
import numpy as np 
from io import BytesIO
from PIL import Image
import tensorflow as tf
from keras.models import load_model


MODEL = tf.keras.models.load_model("C:\\Users\\Dinesh\\Desktop\\tomato_disease_classification\\saved_models\\model.keras")
CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]

app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello Im alive"

def read_file_as_image(data)-> np.ndarray:
    image = np.array(Image.open(BytesIO(data)))
    return image


@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    image_batch = np.expand_dims(image,0)
    prediction = MODEL.predict(image_batch)
    index = np.argmax(prediction[0])
    predicted_class = CLASS_NAMES[index]
    confidence = np.max(prediction[0])

    return{
        "class": predicted_class,
        "confidence": float(confidence)
    }

if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8001)