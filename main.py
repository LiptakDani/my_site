from fastapi import FastAPI
from routers import site


app = FastAPI()
app.include_router(site.router)
