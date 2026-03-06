# Contrato API MVP (borrador)

Base URL local: `http://localhost:8000`

## Health

### `GET /health`
Respuesta:

```json
{
  "status": "ok",
  "env": "development"
}
```

## Público

### `POST /public/session/start`
Body:

```json
{
  "table_token": "token-qr-mesa"
}
```

### `GET /public/menu`
Devuelve lista de items activos.

### `POST /public/game/play`
Body:

```json
{
  "session_id": "sess_xxx"
}
```

### `POST /public/votes`
Body:

```json
{
  "session_id": "sess_xxx",
  "item_id": "item_1"
}
```

### `GET /public/ranking/daily`
Devuelve top de items por votos del día.

## Admin (placeholder)

### `POST /admin/auth/login`

### `GET /admin/analytics/summary`
