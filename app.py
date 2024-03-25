import os
from fastapi import FastAPI , Query , Response ,  status
from fastapi.responses import HTMLResponse , RedirectResponse
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

HADE_INVITE_URL = os.getenv('HADE_INVITE_URL')
HADE_CANARY_INVITE_URL = os.getenv('HADE_CANARY_INVITE_URL')
HADE_SUPPORT_URL = os.getenv('HADE_SUPPORT_URL')
HADE_VOTE_URL = os.getenv('HADE_VOTE_URL')


app = FastAPI(debug=True)
app.mount('/static' , StaticFiles(directory='static') , name="static")

templates = Jinja2Templates(directory="templates")


@app.get('/' , response_class=HTMLResponse)
async def index(request : Request):
    context = {'request':request}
    return templates.TemplateResponse("index.html" , context=context)


@app.get('/invite/' , response_class=RedirectResponse)
async def invite():
    return RedirectResponse(url=HADE_INVITE_URL , status_code=307)

@app.get('/support/' , response_class=RedirectResponse)
async def support():
    return RedirectResponse(url=HADE_SUPPORT_URL, status_code=307)

@app.get('/vote/' , response_class=RedirectResponse)
async def vote():
    return RedirectResponse(url=HADE_VOTE_URL , status_code=307)

@app.get('/documentation/' , response_class=HTMLResponse)
async def documentation(request : Request):
    context = {'request':request}
    return templates.TemplateResponse("docs/index.html",context=context)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run('app:app' , reload=True)