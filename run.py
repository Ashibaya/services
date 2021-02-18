from fastapi.responses import HTMLResponse
from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from routers import admin
import uvicorn 

app = FastAPI()

app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"],
    responses={404: {"description": "Not found"}},
    )


if __name__ == "__main__":
    uvicorn.run("run:app", host="127.0.0.1", port=5000, log_level="info", debug = True)