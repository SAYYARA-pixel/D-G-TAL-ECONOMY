from pydantic import BaseModel


class StateServiceIn(BaseModel):
    name_az: str
    owner_institution: str
    legal_basis: str
    fee_azn: float


class PermitIn(BaseModel):
    name_az: str
    authority: str
    sector: str
    processing_days: int


class BurdenAssessmentIn(BaseModel):
    title: str
    baseline_hours: float
    reform_hours: float
    baseline_cost_azn: float
    reform_cost_azn: float


class RiskIndicatorIn(BaseModel):
    code: str
    name_az: str
    weight: float
    description: str
