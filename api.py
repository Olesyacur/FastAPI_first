import datetime

import fastapi

api = fastapi.APIRouter(prefix='/api')

@api.get('/')
def api_index():
    '''
    Ручка для главной страницы.
    '''
    return 'API index page'

@api.post('/get_cur_dt')
def get_cur_dt():
    return {'cur_dt': datetime.datetime.now()}
