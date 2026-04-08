"""initial schema"""

from alembic import op
import sqlalchemy as sa

revision = '20260408_0001'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('roles', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('code', sa.String(length=50), nullable=False, unique=True), sa.Column('name_az', sa.String(length=120), nullable=False), sa.Column('name_en', sa.String(length=120), nullable=False))
    op.create_table('users', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('full_name', sa.String(length=150), nullable=False), sa.Column('email', sa.String(length=120), nullable=False, unique=True), sa.Column('password_hash', sa.String(length=255), nullable=False), sa.Column('role_id', sa.Integer(), sa.ForeignKey('roles.id'), nullable=False))
    op.create_table('legal_documents', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('title_az', sa.String(length=300), nullable=False), sa.Column('title_en', sa.String(length=300), nullable=False), sa.Column('institution', sa.String(length=200), nullable=False), sa.Column('status', sa.String(length=50), nullable=False))
    op.create_table('document_versions', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('legal_document_id', sa.Integer(), sa.ForeignKey('legal_documents.id'), nullable=False), sa.Column('version_label', sa.String(length=50), nullable=False), sa.Column('content', sa.Text(), nullable=False))
    op.create_table('review_findings', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('document_version_id', sa.Integer(), sa.ForeignKey('document_versions.id'), nullable=False), sa.Column('norma_ref', sa.String(length=120), nullable=False), sa.Column('issue', sa.Text(), nullable=False), sa.Column('risk_level', sa.String(length=20), nullable=False), sa.Column('recommendation', sa.Text(), nullable=False), sa.Column('rationale', sa.Text(), nullable=False), sa.Column('review_status', sa.String(length=20), nullable=False))
    op.create_table('state_services', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('name_az', sa.String(length=250), nullable=False), sa.Column('owner_institution', sa.String(length=180), nullable=False), sa.Column('legal_basis', sa.Text(), nullable=False), sa.Column('fee_azn', sa.Float(), nullable=False))
    op.create_table('permits', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('name_az', sa.String(length=250), nullable=False), sa.Column('authority', sa.String(length=180), nullable=False), sa.Column('sector', sa.String(length=120), nullable=False), sa.Column('processing_days', sa.Integer(), nullable=False))
    op.create_table('burden_assessments', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('title', sa.String(length=250), nullable=False), sa.Column('baseline_hours', sa.Float(), nullable=False), sa.Column('reform_hours', sa.Float(), nullable=False), sa.Column('baseline_cost_azn', sa.Float(), nullable=False), sa.Column('reform_cost_azn', sa.Float(), nullable=False))
    op.create_table('risk_indicators', sa.Column('id', sa.Integer(), primary_key=True), sa.Column('code', sa.String(length=80), nullable=False, unique=True), sa.Column('name_az', sa.String(length=180), nullable=False), sa.Column('weight', sa.Float(), nullable=False), sa.Column('description', sa.Text(), nullable=False))


def downgrade():
    op.drop_table('risk_indicators')
    op.drop_table('burden_assessments')
    op.drop_table('permits')
    op.drop_table('state_services')
    op.drop_table('review_findings')
    op.drop_table('document_versions')
    op.drop_table('legal_documents')
    op.drop_table('users')
    op.drop_table('roles')
