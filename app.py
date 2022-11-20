import fastapi
from fastapi.templating import Jinja2Templates

from api import api

app = fastapi.FastAPI()
app.include_router(api)

templates = Jinja2Templates(directory='templates')

@app.get('/')
def index(request: fastapi.Request):
    context = {
        'name': 'Olesya',
        'request': request
    }
    return templates.TemplateResponse('index.html', context)
