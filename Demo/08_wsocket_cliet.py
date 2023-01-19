import asyncio 
import websockets

async def message():
    async with websockets.connect("ws://127.0.0.1:8000/ws") as socket:
        msg = input("Message to send: ")
        await socket.send(msg)
        print(await socket.recv())

asyncio.get_event_loop().run_until_complete(message())

## client
## (env) ➜  Demo git:(main) ✗ python 06_wsocket_client.py 
## Message to send: Miguel
## Hello WebSocket!!

## Server
## INFO:     ('127.0.0.1', 54015) - "WebSocket /" [accepted]
## INFO:     connection open
## INFO:     connection closed
