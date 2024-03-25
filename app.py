from fastapi import FastAPI , Query , Response ,  status
from fastapi.responses import HTMLResponse , RedirectResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(debug=True)
app.mount('/static' , StaticFiles(directory='static') , name="static")

templates = Jinja2Templates(directory="templates")


@app.get('/' , response_class=HTMLResponse)
async def index(request : Request):
    context = {'request':request}
    return templates.TemplateResponse("index.html" , context=context)


@app.get('/invite/' , response_class=RedirectResponse)
async def invite():
    return RedirectResponse(url="https://google.com" , status_code=307)

@app.get('/support/' , response_class=RedirectResponse)
async def support():
    return RedirectResponse(url="https://google.com", status_code=307)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run('app:app' , reload=True)