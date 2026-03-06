# Arquitectura MVP FastQR

## Objetivo

Validar en 1–2 semanas una experiencia QR interactiva para mesas de restaurantes, sin registro de cliente.

## Componentes

- `apps/web`: interfaz móvil pública (cliente) y base para admin.
- `apps/api`: API de negocio (sesión, menú, juego, votos, ranking).
- `db/schema.sql`: modelo relacional inicial.

## Flujo principal

1. Cliente escanea QR de mesa.
2. Frontend abre ruta dinámica de restaurante/mesa.
3. Frontend inicia sesión anónima en API.
4. API aplica reglas antiabuso y responde acciones permitidas.
5. Cliente consulta menú, juega, vota y ve ranking.

## Multi-tenant

Cada entidad operacional está asociada a `restaurant_id`.

## Antiabuso

- Límite por sesión.
- Límite por mesa.
- Límite diario por restaurante.
- Cooldown configurable para juego.

## Métricas mínimas

- Escaneos.
- Sesiones iniciadas.
- Partidas jugadas.
- Premios entregados.
- Votos.
