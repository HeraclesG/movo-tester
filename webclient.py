import json
import websocket

def on_message(ws, message):
    print(f"Received message: {message}")

def on_error(ws, error):
    print(f"WebSocket error: {error}")

def on_close(ws):
    print("WebSocket connection closed")

def on_open(ws):
    print("WebSocket connection opened")
    ws.send(json.dumps({"action": "join", "data": "Hello, server!"}))

ws = websocket.WebSocketApp("ws://136.243.90.46:8082/api/socket/",
                          on_message=on_message,
                          on_error=on_error)
ws.on_open = on_open
ws.run_forever()