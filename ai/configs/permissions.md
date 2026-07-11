# Permissions

## Principle
Agents should have the minimum access needed to complete their task.

## Access Levels
- Read-only: inspect docs, code, logs, and requirements.
- Contributor: propose or create changes for review.
- Maintainer: merge approved changes and manage releases.
- Admin: manage secrets, infrastructure, billing, and production settings.

## Restricted Actions
Require human approval for:
- Production deployment.
- Secret changes.
- Permission changes.
- Deleting data.
- Customer communication.
- Legal, financial, or compliance decisions.

## Data Handling
- Do not expose secrets in prompts, logs, screenshots, or documentation.
- Mask customer personal data unless needed for approved debugging.
