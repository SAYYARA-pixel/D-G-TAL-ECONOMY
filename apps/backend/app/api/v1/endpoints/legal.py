from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.api.deps import require_roles
from app.db.session import get_db
from app.models import DocumentVersion, LegalDocument, ReviewFinding
from app.schemas.legal import (
    DocumentVersionCreate,
    DocumentVersionOut,
    LegalDocumentCreate,
    LegalDocumentOut,
    ReviewFindingCreate,
    ReviewFindingOut,
)

router = APIRouter(prefix='/legal', tags=['legal'])


@router.get('/documents', response_model=list[LegalDocumentOut])
def list_documents(search: str | None = Query(default=None), db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'legal_expert', 'policy_analyst', 'analyst_viewer'))):
    query = db.query(LegalDocument)
    if search:
        query = query.filter(LegalDocument.title_az.ilike(f'%{search}%'))
    return query.order_by(LegalDocument.id.desc()).all()


@router.post('/documents', response_model=LegalDocumentOut)
def create_document(payload: LegalDocumentCreate, db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'legal_expert'))):
    obj = LegalDocument(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.get('/versions', response_model=list[DocumentVersionOut])
def list_versions(document_id: int, db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'legal_expert', 'policy_analyst', 'analyst_viewer'))):
    return db.query(DocumentVersion).filter(DocumentVersion.legal_document_id == document_id).order_by(DocumentVersion.id.desc()).all()


@router.post('/versions', response_model=DocumentVersionOut)
def create_version(payload: DocumentVersionCreate, db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'legal_expert'))):
    obj = DocumentVersion(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj


@router.get('/findings', response_model=list[ReviewFindingOut])
def list_findings(version_id: int, db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'legal_expert', 'policy_analyst', 'analyst_viewer'))):
    return db.query(ReviewFinding).filter(ReviewFinding.document_version_id == version_id).order_by(ReviewFinding.id.desc()).all()


@router.post('/findings', response_model=ReviewFindingOut)
def create_finding(payload: ReviewFindingCreate, db: Session = Depends(get_db), _: object = Depends(require_roles('super_admin', 'ministry_admin', 'legal_expert', 'policy_analyst'))):
    obj = ReviewFinding(**payload.model_dump())
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj
