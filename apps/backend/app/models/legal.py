from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class LegalDocument(Base):
    __tablename__ = 'legal_documents'

    id: Mapped[int] = mapped_column(primary_key=True)
    title_az: Mapped[str] = mapped_column(String(300), nullable=False)
    title_en: Mapped[str] = mapped_column(String(300), nullable=False)
    institution: Mapped[str] = mapped_column(String(200), nullable=False)
    status: Mapped[str] = mapped_column(String(50), nullable=False, default='draft')
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    versions: Mapped[list['DocumentVersion']] = relationship(back_populates='document', cascade='all, delete-orphan')


class DocumentVersion(Base):
    __tablename__ = 'document_versions'

    id: Mapped[int] = mapped_column(primary_key=True)
    legal_document_id: Mapped[int] = mapped_column(ForeignKey('legal_documents.id'), nullable=False)
    version_label: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    document: Mapped[LegalDocument] = relationship(back_populates='versions')
    findings: Mapped[list['ReviewFinding']] = relationship(back_populates='version', cascade='all, delete-orphan')


class ReviewFinding(Base):
    __tablename__ = 'review_findings'

    id: Mapped[int] = mapped_column(primary_key=True)
    document_version_id: Mapped[int] = mapped_column(ForeignKey('document_versions.id'), nullable=False)
    norma_ref: Mapped[str] = mapped_column(String(120), nullable=False)
    issue: Mapped[str] = mapped_column(Text, nullable=False)
    risk_level: Mapped[str] = mapped_column(String(20), nullable=False)
    recommendation: Mapped[str] = mapped_column(Text, nullable=False)
    rationale: Mapped[str] = mapped_column(Text, nullable=False)
    review_status: Mapped[str] = mapped_column(String(20), nullable=False, default='draft')

    version: Mapped[DocumentVersion] = relationship(back_populates='findings')
