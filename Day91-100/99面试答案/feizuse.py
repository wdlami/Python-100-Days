import asyncio
import time

async def async_task(name):
    print(f"{name} start")
    # time.sleep(3)  # 阻塞操作：阻塞整个事件循环
    await asyncio.sleep(3)

    print(f"{name} end")

async def main():
    await asyncio.gather(
        async_task("Task 1"),
        async_task("Task 2"),
    )

asyncio.run(main())
