from fastapi import Depends, FastAPI, Header, HTTPException, requests, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from routers import admin, api
from starlette.middleware.cors import CORSMiddleware
from dependencies import get_token_header, get_query_token
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

templates = Jinja2Templates(directory="app/templates")


def render_template(templateurl, request, obj):
    return templates.TemplateResponse(templateurl, {"request": request, "objects": obj})


@app.get('/')
async def hello():
    return {"greating": "Hello"}


@app.post('/auth')
async def get_token():
    return {"x-token": "fake-super-secret-token"}


@app.get('/auth', response_class=HTMLResponse)
async def show_auth_page(request: Request):
    return templates.TemplateResponse("login_page.html", {"request": request})

app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

app.include_router(admin.router)
app.include_router(api.router)


if __name__ == "__main__":
    uvicorn.run("run:app", host="127.0.0.1", port=5000,
                log_level="info", debug=True)
