# Architecture Plan

## Target Principles
- Modular domain architecture per regulatory function.
- Secure defaults, role-based access, auditability.
- Bilingual information model (`*_az`, `*_en`).
- Human-in-the-loop legal intelligence with traceable rationale.

## Bounded Contexts
1. Identity & Access
2. Legal Analysis
3. Regulatory Registry (services/permits)
4. Compliance Burden
5. Inspection Risk
6. AI Assistant & Source Governance
7. Admin & Taxonomy

## Runtime Architecture
- **Frontend**: Next.js app router, module pages, reusable table cards.
- **Backend**: FastAPI routers under `/api/v1`, SQLAlchemy models, JWT auth.
- **Database**: PostgreSQL (local compose), migration-ready via Alembic.
- **Storage**: Local first (future S3 abstraction).
- **AI Layer**: planned provider-agnostic adapter + RAG source policies.

## Security Baseline
- Password hashing (bcrypt via passlib).
- JWT bearer tokens.
- Role gate dependencies per endpoint.
- Env-driven secrets and connection strings.

## Current Vertical Slice
- Legal documents + versions + review findings with end-to-end API/UI.

## Risks & Assumptions
- Current migration setup is minimal and should be hardened before production rollout.
- Frontend currently reads token from localStorage; production should use secure httpOnly cookies.
- Conflict engine and AI modules are structured for extension but not fully implemented yet.
