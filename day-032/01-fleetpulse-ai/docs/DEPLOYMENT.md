# Deployment Notes

For local development use Uvicorn. For a controlled pilot, place behind an authenticated reverse proxy, use a managed database, configure TLS, secrets, backups, log retention, and health monitoring. Restrict network access to read-only telemetry ingress. Review industrial network segmentation and site-specific cybersecurity controls before connecting operational equipment.