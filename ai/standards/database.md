# Database Standard

## Modeling
- Use clear table and column names.
- Store one fact in one place.
- Use foreign keys for relational integrity.
- Use timestamps for created and updated records.

## Migrations
- Every schema change requires a migration.
- Migrations must be repeatable in clean environments.
- Include rollback guidance for risky changes.

## Performance
- Add indexes for common filters, joins, and ordering.
- Review slow queries before scaling infrastructure.

## Data Safety
- Protect personal and customer data.
- Avoid storing secrets in application tables.
