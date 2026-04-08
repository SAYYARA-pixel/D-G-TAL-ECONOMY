from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import require_roles
from app.db.session import get_db
from app.models import BurdenAssessment, Permit, RiskIndicator, StateService
from app.schemas.registry import BurdenAssessmentIn, PermitIn, RiskIndicatorIn, StateServiceIn

router = APIRouter(prefix='/registry', tags=['registry'])


@router.get('/services')
def list_services(db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'legal_expert', 'policy_analyst', 'analyst_viewer', 'entrepreneur_user', 'public_user'))):
    return db.query(StateService).all()


@router.post('/services')
def create_service(payload: StateServiceIn, db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'policy_analyst'))):
    obj = StateService(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.get('/permits')
def list_permits(db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'legal_expert', 'policy_analyst', 'analyst_viewer', 'entrepreneur_user', 'public_user'))):
    return db.query(Permit).all()


@router.post('/permits')
def create_permit(payload: PermitIn, db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'policy_analyst'))):
    obj = Permit(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.get('/burden-assessments')
def list_burden_assessments(db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'legal_expert', 'policy_analyst', 'analyst_viewer'))):
    return db.query(BurdenAssessment).all()


@router.post('/burden-assessments')
def create_burden_assessment(payload: BurdenAssessmentIn, db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'policy_analyst'))):
    obj = BurdenAssessment(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.get('/risk-indicators')
def list_risk_indicators(db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'legal_expert', 'policy_analyst', 'analyst_viewer'))):
    return db.query(RiskIndicator).all()


@router.post('/risk-indicators')
def create_risk_indicator(payload: RiskIndicatorIn, db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'policy_analyst'))):
    obj = RiskIndicator(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
