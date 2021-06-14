from fastapi import FastAPI
import uvicorn

from api.routes.api import apiRouter, API_PREFIX

api = FastAPI()

api.include_router(apiRouter, prefix=API_PREFIX)
