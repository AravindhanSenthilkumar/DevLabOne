# Performance Standard

## Frontend
- Keep initial bundles small.
- Lazy-load large features when useful.
- Avoid unnecessary re-rendering.
- Optimize images and assets.

## Backend
- Measure latency before optimizing.
- Avoid repeated database calls in loops.
- Use caching for expensive, repeatable reads.
- Set timeouts for external calls.

## Database
- Index common query paths.
- Avoid returning unused columns.
- Use pagination for large lists.

## Targets
- Define performance targets for critical flows.
- Monitor real production behavior.
