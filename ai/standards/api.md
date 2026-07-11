# API Standard

## Design
- Use RESTful resource names.
- Use nouns in routes and HTTP verbs for actions.
- Version public APIs when breaking changes are possible.
- Document APIs with OpenAPI.

## Responses
- Return consistent status codes.
- Use consistent error format.
- Do not expose stack traces or secrets.

## Security
- Authenticate protected routes.
- Authorize by user role and resource ownership.
- Rate limit sensitive endpoints.

## Compatibility
- Avoid breaking clients without migration guidance.
