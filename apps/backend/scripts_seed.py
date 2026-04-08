from app.db.base import Base
from app.db.session import SessionLocal, engine
from app.models import BurdenAssessment, DocumentVersion, LegalDocument, Permit, ReviewFinding, RiskIndicator, Role, StateService, User
from app.security.password import hash_password

Base.metadata.create_all(bind=engine)

db = SessionLocal()

roles = {
    'super_admin': ('Super Admin', 'Super Admin'),
    'ministry_admin': ('Nazirlik Admini', 'Ministry Admin'),
    'legal_expert': ('Hüquq eksperti', 'Legal Expert'),
    'policy_analyst': ('Siyasət analitiki', 'Policy Analyst'),
    'analyst_viewer': ('Müşahidəçi analitik', 'Analyst Viewer'),
    'public_user': ('İctimai istifadəçi', 'Public User'),
    'entrepreneur_user': ('Sahibkar istifadəçi', 'Entrepreneur User'),
}
for code, (az, en) in roles.items():
    if not db.query(Role).filter_by(code=code).first():
        db.add(Role(code=code, name_az=az, name_en=en))
db.commit()

admin_role = db.query(Role).filter_by(code='super_admin').one()
if not db.query(User).filter_by(email='admin@economy.gov.az').first():
    db.add(User(full_name='Platform Super Admin', email='admin@economy.gov.az', password_hash=hash_password('Admin123!'), role_id=admin_role.id))

if not db.query(LegalDocument).first():
    doc = LegalDocument(
        title_az='Sahibkarlıq fəaliyyətinin sadələşdirilməsi haqqında layihə',
        title_en='Draft on Simplification of Entrepreneurial Activity',
        institution='Azərbaycan Respublikası İqtisadiyyat Nazirliyi',
        status='in_review',
    )
    db.add(doc)
    db.flush()
    version = DocumentVersion(legal_document_id=doc.id, version_label='v1.0', content='Maddə 1. Məqsəd...')
    db.add(version)
    db.flush()
    db.add(ReviewFinding(document_version_id=version.id, norma_ref='Maddə 3.2', issue='Terminologiya qeyri-dəqiqdir.', risk_level='medium', recommendation='Terminlərin vahid lüğətlə uyğunlaşdırılması.', rationale='Normativ hüquqi aktlarda terminoloji vahidlik tələbi.', review_status='in_review'))

if not db.query(StateService).first():
    db.add(StateService(name_az='İxracatçı sertifikatının verilməsi', owner_institution='İqtisadiyyat Nazirliyi', legal_basis='Nazirlər Kabinetinin 2024-cü il qərarı', fee_azn=45))
if not db.query(Permit).first():
    db.add(Permit(name_az='Qida istehsalı üçün icazə', authority='AQTA', sector='Qida sənayesi', processing_days=20))
if not db.query(BurdenAssessment).first():
    db.add(BurdenAssessment(title='Kiçik restoran qeydiyyatı', baseline_hours=16, reform_hours=7, baseline_cost_azn=320, reform_cost_azn=140))
if not db.query(RiskIndicator).first():
    db.add(RiskIndicator(code='INSP_HYGIENE', name_az='Gigiyena uyğunsuzluğu tarixi', weight=0.35, description='Son 12 ay üzrə gigiyena pozuntuları.'))

db.commit()
db.close()
print('Seed completed')
