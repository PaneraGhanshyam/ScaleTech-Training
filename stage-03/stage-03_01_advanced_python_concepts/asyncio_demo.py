import asyncio


async def task(name, delay):
    print(f"{name} started")

    await asyncio.sleep(delay)

    print(f"{name} finished")


async def main():
    await asyncio.gather(
        task("Task 1", 3),
        task("Task 2", 2),
        task("Task 3", 1)
    )


asyncio.run(main())