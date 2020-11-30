
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.modules.common.controller import router as common
from api.modules.file.controller import router as file
from api.modules.kg.controller import router as kg
from api.modules.stat.controller import router as stat

app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(common, prefix='/api')
app.include_router(file, prefix='/api/file')
app.include_router(kg, prefix='/api/kg')
app.include_router(stat, prefix='/api/stat')

def start():
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True, debug=True)

if __name__ == '__main__':
    start()
