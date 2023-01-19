### Running application: uvicorn 04_request:app

from starlette.requests import Request
from starlette.responses import Response

# http://127.0.0.1:8000
# Result: GET - /
async def app(scope, receive, send):
    assert scope['type'] == 'http'
    request  = Request(scope, receive)
    content = f"{request.method} - {request.url.path}"
    response = Response(content, media_type= 'text/plain')
    await response(scope, receive, send)
