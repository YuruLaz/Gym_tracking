from fastapi import APIRouter, FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


router = APIRouter()


@router.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


app.include_router(router, prefix="/api")
