from fastapi import FastAPI, Path, HTTPException, Query
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from model.predict import predict_output, model,MODEL_VERSION
import pandas as pd
from schema.prediction_response import PredictionResponse
app = FastAPI()

# human readable
@app.get('/')
def home():
    return {'message':' Insurance premium prediction API'}

#machine readable , aws need this endpoint to check the working of the api
@app.get('/health')
def health_check():
    return {
        'status':'OK',
        'version':MODEL_VERSION,
        ' model_loaded':model is not None
    }

@app.post('/predict', response_model = PredictionResponse) # it is for the output validation
def predict_premium(data : UserInput): # pydantic object type ka data user bhejega
    user_input = {
        'bmi' : data.bmi,
        'age_group' : data.age_group,
        'lifestyle_risk' : data.lifestyle_risk,
        'city_tier' : data.city_tier,
        'income_lpa' : data.income_lpa,
        'occupation' : data.occupation
    }

    try:
        prediction = predict_output(user_input)
        return JSONResponse(status_code =200, content =  {'predicted_category':prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content = str(e))

    
