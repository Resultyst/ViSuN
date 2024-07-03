from websocket_server import WebsocketServer
from chatbot import get_response

# Called for every client connecting (after handshake)
def new_client(client, server):
    print(f"Client({client['id']}) connected")

# Called for every client disconnecting
def client_left(client, server):
    print(f"Client({client['id']}) disconnected")

# Called for every message received
def message_received(client, server, message):
    try:
        response = get_response(message)
        server.send_message(client, response)
    except Exception as e:
        print(f"Error handling message: {e}")

# Create a new WebSocket server
server = WebsocketServer(host='0.0.0.0', port=8000)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)

# Run the server
server.run_forever()
