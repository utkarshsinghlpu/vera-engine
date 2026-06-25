%%writefile README.md
# Vera Message Engine

## Features
- Deterministic message composition
- Trigger-based routing
- Merchant-aware messaging
- Single CTA per message
- Suppression key support

## Supported Triggers
- research_digest
- regulation_change
- perf_spike
- perf_dip
- festival_upcoming
- recall_due

## API Endpoints
GET /v1/healthz
GET /v1/metadata
POST /v1/context
POST /v1/tick
POST /v1/reply

## Determinism
The same input always produces the same output.
