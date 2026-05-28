from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI(title = "Loan Default Predciton API")

class LoanRequest(BaseModel):
    income: float
    LTV: float
    Credit_Score: float
class LoanResponse(BaseModel):
    default_probability: float

@app.post("/predict")
async def predict(payload: LoanRequest) -> LoanResponse:
    #implementing prediction logic
    return LoanResponse(default_probability=0.5)