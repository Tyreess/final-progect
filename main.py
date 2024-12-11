from fastapi import FastAPI

app = FastAPI(
    description='first site'
)

@app.get('/')
def index():
    return {'status': 200}

@app.get('/toor')
def toor_int(book_id: int):
    return {'{toor_id}': book_id}


@app.get('/toor/{toor_id}')
def toor_str(book_id: str):
    return {'{toor_id_str}': book_id}