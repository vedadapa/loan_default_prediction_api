from pydantic import BaseModel, Field

class LoanRequest(BaseModel):
    loan_amount: float = Field(..., gt=0, description="Requested loan amount")
    term: int = Field(..., gt=0, le=360, description="Loan tenure in months")
    property_value: float = Field(..., gt=0, description="Property value")
    income: float = Field(..., gt=0, description="Annual income")
    LTV: float = Field(..., gt=0, description="Loan to Value in %")

class LoanResponse(BaseModel):
    default_probability: float
    risk_label: str
    approved: bool
    confidence: float