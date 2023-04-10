#協程
#協程是一種輕量級的執行序，它在同一個執行序中運行，可以在適當的時候暫停和繼續執行，不需要進程或線程的切換開銷，可以更高效地利用CPU和內存資源。
#Python的協程實現方式有多種，比如Generator、async/await、greenlet等。
# 其中，async/await是Python 3.5版本以後新增的原生協程實現方式，也是最為常用的方式。
import asyncio

async def worker():
    for i in range(100000):
        pass

async def main():
    tasks = []
    for i in range(10):
        tasks.append(asyncio.create_task(worker()))
    await asyncio.gather(*tasks)

asyncio.run(main())
