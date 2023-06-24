import uvicorn
from fastapi import FastAPI
from src.logger import logger
from src.log_middleware import LogMiddleware

app = FastAPI()
app.add_middleware(LogMiddleware)

@app.get("/")
async def hello():
    logger.info("Hello")
    return "Hello World"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_config=None)
