from app.resource import router


@router.get("/")
async def hello():
    return {"msg": "hello world"}
