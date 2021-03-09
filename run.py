from fastapi import Depends, FastAPI, Header, HTTPException
from fastapi.staticfiles import StaticFiles
from routers import admin, api
from starlette.middleware.cors import CORSMiddleware
from .dependencies import get_token_header, get_query_token
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import uvicorn

app = FastAPI(dependencies = [Depends(get_query_token)])

oath2_scheme = OAuth2PasswordBearer(tokenUrl = 'token')

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post('/token')
async def token(form_data: OAuth2PasswordRequestForm = Depends()):
    return {'access_token': form_data.username + 'token'}

@app.get('/')
async def index(token: str = Depends(oath2_scheme)):
    return {'the_token': token}

app.mount("/app/static", StaticFiles(directory="app/static"), name="static")

app.include_router(admin.router)
app.include_router(api.router)


if __name__ == "__main__":
    uvicorn.run("run:app", host="127.0.0.1", port=5000,
                log_level="info", debug=True)
