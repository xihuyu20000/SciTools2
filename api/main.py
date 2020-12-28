
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scrapy import Request
from starlette.responses import JSONResponse, HTMLResponse
from starlette.websockets import WebSocket

app = FastAPI()

# 全局统一异常处理
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except BaseException as e:
        return JSONResponse(status_code=200, content={"status":400,"msg":f"错误信息："+str(e),"data":{}})

# 使用下面这种方式，可以让CORS有效
# app.middleware('http')(catch_exceptions_middleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from api.web.advanced.controller import router as advanced
app.include_router(advanced, prefix='/api/advanced')

from api.web.common.controller import router as common
app.include_router(common, prefix='/api')

from api.web.config.controller import router as config
app.include_router(config, prefix='/api/config')

from api.web.scimetrics.dataset.controller import router as dataset
app.include_router(dataset, prefix='/api/dataset')

from api.web.scimetrics.stat.controller import router as stat
app.include_router(stat, prefix='/api/stat')

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        print(data)
        await websocket.send_text(f"Message text was: {data}")

def start():
    uvicorn.run(app='main:app', host='127.0.0.1', port=8000, reload=True, debug=True, log_level='debug')

if __name__ == '__main__':
    start()
