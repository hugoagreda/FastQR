# FastQR

FastQR es un micro-SaaS para restaurantes, bares y cafés que convierte cada mesa en una experiencia interactiva vía QR, sin app y sin registro de cliente.

## Propuesta de valor

- Menú digital en segundos.
- Mini-juego (scratch/roulette) con premios pequeños.
- Votación de platos.
- Ranking diario de platos o bebidas más populares.

Todo optimizado para móvil, con experiencia simple y fricción mínima.

## Stack MVP recomendado

- Frontend: Next.js (App Router, mobile-first)
- Backend: FastAPI
- DB: PostgreSQL / Supabase
- Hosting: Vercel (web) + Railway/Render (API)

## Estructura del proyecto

```text
FastQR/
├─ apps/
│  ├─ web/                  # Frontend móvil (Next.js)
│  │  ├─ app/
│  │  │  ├─ r/[restaurantSlug]/t/[tableCode]/page.tsx
│  │  │  ├─ layout.tsx
│  │  │  ├─ page.tsx
│  │  │  └─ globals.css
│  │  ├─ package.json
│  │  ├─ tsconfig.json
│  │  └─ next.config.mjs
│  └─ api/                  # Backend (FastAPI)
│     ├─ app/
│     │  ├─ main.py
│     │  ├─ config.py
│     │  ├─ schemas.py
│     │  ├─ routes/
│     │  │  ├─ public.py
│     │  │  └─ admin.py
│     │  └─ services/
│     │     └─ limits.py
│     ├─ tests/
│     │  └─ test_health.py
│     └─ requirements.txt
├─ db/
│  ├─ schema.sql            # Esquema inicial PostgreSQL
│  └─ migrations/
├─ docs/
│  ├─ architecture.md
│  └─ api-contract.md
└─ .gitignore
```

## Flujos MVP

### Cliente (sin registro)

1. Escanea QR de la mesa.
2. Abre experiencia móvil.
3. Ve menú.
4. Opcional: juega para premio.
5. Opcional: vota platos.
6. Ve ranking diario.

### Restaurante (admin)

1. Configura menú digital.
2. Define reglas de premios y límites.
3. Genera QR por mesa.
4. Consulta métricas de interacción.

## Endpoints MVP (resumen)

### Público

- `GET /health`
- `POST /public/session/start`
- `GET /public/menu`
- `POST /public/game/play`
- `POST /public/votes`
- `GET /public/ranking/daily`

### Admin (placeholder)

- `POST /admin/auth/login`
- `GET /admin/analytics/summary`

## Cómo ejecutar localmente

### 1) Entorno Python (venv)

1. Activar el venv:
  - PowerShell: `.\.venv\Scripts\Activate.ps1`
  - CMD: `.venv\Scripts\activate.bat`

2. Instalar dependencias:
  - `python -m pip install --upgrade pip`
  - `python -m pip install -r requirements.txt`

3. Desactivar al terminar:
  - `deactivate`

API disponible en: `http://localhost:8000`

### 2) Frontend

```bash
cd apps/web
npm install
npm run dev
```

Web disponible en: `http://localhost:3000`

## Variables de entorno sugeridas

Backend (`apps/api/.env`)

```env
APP_ENV=development
APP_NAME=FastQR API
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/fastqr
SECRET_KEY=change-me
```

Frontend (`apps/web/.env.local`)

```env
NEXT_PUBLIC_API_BASE_URL=http://localhost:8000
```

## Roadmap corto (1–2 semanas)

### Semana 1

- CRUD de menú en admin.
- Sesión anónima por mesa.
- Menú público listo para producción.

### Semana 2

- Juego con reglas y límites por mesa/sesión/día.
- Votos + ranking diario.
- Métricas básicas para restaurantes.

## Principios del MVP

- Sin cuentas de cliente.
- Sin integración POS.
- Sin gamificación compleja.
- Prioridad total a velocidad de implementación y validación con restaurantes reales.