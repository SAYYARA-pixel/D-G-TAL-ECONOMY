from pydantic import BaseModel


class LegalDocumentCreate(BaseModel):
    title_az: str
    title_en: str
    institution: str
    status: str = 'draft'


class LegalDocumentOut(LegalDocumentCreate):
    id: int

    class Config:
        from_attributes = True


class DocumentVersionCreate(BaseModel):
    legal_document_id: int
    version_label: str
    content: str


class DocumentVersionOut(DocumentVersionCreate):
    id: int

    class Config:
        from_attributes = True


class ReviewFindingCreate(BaseModel):
    document_version_id: int
    norma_ref: str
    issue: str
    risk_level: str
    recommendation: str
    rationale: str
    review_status: str = 'draft'


class ReviewFindingOut(ReviewFindingCreate):
    id: int

    class Config:
        from_attributes = True
