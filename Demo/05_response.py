
from starlette.responses import Response, HTMLResponse, JSONResponse


### Running application: uvicorn 05_response:app
# http://127.0.0.1:8000
async def app(scope, receive, send):
    assert scope["type"] == "http"
    response = Response('Hello this is a Response using starlette response', media_type='text/plain')
    await response(scope,receive, send)

### Running application: uvicorn 05_response:app_html
async def app_html(scope, receive, send):
    assert scope["type"] == "http"
    response = HTMLResponse('<h1>Hello this is a Response using starlette HTMLResponse</h1>')
    await response(scope,receive, send)

### Running application: uvicorn 05_response:app_json
async def app_json(scope, receive, send):
    assert scope["type"] == "http"
    response = JSONResponse({"Hello":"JSONResponse"})
    await response(scope,receive, send)
