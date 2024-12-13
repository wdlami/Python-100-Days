import asyncio

async def task(i, duration):
    print(f"Task {i} started")
    await asyncio.sleep(duration)
    print(f"Task {i} completed")
    return f"Result {i}"

async def main():
    tasks = [asyncio.create_task(task(i, duration)) for i, duration in enumerate([3, 2, 1, 5], start=1)]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)

    print("Some tasks are completed:")
    for t in done:
        print(await t)  # 打印已经完成的任务结果

    print("Remaining tasks are still running:")
    for t in pending:
        print(f"Task {t.get_name()} is still pending")

asyncio.run(main())
