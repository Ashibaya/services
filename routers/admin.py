from fastapi import Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import APIRouter, Response
from dependencies import get_token_header

router = APIRouter(
    prefix="/admin",
    tags=["admin"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

templates = Jinja2Templates(directory="app/templates")


def render_template(templateurl, request, obj):
    return templates.TemplateResponse(templateurl, {"request": request, "objects": obj})


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
