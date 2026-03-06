# FastQR API

Backend del MVP en FastAPI.

## Run

```bash
uvicorn app.main:app --reload --port 8000
```

## Endpoints clave

- `GET /health`
- `POST /public/session/start`
- `GET /public/menu`
- `POST /public/game/play`
- `POST /public/votes`
- `GET /public/ranking/daily`
