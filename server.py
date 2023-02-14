import asyncio

HOST = '0.0.0.0'
PORT = 5454
WRITERS = set()


async def handle_echo(reader, writer):
    WRITERS.add(writer)

    while True:
        data = await reader.read()
        if not data:
            writer.close()
            break

        for w in WRITERS:
            if w == writer:
                continue
            w.write(data)

        await asyncio.gather(*(w.drain() for w in WRITERS if w != writer))


async def main():
    server = await asyncio.start_server(
        handle_echo, HOST, PORT)

    address = ', '.join(str(s.getsockname()) for s in server.sockets)
    print(f'Serving on {address}')

    async with server:
        await server.serve_forever()

asyncio.run(main())
