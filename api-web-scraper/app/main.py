from fastapi import FastAPI
from mangum import Mangum
import uvicorn

from app.core.container import Container
from app.api.routes import routers

container = Container()
container.wire(modules=["app.api.endpoints.advertiser"])

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(routers)
handler = Mangum(app)

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8080)