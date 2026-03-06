from fastapi import APIRouter

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/auth/login")
def admin_login() -> dict[str, str]:
    return {"message": "login endpoint placeholder"}


@router.get("/analytics/summary")
def analytics_summary() -> dict[str, int]:
    return {
        "scans": 0,
        "sessions": 0,
        "games_played": 0,
        "rewards_claimed": 0,
        "votes": 0,
    }
