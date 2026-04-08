from sqlalchemy import Float, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class StateService(Base):
    __tablename__ = 'state_services'

    id: Mapped[int] = mapped_column(primary_key=True)
    name_az: Mapped[str] = mapped_column(String(250), nullable=False)
    owner_institution: Mapped[str] = mapped_column(String(180), nullable=False)
    legal_basis: Mapped[str] = mapped_column(Text, nullable=False)
    fee_azn: Mapped[float] = mapped_column(Float, default=0)


class Permit(Base):
    __tablename__ = 'permits'

    id: Mapped[int] = mapped_column(primary_key=True)
    name_az: Mapped[str] = mapped_column(String(250), nullable=False)
    authority: Mapped[str] = mapped_column(String(180), nullable=False)
    sector: Mapped[str] = mapped_column(String(120), nullable=False)
    processing_days: Mapped[int] = mapped_column(default=15)


class BurdenAssessment(Base):
    __tablename__ = 'burden_assessments'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(250), nullable=False)
    baseline_hours: Mapped[float] = mapped_column(Float, default=0)
    reform_hours: Mapped[float] = mapped_column(Float, default=0)
    baseline_cost_azn: Mapped[float] = mapped_column(Float, default=0)
    reform_cost_azn: Mapped[float] = mapped_column(Float, default=0)


class RiskIndicator(Base):
    __tablename__ = 'risk_indicators'

    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(80), unique=True, nullable=False)
    name_az: Mapped[str] = mapped_column(String(180), nullable=False)
    weight: Mapped[float] = mapped_column(Float, default=1.0)
    description: Mapped[str] = mapped_column(Text, nullable=False)
