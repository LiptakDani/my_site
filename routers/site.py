from fastapi import APIRouter


router = APIRouter(
    prefix="",
    tags=["Site"],
    responses={404:{"description": "Not found"}},
)

@router.get("/")
def return_index():
    return {"proba": 1}