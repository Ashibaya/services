from fastapi import APIRouter

router = APIRouter()

@router.post("/login")
async def getLogin():
    return {'dsd':'asda'}