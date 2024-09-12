import json
from websocket_server import WebsocketServer

# Callback function for new client connections
def new_client(client, server):
    print(f"New client connected: {client['address']}")

# Callback function for client messages
def message_received(client, server, message):
    print(f"Client({client['address']}) said: {message}")
    server.send_message_to_all(message)

# Callback function for client disconnections
def client_left(client, server):
    print(f"Client({client['address']}) disconnected")

# Create the WebSocket server
server = WebsocketServer(host='0.0.0.0', port=8000)
server.set_fn_new_client(new_client)
server.set_fn_message_received(message_received)
server.set_fn_client_left(client_left)
server.run_forever()