from fastapi import FastAPI, Depends

class DatabaseProto:
    async def get_all(self):
        pass

app = FastAPI()

class Dict(DatabaseProto):
    def __init__(self):
        self.items = [i for i in range(10)]

    async def get_all(self):
        return self.items

async def database() -> DatabaseProto:
    return Dict()

@app.get("/items")
async def get_items(
    db: DatabaseProto = Depends(database),
):
    return await db.get_all()
