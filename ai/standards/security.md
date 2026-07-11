# Security Standard

## Authentication and Authorization
- Require authentication for private data.
- Check authorization on the server for every protected action.
- Use least privilege for users, services, and agents.

## Secrets
- Store secrets in approved secret managers or environment configuration.
- Never commit secrets to source control.
- Rotate exposed credentials immediately.

## Data Protection
- Collect only needed data.
- Encrypt sensitive data in transit.
- Protect backups and logs.

## Development
- Review dependencies for vulnerabilities.
- Validate inputs and encode outputs.
- Log security events without leaking private data.
