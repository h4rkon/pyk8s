from fastapi import Depends
from fastapi import APIRouter

from ..auth import get_current_active_user
from ..auth import User


router = APIRouter(
    prefix="/greetings",
    responses={404: {"description": "Meaningful description"}},
)


@router.get("/")
async def hello_world(current_user: User = Depends(get_current_active_user)):
    return f'Hi {current_user} - how are you!'
