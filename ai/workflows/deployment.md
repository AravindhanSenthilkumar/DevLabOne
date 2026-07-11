# Workflow: Deployment

## Steps
1. Confirm target environment and version.
2. Verify build and tests passed.
3. Review database migrations.
4. Confirm environment variables and secrets.
5. Deploy through the approved pipeline.
6. Run smoke tests.
7. Check logs, metrics, and alerts.
8. Announce deployment status.

## Rollback
- Keep rollback steps documented.
- Know whether database changes are reversible.
- Escalate quickly if user impact is detected.
