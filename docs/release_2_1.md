# Release 2.1

## Features

- Added email notifications
- Improved deployment pipeline

## Bug Fixes

- Fixed login timeout issue
- Fixed database migration bug

## Rollback

Run:

```bash
kubectl rollout undo deployment/api
```