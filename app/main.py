from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory= "templates")

from app.routes import auth_router

app.include_router(auth_router)

@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse(request, "index.html")

#uvicorn app.main:app --reload

