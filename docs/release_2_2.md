# Release 2.2

## Features

- Added payment gateway
- Improved dashboard performance

## Known Issues

Payment retry may fail if timeout exceeds 30 seconds.

## Rollback

```bash
helm rollback payment-service
```