# D-G-TAL Economy Platform (GovTech + LegalTech)

A production-oriented monorepo scaffold for the Ministry of Economy of the Republic of Azerbaijan.

## Phase Summary

### Phase 1 (Architecture and planning)
- Domain-driven modular architecture with backend/frontend separation.
- Bilingual-ready UI architecture (Azerbaijani default, English-ready field pairs).
- Role-based auth and auditable legal review workflow baseline.

### Phase 2 (Core scaffold)
- FastAPI backend with SQLAlchemy models and JWT auth.
- Next.js frontend with institutional layout and module pages.
- Docker Compose with PostgreSQL, backend, frontend.
- Seed script with Azerbaijan-oriented demo content.

### Phase 3 (Core CRUD)
- CRUD/list endpoints for legal documents/versions/findings.
- CRUD/list endpoints for services, permits, burden assessments, and risk indicators.

## Repository Structure

- `apps/backend`: FastAPI services, domain models, API, tests, seeds.
- `apps/frontend`: Next.js TypeScript + Tailwind web UI.
- `docs/architecture.md`: Target architecture and roadmap.
- `docs/developer-notes.md`: Engineering assumptions and next steps.
- `infra/docker`: Container definitions.

## Quickstart

```bash
cp .env.example .env
docker compose up --build
```

Backend: `http://localhost:8000`  
Frontend: `http://localhost:3000`

Seed data (local backend run):

```bash
cd apps/backend
python scripts_seed.py
```

Default admin:
- Email: `admin@economy.gov.az`
- Password: `Admin123!`

## API Highlights

- `POST /api/v1/auth/login`
- `GET /api/v1/legal/documents`
- `POST /api/v1/legal/documents`
- `GET /api/v1/legal/versions?document_id=...`
- `POST /api/v1/legal/versions`
- `GET /api/v1/legal/findings?version_id=...`
- `POST /api/v1/legal/findings`
- `GET/POST /api/v1/registry/services`
- `GET/POST /api/v1/registry/permits`
- `GET/POST /api/v1/registry/burden-assessments`
- `GET/POST /api/v1/registry/risk-indicators`

## Example Workflow
1. Login as admin.
2. Open legal documents workspace.
3. Select a legal draft, inspect versions.
4. Open findings table (`norma / issue / risk / recommendation`).
5. Browse permits/services modules.
6. Review burden metrics and risk indicators.
7. Use dashboard KPIs for executive overview.

## Next Modules
- Norm conflict detection rule engine and explainability ledger.
- Redline version diff and article-level annotation editor.
- Service journey visualization.
- Permit recommendation wizard by business activity.
- Compliance scenario analysis reporting.
- Risk heatmaps and inspection scoring explainers.
- Source-grounded RAG for AI legal assistant.
