### Running demo: uvicorn 01_hello_JSON:app
### URL: http://127.0.0.1:8000

from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

# homepage
async def homepage(request):
    return JSONResponse({"Welcome": "Hello World! JSONResponse"})

# App name
app = Starlette(debug = True, routes = [Route("/", homepage)])

