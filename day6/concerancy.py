import asyncio

async def foo():
    await asyncio.sleep(1)
    print("Foo")

async def bar():
    await asyncio.sleep(2)
    print("Bar")

async def main():
    await asyncio.gather(foo(), bar())

asyncio.run(main())
