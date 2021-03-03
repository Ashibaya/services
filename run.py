from fastapi.responses import HTMLResponse
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from routers import admin
from routers import api
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, Response, UJSONResponse
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    api.router,
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)


if __name__ == "__main__":
    uvicorn.run("run:app", host="127.0.0.1", port=5000,
                log_level="info", debug=True)
