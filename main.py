# main.py
from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from schema import LoanRequest, LoanResponse
from model_loader import predict_default_probability, load

@asynccontextmanager
async def lifespan(app: FastAPI):
    load()          # runs at startup
    yield           # server is running
                    # anything after yield runs at shutdown

app = FastAPI(title="Loan Default Predictor", version="1.0", lifespan=lifespan)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=LoanResponse)
async def predict(request: LoanRequest) -> LoanResponse:
    try:
        result = predict_default_probability(request.model_dump())
        return LoanResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
