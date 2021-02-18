from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Response

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")

def check_auth(token):
    return True if token else False


def render_template(templateurl, request, obj):
    return templates.TemplateResponse(templateurl, {"request": request , "objects" :obj }) 

@router.get("/", response_class=HTMLResponse)
async def hello(request: Request):       
    print(request.cookies.get("token"))
    user = {
        'nickname': 'Slava',
        'firstname': 'Vinokurov'
        } 
    return render_template("index.html", request, user)

@router.get("/auth", response_class=HTMLResponse)
async def get_token(request: Request):
    return templates.TemplateResponse("login_page.html", {"request": request})    

@router.get("/{id}", response_class=HTMLResponse)
async def read_item(request: Request, id: str):
    return templates.TemplateResponse("item.html", {"request": request, "id": id})

