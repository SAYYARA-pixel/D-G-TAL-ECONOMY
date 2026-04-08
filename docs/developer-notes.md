# Developer Notes

## Implementation Notes
- Phase-based delivery applied with a working skeleton and first vertical slice.
- Azerbaijan-centric sample records added in seed script.
- Role catalog includes all required role categories.

## Practical Extensions
- Add `audit_logs` model + middleware for immutable event records.
- Add taxonomies/configuration tables for indicator and policy checks.
- Introduce Celery for asynchronous document parsing and conflict checks.
- Add OpenAPI client generation to share typed contracts with frontend.

## Quality Roadmap
- Add backend service-level tests for auth and legal CRUD.
- Add Playwright smoke tests for dashboard and legal workspace.
- Integrate linting pipelines (`ruff`, `black`, `eslint`, `prettier`) in CI.
