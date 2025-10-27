from fastapi import FastAPI 
import pickle


with open('pipeline_v1.bin', 'rb') as f_in:
    dv, model = pickle.load(f_in)

app = FastAPI()

@app.post('/predict')
def predict(record: dict):
    record_dict = dv.transform(dict(record))
    prediction = model.predict_proba(record_dict)
    return {"prediction": float(prediction[0,1])}
