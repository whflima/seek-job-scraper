from fastapi import FastAPI
from mangum import Mangum
import uvicorn


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

handler = Mangum(app)

if __name__ == "__main__":
   uvicorn.run(app, host="0.0.0.0", port=8080)