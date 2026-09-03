import asyncio


async def download(name, delay):
    print(f"{name}: started")

    await asyncio.sleep(delay)

    print(f"{name}: finished")

    return f"{name} complete"


async def main():
    result1 = await download("File 1", 2)
    result2 = await download("File 2", 1)

    print(result1)
    print(result2)


asyncio.run(main())