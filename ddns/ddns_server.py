# tunnel_server.py
import asyncio
import json

clients = {}

async def handle_client(reader, writer):
    client_id = await reader.readline()

    with open('clients.json', 'r') as file:
        allowed_clients = json.load(file)

    if client_id not in allowed_clients:
        return

    clients[client_id.decode().strip()] = (reader, writer)
    print(f"Client {client_id} connected")
    try:
        while True:
            data = await reader.read(100)
            if not data:
                break
            print(f"Data from {client_id}: {data}")
    finally:
        del clients[client_id.decode().strip()]
        writer.close()
        await writer.wait_closed()

async def main():
    server = await asyncio.start_server(handle_client, '0.0.0.0', 9999)
    async with server:
        await server.serve_forever()

asyncio.run(main())
