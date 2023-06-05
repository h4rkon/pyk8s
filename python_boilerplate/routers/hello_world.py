from fastapi import APIRouter


router = APIRouter(
    prefix="/greetings",
    responses={404: {"description": "Meaningful description"}},
)


@router.get("/")
async def hello_world():
    return 'Hello World!'
