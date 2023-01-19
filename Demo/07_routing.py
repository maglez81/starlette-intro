from starlette.applications import Starlette
from starlette.responses import PlainTextResponse
from starlette.routing import Route


async def home(request):
    return PlainTextResponse("Welcome home page!")

async def about(request):
    return PlainTextResponse("This is about page!")


async def users(request):
    username = request.path_params['username']
    return PlainTextResponse(f"Hello {username}")

routes = [
    Route("/", endpoint=home),
    Route('/about', endpoint=about, methods=['GET']), ##   "POST /about HTTP/1.1" 405 Method Not Allowed
    Route('/users/{username}', endpoint=users)
]

app = Starlette(routes=routes)