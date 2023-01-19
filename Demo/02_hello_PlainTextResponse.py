### Running demo: uvicorn 02_hello_PlainTextResponse:application
### URL: http://127.0.0.1:8000

from starlette.responses import PlainTextResponse

# homepage: def as application!
async def application(scope, receive, send):
    assert scope['type'] == 'http'
    response = PlainTextResponse('Welcome to starlette :: PlainTextResponse')
    await response(scope, receive, send)

