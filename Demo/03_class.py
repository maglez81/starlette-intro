### Running application: uvicorn app_class:app

from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route, Mount, WebSocketRoute
from starlette.staticfiles import StaticFiles

# # http://127.0.0.1:8000
def homepage(request):
    return PlainTextResponse("Application class!")

# http://127.0.0.1:8000/user/me
def user_me(request):
    username = "Miguel"
    return PlainTextResponse(f"Welcome {username}")

# http://127.0.0.1:8000/user/<username>
def user(request):
    username = request.path_params['username']
    return PlainTextResponse(f"Welcome user: {username}")



routes = [
    Route('/', homepage),
    Route('/user/me', user_me),
    Route('/user/{username}', user)
]

app = Starlette(debug=True, routes=routes, on_startup=[startup])