from pydantic import BaseModel, Field


class SessionStartRequest(BaseModel):
    table_token: str = Field(min_length=6, max_length=255)


class SessionStartResponse(BaseModel):
    session_id: str
    restaurant_slug: str
    table_code: str


class MenuItem(BaseModel):
    id: str
    name: str
    category: str
    price: float


class PlayGameRequest(BaseModel):
    session_id: str


class PlayGameResponse(BaseModel):
    win: bool
    reward: str | None = None


class VoteRequest(BaseModel):
    session_id: str
    item_id: str


class VoteResponse(BaseModel):
    accepted: bool
