import asyncio

async def forward_to_local(local_host, local_port, request_data):
    reader, writer = await asyncio.open_connection(local_host, local_port)
    writer.write(request_data)
    await writer.drain()

    response = b""
    while True:
        chunk = await reader.read(1024)
        if not chunk:
            break
        response += chunk

    writer.close()
    await writer.wait_closed()
    return response

async def tunnel_client(local_host, local_port, server_host, server_port, client_id):
    reader, writer = await asyncio.open_connection(server_host, server_port)
    writer.write((client_id + "\n").encode())
    await writer.drain()

    try:
        while True:
            data = await reader.read(4096)
            if not data:
                break

            print(f"Received request from tunnel server:\n{data.decode(errors='ignore')}")

            # Forward request to local server
            local_response = await forward_to_local(local_host, local_port, data)

            # Send response back to tunnel server
            writer.write(local_response)
            await writer.drain()

    except Exception as e:
        print(f"Error: {e}")
    finally:
        writer.close()
        await writer.wait_closed()

# Run the tunnel client
asyncio.run(tunnel_client(
    local_host='127.0.0.1',
    local_port=8000,
    server_host='your-server-ip',
    server_port=9999,
    client_id='client123'
))
