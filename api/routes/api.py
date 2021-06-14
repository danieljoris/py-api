from fastapi import APIRouter

from api.routes import posts

apiRouter = APIRouter()

API_PREFIX = "/api"

apiRouter.include_router(posts.router, prefix=posts.PREFIX)
