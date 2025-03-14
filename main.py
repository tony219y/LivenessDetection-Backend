from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from tensorflow import keras
import numpy as np
import cv2


app = FastAPI()

#แก้ติดคอ
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI!"}
@app.get("/hello-test")
def helloTest():
    return {"message": "Hello, tony219y!"}


# import model
model = keras.models.load_model("./final_liveness_detection_model_v3.keras")

@app.post("/liveness")
async def liveness_detection(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = predict_liveness(image_bytes)
    return result

def preprocess_image(image_bytes):
    """ แปลงภาพให้เป็นรูปแบบที่โมเดลสามารถพยากรณ์ได้ """
    np_arr = np.frombuffer(image_bytes, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    # Resize ให้ตรงกับ input ของโมเดล (เช่น 224x224)
    img_resized = cv2.resize(img, (224, 224))
    img_array = img_resized.astype("float32") / 255.0
    img_array = np.expand_dims(img_array, axis=0)  # เพิ่มมิติให้ตรงกับโมเดล
    return img_array


def predict_liveness(image_bytes):
    """ ใช้โมเดล Liveness เช็คว่าภาพเป็นจริงหรือเค้ก """
    img_array = preprocess_image(image_bytes)
    prediction = model.predict(img_array)

    print(prediction[0][0])
    is_real = bool(0.00001 <=prediction[0][0] <= 0.007)
    
    return {"is_real": is_real, "confidence": float(prediction[0][0])}