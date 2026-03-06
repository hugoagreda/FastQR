from fastapi import APIRouter

from app.schemas import (
    MenuItem,
    PlayGameRequest,
    PlayGameResponse,
    SessionStartRequest,
    SessionStartResponse,
    VoteRequest,
    VoteResponse,
)

router = APIRouter(prefix="/public", tags=["public"])


@router.post("/session/start", response_model=SessionStartResponse)
def start_session(payload: SessionStartRequest) -> SessionStartResponse:
    token = payload.table_token
    return SessionStartResponse(
        session_id=f"sess_{token[-8:]}",
        restaurant_slug="demo-restaurant",
        table_code="A1",
    )


@router.get("/menu", response_model=list[MenuItem])
def get_menu() -> list[MenuItem]:
    return [
        MenuItem(id="item_1", name="Hamburguesa Clásica", category="Comida", price=12.5),
        MenuItem(id="item_2", name="Limonada", category="Bebidas", price=4.0),
    ]


@router.post("/game/play", response_model=PlayGameResponse)
def play_game(_payload: PlayGameRequest) -> PlayGameResponse:
    return PlayGameResponse(win=False, reward=None)


@router.post("/votes", response_model=VoteResponse)
def vote(_payload: VoteRequest) -> VoteResponse:
    return VoteResponse(accepted=True)


@router.get("/ranking/daily")
def daily_ranking() -> list[dict[str, str | int]]:
    return [
        {"item_id": "item_1", "name": "Hamburguesa Clásica", "votes": 18},
        {"item_id": "item_2", "name": "Limonada", "votes": 11},
    ]
