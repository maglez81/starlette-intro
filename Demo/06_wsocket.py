from starlette.websockets import WebSocket

### Running application: uvicorn 06_wsocket:app
async def app(scope, receive, send):
    websocket = WebSocket(scope=scope, receive=receive, send=send)
    await websocket.accept()
    await websocket.send_text("Hello WebSocket!!")
    await websocket.close()

## client
## (env) ➜  Demo git:(main) ✗ python 06_wsocket_client.py 
## Message to send: Miguel
## Hello WebSocket!!

## Server
## INFO:     ('127.0.0.1', 54015) - "WebSocket /" [accepted]
## INFO:     connection open
## INFO:     connection closed