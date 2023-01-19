# Doc: https://www.starlette.io/middleware/
# A middleware is an object that wrapps the original application, hence the name. 
# A middle is called between the application and the server. It can modify the response 
# or the environment or route requests to different application objects.


from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.httpsredirect import HTTPSRedirectMiddleware
from starlette.responses import Response
from starlette.routing import Route

async def home(request):
    return Response("Hellow Middelware!!", media_type="text/plain")

routes = [
    Route('/', home)
]

middleware = [
    Middleware(CORSMiddleware, allow_origins=['*']),
]

app = Starlette(routes=routes, middleware=middleware)