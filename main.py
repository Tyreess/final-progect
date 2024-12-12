from fastapi import FastAPI

toors = [
    {
        'id': 1,
        'country': 'Franche',
        'price': 10000
}
]

app = FastAPI(
    description='first site'
)

@app.get('/')
def index():
    return {'status': 200}

@app.get('/toor/{toor_id}')
def toor(toor_id: int):
    for toor in toors:
        if toor_id == toor['id']:
            return toor
    return {}
