# Loan Default Prediction API

A production-ready asynchronous backend service built with FastAPI to serve an XGBoost machine learning model for loan default risk evaluation.

## Features
- **Asynchronous Routing:** Uses `async def` to handle multiple incoming requests efficiently at the same time, without blocking system threads.
- **Strict Data Validation:** Powered by Pydantic to enforce data types at the gateway door, automatically catching malformed(incorrect) client requests before model execution.

## API Endpoints
- `POST /predict`: Evaluates loan features and returns the default probability.
- `GET /docs`: Interactive Swagger UI dashboard for testing system payloads(the data being sent from the response).

## Local Setup

1. **Install Dependencies:**
   ```bash
   pip install fastapi uvicorn