from fastapi import FastAPI

app = FastAPI(
    description='first site'
)

@app.get('/')
def index():
    return {'status': 200}
