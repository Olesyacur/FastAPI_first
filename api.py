import fastapi

api = fastapi.APIRouter(prefix='/api')

@api.get('/')
def api_index():
    return 'API index page'