
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def home(request: Request):
    """
    displays the stock screener dashboard / homepage
    """
    return templates.TemplateResponse("home.html", {
        "request": request
    })


@app.post("/stock")
def create_stock():
    """
    created a stock and stores in the database
    """
    return{
        "code":"success",
        "message":"stocked created"
    }



