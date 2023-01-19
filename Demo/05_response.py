
from starlette.responses import Response, HTMLResponse, JSONResponse
from starlette.responses import PlainTextResponse, RedirectResponse
from starlette.responses import StreamingResponse
import asyncio


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

### Running application: uvicorn 05_response:app_redirect
async def app_redirect(scope, receive, send):
    assert scope["type"] == "http"
    if scope['path'] != "/":
        response = RedirectResponse(url='/')
    else:
        response = PlainTextResponse("hello PlainTextResponse!!")
    await response(scope,receive, send)


### Running application: uvicorn 05_response:app_streaming
async def slow_moth(min, max):
    yield('<html><body><ul>')
    for num in range(min, max+1):
        yield(f'<li>{num}</li>')
        await asyncio.sleep(0.5)
    yield('</ul></body></html>')

async def app_streaming(scope, receive, send):
    assert scope['type'] == 'http'
    generator = slow_moth(1,10)
    reponse = StreamingResponse(generator, media_type='text/html')
    await reponse(scope, receive, send)