from fastapi import APIRouter


router=APIRouter(
    prefix="/home",
    tags=["Home"]
)


@router.get('/')
def home():
    return f"Assalomu alaykum!"