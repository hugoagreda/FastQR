from fastapi import FastAPI

from app.config import settings
from app.routes.admin import router as admin_router
from app.routes.public import router as public_router

app = FastAPI(title=settings.app_name)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "env": settings.app_env}


app.include_router(public_router)
app.include_router(admin_router)
